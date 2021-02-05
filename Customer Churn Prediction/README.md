# Deploy an end-to-end ML pipeline on GCP --- KKBox Customer Churn Prediction


**Bo Tian** 

## Overview

> “There is only one boss. The customer. And he can fire everybody in the company from the chairman on down, simply by spending his money somewhere else.”
— Sam Walton

> One of the most important tasks a company faces is not just acquiring new customers but retaining existing customers. Customer retention is critical for a company’s growth and success, as the cost of acquiring a new customer is often greater than retaining an existing customer.

Accurately predicting customer churn using large scale time-series data is a common problem facing many business domains. The creation of model features across various time windows for training and testing can be particularly challenging due to temporal issues common to time-series data. In this paper, we will explore the application of extreme gradient boosting (XGBoost) on a customer dataset with a wide-variety of temporal features in order to create a highly-accurate customer churn model. In particular, we describe an effective method for handling temporally sensitive feature engineering. The proposed model was submitted in the WSDM Cup 2018 Churn Challenge and achieved first-place out of 575 teams.
Customer churn can be addressed by 1) predicting at-risk customers and intervening with proactive support, and 2) learning what is driving customers to leave and developing strategies to prevent future churn. We used Google Cloud Platform (GCP) to develop a customer churn model and Looker to explore the results to understand the key drivers of churn for a Telecom company. We leveraged the following services in our solution:

- Google Cloud Storage – A scalable object storage service
- Google BigQuery – A fully managed, serverless, pay-as-you-go data warehouse solution
- Google AI Platform – A one-stop shop to build and deploy models within the GCP infrastructure
- Looker – A web-based visualization tool

## Telecom Customer Data
For this use case, we used customer data from a Telecom company. The data is a one-month snapshot of customer information, including customers who left in the last month, registered services (speed, contract length), and account information (tenure, monthly payments, support interactions, total spend). The dataset represents three sources: Service (Internet, Phone, Security, etc.), Account, and Customer Demographic information. Using this data, we built a logistic regression model to predict whether a customer would churn (yes/no) in the following month.

## AI Platform
The bulk of our solution leverages GCP’s AI Platform, which provides a portal into GCP’s suite of machine learning services. The AI Platform has six main components: AI Hub, Data Labeling, Notebooks, Jobs and Models. This example utilizes the Notebooks and Models capabilities of GCP’s AI Platform.
- Notebooks — Provides the ability to spin up JupyterLab servers, pre-built with all the general machine learning frameworks needed. Enables scaling up or down on hardware, connecting to a compute cluster, and connecting to other services within the GCP ecosystem.
- Models — Provides a model repository for model version control and monitoring model deployments and availability. Enables endpoint setup to allow models to be called in serverless functions.

In this project, we developed a XGBoost model and served it on Google Cloud Platform (GCP) using AI Platform. The objective of our work is to predict whether a user of the music streaming service KKBox will “churn”, i.e. leave this subscription-based service, by analysing the user’s behaviour on the website.

GCP Pipeline & Process Overview
Google Cloud Platform is easy to navigate and thread different services together to create a pipeline for any analytics project. Our process included four major steps: landing the data into Google Cloud Storage, loading the data into BigQuery, building a model in AI Platform, and visualizing the data in Looker.
The key steps of this project involve:

Step 1: Clean & Land the Data
We landed the dataset in Google Cloud Storage (GCS). GCS is often used as a data lake and houses raw data. In production, this raw data would be collected and stored from a variety of business workstreams. We used an AI Notebook environment to write a script that merges and cleans the data to meet Analytics & Data Warehousing Standards. This data is then staged back into GCS as a csv file.
Step 2: Load Data into BigQuery
BigQuery is GCP’s serverless, petabyte-scale, pay-as-you-go data warehouse solution. The BigQuery console allows us to select our staged data in GCS. BigQuery can auto-detect the schema of our file, making this just a point-and-click load of our data into this service.
Step 3: XGBoost
The AI Notebook environment provides a BigQuery extension as part of the GCP Python SDK. We used this client to query against BigQuery and load the data locally into a Pandas data frame. BigQuery maintains a single source of truth for the business, rather than needing to load intermediate stage data from GCS. With data available in a Pandas data frame, we can iterate quickly and execute our model experiment design local to the AI Notebook environment.
We approached customer churn as a binary classification problem: churn or no-churn. We used the SciKit-Learn framework to create a model pipeline object containing a preprocessor and a logistic regression predictor.

