# End-to-End Customer Churn Prediction


**Bo Tian** 

<p align="center">
  <img width="900" height="400" src="https://github.com/tianbo137/My_Portfolio/blob/main/Images/gcp%20ml%20pipeline.jpeg">
</p>


## Overview:
- [KKBOX Challenge](https://www.kaggle.com/c/kkbox-churn-prediction-challenge) offers 6 tables of customer data of 40+ GB
- We used GCP BigQuery and Datalab to analyze and build predicative models. 
- Used Lift chart, permutation importance, and LIME to explain model effectiveness

## Objective and Metric

Our goal is to predict if a given customer will churn for the next month subscription and the model metric chosen is logloss

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

My XGBoost model scored top 5% with only 8 selected features
