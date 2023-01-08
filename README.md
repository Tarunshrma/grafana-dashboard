**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

TASK : Run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

![kubectl-all-resources](./answer-img/kubectl-all-resources.png?raw=true "All Resources")
![kubectl-monitoring](./answer-img/kubectl-monitoring.png?raw=true "Monitoring")
![kubectl-observablity](./answer-img/kubectl-observablity.png?raw=true "Monitoring")
![kubernetes-overview](./answer-img/kubernetes-overview.png?raw=true "Overview")

## Setup the Jaeger and Prometheus source

TASK : Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

![grafana-home-screen](./answer-img/grafana-home-screen.png?raw=true "Grafana Home Screen")


## Create a Basic Dashboard
TASK: Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![prometheus-dashboard](./answer-img/prometheus-dashboard.png?raw=true "Prometheus Dashboard")


## Describe SLO/SLI
- **SLO**
    SLO stands for Service level objectives. It is the promise or target committed to stakeholders/customers usually documented by Service level agreement(SLA).

    - **Monthly uptime** 
        Application should remain available 99.95%/month. 
        
    - **Request response time**
        Avg. api letancy should be less then 1 second.
- **SLI**
    SLI Stands for Service level indicator. It is the quantitative measure of SLO to keep check if SLOs are met or not. SLA may define panelties on missing the SLO. Thus SLIs are very critical to measure. 

    - **Monthly uptime**
        Application was available 99.9% during last month.
        SLO Achieved.
        
    - **Request response time**
        5% of all api's took more then 1 second to respond. 
        SLO Failed, need to do the root cause analysis and fixed the slow api's to achieve the SLO.  

## Creating SLI metrics.
SLI indicates if an application is achieving it's desirable output. It also helps identify some potential problems that should be fixed to keep the application healthy. SLI metrics can be derived from four golden signals i.e. Lenacy, traffic, Errors & Saturation. Some examples of matrices are as below

- **Letancy**: Time taken by service to respond. Slow signup service can result losing the potential customer/user. e.g. `Avg. time taken by signup service is 1.5 seconds over a period of black friday sale.`

- **Traffic**: How much load can be handled by application at any given time. During FIFA final worldcup streaming on any OTT platform should be able to handle millions of concurrent streaming request. `Popular OTT Platform successfully handled 50 Million Concurrent Request During FIFA World Cup Final`

- **Errors**: Number of failed requests or unexpected result for a request. e.g. HTTP 503 status signals temporary overloading or maintenance of the server. `Only 0.01% of ticket booking service resulted error during Justin Bieber concert. It was within the agreeable range of 99.95%`
 
- **Saturation**: This indicates the resource consumption by application services. More saturated services mean applications may become slow due to resource scarcity. Some examples are CPU utilization, memory use, I/O rates for DB. `Maximum memory consumption for GPU Intensive game app on mobile device should not a exceed 2GB`
 
- **Resilient**: This is another critical matrix to track, how early an application/system could recover from a failed state. `Pod should recreate within 2 seconds in case of failure to fulfill desired replica requests configured in menifast file`

## Create a Dashboard to measure our SLIs
Task: Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

![app-dashboard](./answer-img/app-dashboard.png?raw=true "App ashboard")


## Tracing our Flask App
Task: We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

![jeager-backend-traces](./answer-img/jeager-backend-traces.png?raw=true "Jeager Backend Traces")

![jeager-backend-code](./answer-img/jeager-backend-code.png?raw=true "Jeager Backend Code")

## Jaeger in Dashboards
Task: Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

![grafana-jeager-dashboard](./answer-img/grafana-jeager-dashboard.png?raw=true "Grafana Jeager Dashboard")


## Report Error

TROUBLE TICKET

Name: Tarun Sharma

Date: 8 January 2023

Subject: Api request failing with "500: Internal Server Error" 

Affected Area: Frontend app "Press Me For Bad Test" feature is breaking.

Severity: Critial

Description: When user cliks on "Press Me For Bad Test" button on frontend home page, it is causing error in "trial" app with "500: Internal Server Error". On further investigation for Jeager below error is captured

`	
  File "/app/app.py", line 50, in homepage
    span.set_tag("first-tag", len(res.json()))
  File "/usr/local/lib/python3.7/site-packages/requests/models.py", line 910, in json
    return complexjson.loads(self.text, **kwargs)
  File "/usr/local/lib/python3.7/json/__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "/usr/local/lib/python3.7/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/local/lib/python3.7/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
`   

For detail please check the screenshot below how to track the error on Jeager    

![jeager-error-report-timeline](./answer-img/jeager-error-report-timeline.png?raw=true "Jeager Error Report Timeline")

![jeager-error-report-stack-trace](./answer-img/jeager-error-report-stack-trace.png?raw=true "Jeager Error Report Stacktrace")

## Creating SLIs and SLOs
Task: We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

Below are some of the SLI that indicating application is fulfilling the SLO target of 99.95%/month

- All Services i.e. Backend & Fronend should be available more then 99.95% over a period of a month.
- Failure requests (4XX and 5XX) should be less then 0.05% of overall http requests over a period of a month.
- Avg. response time should be less then 500ms over a period of a month.
- CPU and Memory threshold not exceeded more then defined thresholds over a period of a month 
  - CPU threshold = 70%
  - Memory threhold = 500 Mib   

## Building KPIs for our plan
Task: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

- All Services i.e. Backend & Fronend should be available more then 99.95% over a period of a month.
  - **Uptime:** This KPI will determine the availablity of application.
  - **Failed Http Requests:** This KPI will help us identifying if some of services are not responding.
- Failure requests (4XX and 5XX) should be less then 0.05% of overall http requests over a period of a month.
  - **Failed Http Requests:** This KPI will help us identifying if some of services are not responding.
  - **Uptime:** We can track uptime to see if some error is coming because non availablity of a service.
- Avg. response time should be less then 500ms over a period of a month.
  - **Letancy:** : This KPI will determine avg. time taken to respond. 
  - **CPU/Memory Usage:** We can track cpu and memory usage to determine if application is reaching to saturation to handle the incoming traffic.
- CPU and Memory threshold not exceeded more then defined thresholds over a period of a month 
  - **CPU Usage:** Avg. cpu usage of applications, it will help us determing the letancy of application.
  - **Memory Usage:** Avg. memory usage of applications, it will help us determing the letancy of application


## Final Dashboard
Task: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

![final-dashboard](./answer-img/final-dashboard.png?raw=true "Final Dashboard")

- Memory Usage: This panel display overall memory usage of application in default namespace
- CPU Usage: This panel display overall cpu usage of application in default namespace
- Average Response Time: Avg response time of all flask http requests.
- Backend/Frontend Uptime: Applicatation uptime in hours for frontend and backend app.
- Failed Http Request: Total http requests with status code in 4XX and 5XX
- Success Http Request: Total http requests with status code 200

## Important Links:
- https://github.com/rycus86/prometheus_flask_exporter/tree/master/examples/sample-signals
- https://tracing.cloudnative101.dev/docs/lab-jaeger-nodejs.html