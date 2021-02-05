# Starbucks Offer Personalizations: Using Starbucks app user data to predict effective offers

## 1. Installations
This project was written in Python, using Jupyter Notebook on Anaconda. The relevant Python packages for this project are as follows:

- pandas
- numpy
- math
- json
- sklearn.model_selection (train_test_split module)
- sklearn.preprocessing (StandardScaler, PolynomialFeatures)
- from sklearn.tree (DecisionTreeClassifier,DecisionTreeRegressor)
- sklearn.ensemble (RandomForestClassifier)
- sklearn.metrics (mean_squared_error,classification_report)
- sklearn.linear_model (Ridge)
- time
- sklearn.model_selection (GridSearchCV)
- matplotlib

## 2. Project Motivation

In this project, I use the simulated data that mimics customer behavior on the Starbucks rewards mobile app to answer 2 business questions:

  - a. What are the main drivers of an effective offer on the Starbucks app?
  - b. Could the data provided, namely offer characteristics and user demographics, predict whether a user would take up an offer?

To answer the above 2 questions, I created 3 models for the data on the 3 offer types provided. The three offers are: Buy One Get One Free (BOGO), Discount (discount with purchase), and Informational (provides information about products).

As a brief summary of my findings:
- For Question 1, the feature importance given by all 3 models were that the tenure of a member is the biggest predictor of the effectiveness of an offer. Further study would be able to indicate what average tenure days would result in an effective BOGO offer.

- For Question 2,my decision to use 3 separate models to predict the effectiveness of each offer type ended up with good accuracy for the 2 of the models (82.83% for BOGO and 87.35% for discount), while slightly less accurate performance for another informational offers (75.3%). However, I would regard 75% as acceptable in a business setting, as for informational offers, there is no cost involved to inform users of a product. Meanwhile, an 80% and above accuracy in a business setting would be acceptable to show offers to people, even if the model misclassifies a few, the overall revenue increase might justify the few mistakes.

