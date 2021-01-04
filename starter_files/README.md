# Consuming AutoML model and Pipeline experiment runs via REST API endpoints

## Project Overview

Our objective is to leverage Azure’s Machine Learning (AML / ML) studio to train a cloud-based machine learning production model, deploy the model, and retrieve its REST endpoint for consumption. The training data is from a Portuguese banking institution and the ML goal is to predict if a client will subscribe to a term deposit following a marketing campaign. This, therefore, is a classification problem. Additionally, we will leverage Azure’s Python SDK to create, publish, and consume a pipeline to continuously execute future ML experiments for this task. The publish step of our pipeline also makes a REST endpoint / HTTP API available to us for consumption.
To execute on this workflow, we must first establish a user as the service principal / owner. This core action allows us to automate the entire training, publishing, and consumption of our ML pipelines. Next, we will use Azure’s Graphical User interface (GUI) to conduct an ML experiment by configuring Azure’s AutoML framework. Once these experiments are complete, we will retrieve the best model, deploy it to retrieve a REST endpoint that Azure provides, and later consume that model via its endpoint to score data. We will also perform load tests with Apache Bench simulating multiple POST requests to the endpoint. This helps us to benchmark our average response time to Azure’s 60 second benchmark and it allows to check our model endpoint’s health status. 
Lastly, we will re-submit our experiment using an Azure ML pipeline strategy. We will create, publish, and consume our pipeline also via a REST endpoint. We will leverage Azure’s Python SDK to execute the pipeline steps. This approach allows us to automate future pipeline deployments, via the pipeline’s REST endpoint, with a Python script. Authentication is also crucial to our pipeline automation.


## Architectural Diagram

**AutoML Model Consumption Architecture with AML GUI**
![automl architecture](images\architecture_automl.png)

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
