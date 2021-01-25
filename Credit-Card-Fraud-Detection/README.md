# Credit Card Fraud Detection

by Bo Tian


This project is an exploration of the kaggle credit card fraud detection dataset. The project was a great opportunity to learn about outlier/anomaly detection techniques as well as to build models dealing with heavily imbalanced classes.

The dataset provide was very clean so we focus more on implementing streamlined model building pipelines and learning about various anomaly detection techniques.

## Method Applied
    - Logistic Regression
    - Tree Ensembles
    - Isolation Forests
    - One Class SVM
    - Robust Covariance estimates
    - Local Outlier Factor
    - Use statistical and un-supervised anomaly detection techniques to try to identify core boundary of real charges and identify anything outside this boundary as fraudulent.
    - Use the outputs from the anomaly detection techniques as additional features in the classification models.

## Key Steps

* Feature engineering such as scaling and deskewing
* Tried down-sampling and over-sampling 
* Optimized hyperparameters via a grid search with 5-fold cross-validation
* Metrics: (accuracy，precision, recall，F1)
* Used L2 regularization to prevent overfitting  
* Used confusion matrix and recall to analyze the effectiveness of the choice of threshold
* Compare the performance with other models

## Data

The [dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud), hosted on Kaggle, includes credit card transactions made in September 2013 by European cardholders. The data contains 284,807 transactions that occurred over a two-day period, of which 492 (0.17%) are fraudulent. Each transaction has 30 features, all of which are numerical. The features `V1, V2, ..., V28` are the result of a PCA transformation. To protect confidentiality, background information on these features is not available. The `Time` feature contains the time elapsed since the first transaction, and the `Amount` feature contains the transaction amount. The response variable, `Class`, is 1 in the case of fraud, and 0 otherwise.

## Result 
On a test set consisting of 25% of the original data, the predictions from the Logistic regression had an F1 score of 0.869 and a Matthews correlation coefficient (MCC) of 0.869. I also trained random forest and linear support vector classifier models, but these models  did not overperform the logistic regression.
