# NBA Game Result Prediction


**An end-to-end machine learning web app to predict NBA game winner**


by **Bo Tian**


![Cuban](https://github.com/tianbo137/Portfolio/blob/main/Images/cuban.png)

## Overview

In this project, I attempt to build a profitable NBA game winners prediction model against the odds of bookmakers. 

The data includes player game-level stats pulled from the [NBA stats website](http://stats.nba.com/) with [nba_api](https://github.com/swar/nba_api) and game odds from [covers.com](http://covers.com) using the Python web scraping framework [Scrapy](https://scrapy.org/). 

The model is a wide-and-deep neural network model together with a custom loss function to assist us identifying fair odds.

## Contents:

- [odds_data](): Scrapy project to scrape point spreads and over/under lines from
- [game_data](): Python module with support functions to perform tasks including collecting stats to a SQLite database, simulating seasons, and customizing plots
- [notebooks](): Jupyter notebooks of all analyses


## What is covered
- Data wrangling with Pandas & data storage with SQLite
- Machine learning (Neural Network) with Keras
- Web app with Flask (and a bit of CSS & HTML)
- App deployment with Docker and Heroku


## Reference
- [Exploiting sports-betting market using machine learning](https://www.researchgate.net/publication/331218530_Exploiting_sports-betting_market_using_machine_learning)
- [Beating the Bookies with Machine Learning](https://www.kdnuggets.com/2019/03/beating-bookies-machine-learning.html)
- [Databall](https://klane.github.io/databall/)
- [How to Create a Custom Loss Function | Keras](https://towardsdatascience.com/how-to-create-a-custom-loss-function-keras-3a89156ec69b)
- [Wide & Deep Learning: Better Together with TensorFlow](https://ai.googleblog.com/2016/06/wide-deep-learning-better-together-with.html)
- [Implement DeepFM model in Keras](https://6chaoran.wordpress.com/2019/01/03/implement-deepfm-model-in-keras/)
- [How to build a wide-and-deep model using Keras in TensorFlow 2.0](https://towardsdatascience.com/how-to-build-a-wide-and-deep-model-using-keras-in-tensorflow-2-0-2f7a236b5a4b)
- [Making real-time predictions for NBA basketball games by combining the historical data and bookmaker’s betting line](https://reader.elsevier.com/reader/sd/pii/S0378437120301618?token=2F7EFE5E4C003EAAEDF06C7D64E80840BC39D53972A73C756558AAEF452BFA8BE5E86389D9B798356604A233187DB845)
