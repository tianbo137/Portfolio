# NBA Game Result Prediction


**An end-to-end machine learning project to predict NBA game winner**


by **Bo Tian**


![Cuban](https://github.com/tianbo137/Portfolio/blob/main/Images/cuban.png)

## Overview

In this project, I attempt to build a profitable NBA game winner prediction model against the odds of bookmakers. 

The data includes player game-level stats pulled from the [NBA stats website](http://stats.nba.com/) with [nba_api](https://github.com/swar/nba_api) and game odds from [covers.com](http://covers.com) using the Python web scraping framework [Scrapy](https://scrapy.org/). 

The model is a wide-and-deep neural network model together with a custom loss function to assist us identifying fair odds.

## Contents:

- [odds_data](https://www.sportsbookreviewsonline.com/scoresoddsarchives/nba/nbaoddsarchives.htm): Historical scores and odds data from past NBA seasons including moneylines, 2nd half lines, opening and closing point spreads and totals. 
- [game_data](): Python module with support functions to perform tasks including collecting stats to a SQLite database, simulating seasons, and customizing plots
- [notebooks](): Jupyter notebooks of all analyses


## What is covered
- Data wrangling with Pandas & data storage with SQLite
- Machine learning (Neural Network) with Keras
- Web app with Flask (and a bit of CSS & HTML)
- App deployment with Docker and Heroku


## Reference
- [Exploiting sports-betting market using machine learning](https://www.researchgate.net/publication/331218530_Exploiting_sports-betting_market_using_machine_learning)
- [Predict NBA games, make money — machine learning project](https://towardsdatascience.com/predict-nba-games-make-money-machine-learning-project-b222b33f70a3)
- [Beating the Bookies with Machine Learning](https://www.kdnuggets.com/2019/03/beating-bookies-machine-learning.html)
- [Sentiment Bias in National Basketball Association Betting](https://journals.sagepub.com/doi/abs/10.1177/1527002516656726)
- [SENTIMENT BIAS AND ASSET PRICES: EVIDENCE FROM SPORTS BETTING MARKETS AND SOCIAL MEDIA](https://onlinelibrary.wiley.com/doi/abs/10.1111/ecin.12404)
- [Databall](https://klane.github.io/databall/)
- [How to Create a Custom Loss Function | Keras](https://towardsdatascience.com/how-to-create-a-custom-loss-function-keras-3a89156ec69b)
- [Wide & Deep Learning: Better Together with TensorFlow](https://ai.googleblog.com/2016/06/wide-deep-learning-better-together-with.html)
- [Implement DeepFM model in Keras](https://6chaoran.wordpress.com/2019/01/03/implement-deepfm-model-in-keras/)
- [How to build a wide-and-deep model using Keras in TensorFlow 2.0](https://towardsdatascience.com/how-to-build-a-wide-and-deep-model-using-keras-in-tensorflow-2-0-2f7a236b5a4b)
- [Making real-time predictions for NBA basketball games by combining the historical data and bookmaker’s betting line](https://reader.elsevier.com/reader/sd/pii/S0378437120301618?token=2F7EFE5E4C003EAAEDF06C7D64E80840BC39D53972A73C756558AAEF452BFA8BE5E86389D9B798356604A233187DB845)
- [Predicting the outcome of NBA games with Machine Learning](https://towardsdatascience.com/predicting-the-outcome-of-nba-games-with-machine-learning-a810bb768f20)
- [Predict NBA Player Lines with Monte Carlo Simulation](https://towardsdatascience.com/predict-nba-player-lines-with-monte-carlo-simulation-58a1c006a6e2)
-[Prediction of NBA games based on Machine Learning Methods](https://homepages.cae.wisc.edu/~ece539/fall13/project/AmorimTorres_rpt.pdf)
- [The benefits of using Floor Impact Counter in the NBA](https://www.pinnacle.com/en/betting-articles/Basketball/floor-impact-counter-explanation/34L28L6QWDDUP8UT)
- [Building an NBA MySQL Database With Python](https://medium.com/@jman4190/building-an-nba-mysql-database-with-python-c653fa15333c)
- [Advanced basketball analytics](https://www.kaggle.com/virtonos/advanced-basketball-analytics)
- [Basketball EDA - Plotly + DABL](https://www.kaggle.com/heyytanay/basketball-eda-plotly-dabl)
- [Basketball prediction](https://www.kaggle.com/dimashmundiak/basketball-prediction)
- [The Best And Worst Defenders](https://www.kaggle.com/edwardyun/the-best-and-worst-defenders)
- [NBA games EDA - let's dive into the data 🏀](https://www.kaggle.com/nathanlauga/nba-games-eda-let-s-dive-into-the-data)
- [An end-to-end machine learning project with Python Pandas, Keras, Flask, Docker and Heroku](https://towardsdatascience.com/an-end-to-end-machine-learning-project-with-python-pandas-keras-flask-docker-and-heroku-c987018c42c7)
- [How We Calculate NBA Elo Ratings](https://fivethirtyeight.com/features/how-we-calculate-nba-elo-ratings/#:~:text=Here's%20the%20formula%3A%20Take%20the,and%20then%20divide%20by%2028.)
- [NBA’s Winning Factor: How to Make Playoff](https://rstudio-pubs-static.s3.amazonaws.com/423157_b5d8f86694ef4cca82465f60af3b97c2.html)
- [NBA Win Percentage Predictor](https://github.com/Vajrasamaya/Predicting-NBA-Win-Percentage)
