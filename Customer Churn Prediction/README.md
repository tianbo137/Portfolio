# Deploy an end-to-end ML pipeline on GCP --- KKBox Customer Churn Prediction


**Bo Tian** 

## 1. Overview

> “There is only one boss. The customer. And he can fire everybody in the company from the chairman on down, simply by spending his money somewhere else.”
— Sam Walton

One of the most important tasks a company faces is not just acquiring new customers but retaining existing customers. Customer retention is critical for a company’s growth and success, as the cost of acquiring a new customer is often greater than retaining an existing customer. However, accurately predicting customer churn using large scale time-series data can be particularly challenging due to temporal issues common to time-series data. In this project, we use Google Cloud Platform (GCP) to implement an extreme gradient boosting (XGBoost) model together with a wide-variety of temporal features to create a highly-accurate customer churn model. We also use Looker to explore the results to understand the key drivers of churn. 


## 2. Dataset
The dataset comes from the WSDM Cup 2018 Challenge and was provided by KKBOX, a music streaming service. The dataset consisted of subscriber data from 3 distinct sources: user activity logs, transactions, and member data spanning several months. 

Transaction details include payment method, duration of the subscription, date, membership expiry date, cancellation of the subscription, and user log contains total no of duration, no of unique songs, and the features based on the duration of songs listened by the user.

The user logs and transaction details are available only up to March. For a user whose subscription expires on April 1, the entire history is open, but for the user with expiry on April 30, most recent activities are inaccessible. Further explanations and data are available [here](https://www.kaggle.com/c/kkbox-churn-prediction-challenge/data)

## 3. GCP Pipeline

<p align="center">
  <img width="2000" height="400" src="https://github.com/tianbo137/Portfolio/blob/main/Images/ml_structure.png">
</p>

#### 3.1. Key Steps

- Data ingestion and aggregation with BigQuery from Google Cloud Storage (GCS)
- ETL and feature engineering using AI Jupyter Notebook
- Build, fit, and hyperparameter tuning XGBoost Model 
- Save the trained model using pickle in gsc bucket
- Deploy the model using AI platform as an API end-point
- Used Looker to moniter output data

#### 3.2. GCP Services 

In this project, we leveraged the following services in our solution:

- Google Cloud Storage – A scalable object storage service
- Google BigQuery – A fully managed, serverless, pay-as-you-go data warehouse solution
- Google AI Platform – A one-stop shop to build and deploy models within the GCP infrastructure
- Looker – A web-based visualization tool


#### 3.3. AI Platform 



In particular, the bulk of our solution leverages GCP’s AI Platform, which provides a portal into GCP’s suite of machine learning services. The AI Platform has six main components: AI Hub, Data Labeling, Notebooks, Jobs and Models. This example utilizes the Notebooks and Models capabilities of GCP’s AI Platform.
- Notebooks — Provides the ability to spin up JupyterLab servers, pre-built with all the general machine learning frameworks needed. Enables scaling up or down on hardware, connecting to a compute cluster, and connecting to other services within the GCP ecosystem.
- Models — Provides a model repository for model version control and monitoring model deployments and availability. Enables endpoint setup to allow models to be called in serverless functions.



## 4. The Churn Model


Step 1: Clean & Land the Data
We landed the dataset in . GCS is often used as a data lake and houses raw data. In production, this raw data would be collected and stored from a variety of business workstreams. We used an AI Notebook environment to write a script that merges and cleans the data to meet Analytics & Data Warehousing Standards. This data is then staged back into GCS as a csv file.Step 2: Load Data into BigQuery
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

- [Predicting Customer Churn: Extreme Gradient Boosting with Temporal Data](https://arxiv.org/pdf/1802.03396.pdf)
