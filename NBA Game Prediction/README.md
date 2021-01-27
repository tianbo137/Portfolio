# <img src="docs/assets/icons/favicon.ico" width="48"> NBA Game Result Prediction

by **Bo Tian**


> As we can see from the following twitter of Mark Cuban, owner of Dallas Mavericks, how important data analytics/machine learning is for the modern era of the NBA leagure.

![Cuban](https://github.com/tianbo137/Portfolio/blob/main/Images/cuban.png)


In this project, I attempt to predict NBA game winners against the odds of bookies using stats pulled from the [NBA stats website](http://stats.nba.com/) with [nba_api](https://github.com/swar/nba_api) and game odds from [covers.com](http://covers.com) using the Python web scraping framework [Scrapy](https://scrapy.org/). All code is written in Python and I used the popular machine learning library [scikit-learn](http://scikit-learn.org/stable/) to make all predictions.

Contents:

- [odds_data](): Scrapy project to scrape point spreads and over/under lines from
- [game_data](): Python module with support functions to perform tasks including collecting stats to a SQLite database, simulating seasons, and customizing plots
- [notebooks](): Jupyter notebooks of all analyses


Link to a test database with data from 1990 - March 2021 [test nba.db file](https://drive.google.com/file/d/10CBcCLv2N_neFL39ThykcudUVUv5xqLB/view?usp=sharing)
