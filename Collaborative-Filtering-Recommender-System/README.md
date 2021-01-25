# Collaborative-Filtering-Recommender-System
This repository is about the movie recommendation with collaborative filtering approach.

## Idea Flow
- Split the original dataset into training and testing;
- Use 'pd.pivot_table' to convert dataframe into matrix;
- Use matrix factorization to find the best parameters that minimize the cost function;
- Tune hyperparameter related to regularization to avoid overfitting;
- Predict the missing rating scores;
- Make recommendations.

## Visitor Cold Start Problem
Recommendation systems work great when you already have lots of reviews. But you don't know enough about first time users to make personalized recommendations. To work around this problem, you can recommend based on average ratings.

## Key Concepts
### Content-based Recommender System
Content-based recommender system uses the knowledge of each product to recommend new products. It tries to recommend products that have similar attributes to a product that the user already liked. 

It can work well if you have descriptive data available for every product. It does not require any comparison among users.

But create the script of data for every product is time-consuming and introduces a lot of subjectivity that can throw off the recommendation results. For example, people may have different judgment criteria about the taste of the food. 

### Collaborative Filtering Recommender System 
Collaborative filtering uses the "wisdom of the crowd" to recommend items. It makes recommendations only based on how users rated products in the past, not based on anything about the products themselves. The assumption behind is that customers who had similar tastes in the past, will have similar tastes in the future. 

Collaborative filtering has a very big advantage over content-based recommendations. You do not need to know anything about the products that you are recommending. As long as you have user review data, you can build a collaborative filtering recommendation system. 

However, it is difficult to recommend products to brand new users because new users have not reviewed any products yet. 

### Matrix Factorization
Assume that a user's rating is a reflection of how much a particular movie appeals to that user's unique set of interests. The rating generating process works as following:
-	Model how much a movie appeals to every possible interest
-	Model the user’s interests
-	Calculate user’s rating based on how well the user’s interests match the movie’s attributes

However, user’s attributes and movies attributes are latent to you. You have to work backwards to reveal those latent attributes based on the rating scores known to you. Matrix factorization is to find the best parameters (attributes) that would generate the known rating scores. 

Reference: https://www.lynda.com/Data-Science-tutorials/Machine-Learning-Fundamentals-Learning-Make-Recommendations/563030-2.html
