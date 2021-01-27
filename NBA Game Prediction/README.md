# <img src="docs/assets/icons/favicon.ico" width="48"> NBA Game Result Prediction

by **Bo Tian**


> The following twitter of Mark Cuban, owner of Dallas Mavericks, shows the importance of data analytics/machine learning towards the NBA leagure nowadays.

![Cuban](https://github.com/tianbo137/Portfolio/blob/main/Images/cuban.png)

## Overview



In this project, I attempt to build a profitable NBA game winners prediction model against the odds of those Las Vegas bookies. In particular, I will be using player game-level stats pulled from the [NBA stats website](http://stats.nba.com/) with [nba_api](https://github.com/swar/nba_api) together with game odds from [covers.com](http://covers.com) using the Python web scraping framework [Scrapy](https://scrapy.org/). 


We investigate how to use a custom loss function to identify fair odds, including a detailed example using machine learning to bet on the results of a darts match and how this can assist you in beating the bookmaker.

## Contents:

- [odds_data](): Scrapy project to scrape point spreads and over/under lines from
- [game_data](): Python module with support functions to perform tasks including collecting stats to a SQLite database, simulating seasons, and customizing plots
- [notebooks](): Jupyter notebooks of all analyses


Link to a test database with data from 1990 - March 2021 [test nba.db file](https://drive.google.com/file/d/10CBcCLv2N_neFL39ThykcudUVUv5xqLB/view?usp=sharing)

## Reference
