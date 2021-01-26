# Deploy an end-to-end ML pipeline on GCP --- KKBox Customer Churn Prediction


**Bo Tian** 

<p align="center">
  <img width="1500" height="450" src="https://github.com/tianbo137/My_Portfolio/blob/main/Images/Google_Cloud_B3.jpg">
</p>


In this project, we developed a XGBoost model and served it on Google Cloud Platform (GCP) using AI Platform. The objective of our work is to predict whether a user of the music streaming service KKBox will “churn”, i.e. leave this subscription-based service, by analysing the user’s behaviour on the website.

The key steps of this project involve:

- ETL and feature engineering using BigQuery and Datalab
- Build, fit, and hyperparameter tuning XGBoost Model 
- Save the trained model using joblib in gsc bucket
- Deploy the model using AI platform to predict on unseen data
- Used Lift chart, permutation importance, and LIME for model explainability (to do)

<p align="center">
  <img width="900" height="400" src="https://github.com/tianbo137/My_Portfolio/blob/main/Images/gcp%20ml%20pipeline.jpeg">
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