Step 4: Deploying the Model
With the exported model object saved in GCS, we are now ready to deploy the model as a serverless function via the Models section of the AI Platform. To deploy the model, we need to supply the following: object store directory, RunTime environment, custom set up modules and the model name. The ML Model is then callable via an API call, making it accessible as an independent microservice.
The term model in the AI Platform is a reference to the endpoint to be called for different business scenarios. This feature provides the ability to independently manage version control for various models.
After calling the model, we can write the inferences back to BigQuery via the BigQuery Client Library. The results of the customer churn model are then available for the business users via a Looker Dashboard to review and decide what preventative measures to implement.
Step 5: Tracking Customer Churn
In order to easily track and manage customer churn, we created a Looker dashboard with the model output and source data by connecting directly to BigQuery. The dashboard provides business users insights into the customers at risk of churn along with the customer information.
The Looker to BigQuery connection is enabled by creating a Looker-specific service account. The service account has access to directly query from and write temporary tables to BigQuery. With a live connection, the dashboard is able to display real-time results from when the model returns new output.
This dashboard highlights customers who are predicted to churn and allows users to dig into detailed account-level information. Overall, this dashboard enables a team to gain insights on at-risk customers and develop strategies to prevent future churn.

- Data ingestion with BigQuery from GCS
- ETL and feature engineering using AI Jupyter Notebook
- Build, fit, and hyperparameter tuning XGBoost Model 
- Save the trained model using joblib in gsc bucket
- Deploy the model using AI platform to predict on unseen data
- Used Lift chart, permutation importance, and LIME for model explainability (to do)

<p align="center">
  <img width="1200" height="800" src="https://github.com/tianbo137/My_Portfolio/blob/main/Images/architecture.png">
</p>


## Dataset:

[KKBOX Challenge](https://www.kaggle.com/c/kkbox-churn-prediction-challenge) offers 6 tables of customer data of 40+ GB


## Metric

For this challenge, we will be using logloss as the measuring metric

## Selected Features

|Feature|Explanation|Table|Usage|
|-------|----|----|-----|
|six_month_day_listen|Total Number of Songs Listened in the Past 6 Month|User_logs|User Usage Pattern|
|six_month_user_latent_satisfaction|User Satisfaction over the Last 6 Month|User_logs|User Satisfaction|
|one_month_day_listen|Total Number of Songs Listened in the Past 1 Month|User_logs|User Usage Pattern|
|registered_via|Device used for Registration|members|User Profiling|
|age_under_26|If the User's Age is Less than 26|members|User Profiling|
|last_last_churn|If the User was Churned last Month|transactions|User Behavior Pattern|
|client_level_code|The number of subscription Renewal|transactions|User Behavior Pattern|
|last_auto_renew|If the last renewal was via Autorenew|transactions|User Behavior Pattern|


## Result

My XGBoost model scored top 5% with only 8 selected features for this competition and deployed the model as a microservice

## Reference

- [Getting started: training and prediction with Keras](https://cloud.google.com/ai-platform/docs/getting-started-keras)

- [Predictions with scikit-learn and XGBoost](https://cloud.google.com/ai-platform/prediction/docs/getting-started-scikit-xgboost#xgboost)

- [Cloud Academy](https://cloudacademy.com/course/introduction-to-google-cloud-machine-learning-engine/tensorflow/)
