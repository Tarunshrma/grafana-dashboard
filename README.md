**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

## Describe SLO/SLI
SLOs
    SLO stands for Service level objectives. It is the promise or target committed to stakeholders/customers usually documented by Service level agreement(SLA).

    **Monthly uptime** 
        Application should remain available 99.95%/month. 
    **Request response time**
        Avg. api letancy should be less then 1 seconds.
SLIs
    SLI Stands for Service level indicator. It is the quantetative measure of SLO to keep check if SLOs are met or not. SLA may define panelties on missing the SLO. Thus SLIs are very critical to measure. 
    **Monthly uptime**
        Application was available 99.9% during last month.
            SLO Achieved.
    **Request response time**
        5% of all api's took more then 1 seconds to respond. 
            SLO Failed, need to do the root cause analysis and fixed the slow api's to achieve the SLO.    

## Creating SLI metrics.
SLI indicates if an application is achieving it's desireable output. It also helps identifying some of potential problems that should be fixed to keep the application healthy. SLI matrics can be derived from Four golden signals i.e. Letancy, Traffic, Errors & Saturation. Some exmaples of matrices are as below: 
    1) Letancy: Time taken by service to respond. Slow signup service can result losing the potential customer/user. e.g. **Avg. time taken by signup service is 1.5 seconds over a period of black friday sale.**
    2) Traffic: How much load can be handled by application at any given time. During FIFA final worldcup streaming on any OTT platform should be able to handle millions of concurrent streaming request. **Popular OTT Platform succesfully handled 50 Million Concurrent Request During FIFA World Cup Final**
    3) Errors: Number of failed requests or unexpected result for a request. e.g. HTTP 503 status signals temporary overloading or maintenance of the server. **Only 0.01% of ticket booking service resulted error during Justin Bieber concert. It was within agreeable range of 99.95%**
    4) Saturation: This indicates the resources consumption by application services. More saturated services means application may become slow due to resource scarcity. Some examples are CPU utilization, Memory Usage, I/O rates for DB. **Maximum memory consumption for GPU Intensive game app on mobile device should not exceeds 2GB**
    5) Resilient: This is another critical matrix to track, how early an application/system could recover from a failed state. **Pod should recreate within 2 seconds in case of failure to fulfill desired replica requests configured in menifast file**    

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
