# UCI_Drug_Review_Analysis

Author: Bo Tian

Date: 10/25/2020

In this notebook, we went through hands on analysis on [UCI ML Drug Review dataset](https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29) and build a simple item-based medication recommendation system given customer's medical condition.

## The Description of the Dataset:
The dataset was originally published on the based on the the following publication:

    Felix Gräßer, Surya Kallumadi, Hagen Malberg, and Sebastian Zaunseder. 2018. Aspect-Based Sentiment Analysis of Drug Reviews Applying Cross-Domain and Cross- Data Learning. In Proceedings of the 2018 International Conference on Digital Health (DH '18). ACM, New York, NY, USA, 121-125.

The data set consists of train and test part (split as 0.75-0.25). These are additional explanations for the features.

- drugName (categorical): name of drug 
- condition (categorical): name of condition
- review (text): patient review 
- rating (numerical): 10 star patient rating 
- date (date): date of review entry 
- usefulCount (numerical): number of users who found review useful

The structure of the data is that a patient with a unique ID purchases a drug that meets his condition and writes a review and rating for the drug he/she purchased on the date. Afterwards, if the others read that review and find it helpful, they will click usefulCount, which will add 1 for the variable.

## List of Possible Questions:

* Classification: Can you predict the patient's condition based on the review?
* Regression: Can you predict the rating of the drug based on the review?
* Sentiment analysis: What elements of a review make it more helpful to others? Which patients tend to have more negative reviews? Can you determine if a review is positive, neutral, or negative?
* Data visualizations: What kind of drugs are there? What sorts of conditions do these patients have?
* What insights can we gain from exploring and visualizing our data?
* How does sentiment play into rating and usefulness of reviews?
* Can we create a way for people to find the best medication for their illness?
* What machine learning models work best for predicting the sentiment or rating based on review?
* Is this problem better suited for classification or regression? In other words, should we be trying to sort the reviews into categories based on sentiment or predict the actual rating of the review?
* What vectorization methods for the reviews are the most efficient and preserve the most data as well as allowing for the most accuracy?
* Can we somehow find insight into what features or words are most important for predicting review rating?

## Results: 
* The sentiment analysis problem could've been framed as either a classification or regression problem depending on the approach.
* In the future, plan to do more feature engineering to develop insights and meaningful conclusions.
* The neural network seems to give the best overall accuracy with 89.4%. Exploring different NN architecture could've been very beneficial, as recurrent nets are known to work very well for NLP problems.
(to be updated)
 
