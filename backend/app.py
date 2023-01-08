from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

from jaeger_client import Config
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

import logging

def initialize_tracer():
    """
    Initializes an instance of the Jaeger tracer.
    """

    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)

    open_tracing_config = {"sampler": {"type": "const", "param": 1}, "logging": True}
    tracer_config = Config(open_tracing_config, service_name="backend")

    return tracer_config.initialize_tracer()


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)
metrics = GunicornInternalPrometheusMetrics(app)

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(ConsoleSpanExporter())
)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
tracer = initialize_tracer()


@app.route("/")
def homepage():
    with tracer.start_span("hello-world") as span:
        span.set_tag("hello-world-tag", "hello")
    return "Hello World"


@app.route("/api")
def my_api():
    with tracer.start_span("from-my-api") as span:
        answer = "something"
        span.set_tag("my-api", answer)

    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    with tracer.start_span("create-star") as span:
        star = mongo.db.stars
        name = request.json["name"]
        distance = request.json["distance"]
        star_id = star.insert({"name": name, "distance": distance})
        new_star = star.find_one({"_id": star_id})

        span.set_tag("star-name", name)

        output = {"name": new_star["name"], "distance": new_star["distance"]}

    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
