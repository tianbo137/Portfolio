# Anomaly Detection in Time Series Data

by **Bo Tian**

## Overview of Project

In this project, I designed and trained an LSTM autoencoder (using the Keras API with Tensorflow) to detect sudden price changes in the S&P 500 index in 2020. I also created interactive charts and plots using Python Plotly and Seaborn for data visualization.

> The S&P 500 is a stock performance indicator for the top 500 companies listed on the stock exchange in the United States. It is considered as one of the best representations of the United States stock market.

## So what are the recognized market anomalies?

> In data mining, anomaly detection is the identification of rare items, events or observations which raise suspicions by differing significantly from the majority of the data. 

Decades of market studies have been touted in the finance literature. Many market anomalies have been identified. Here I describe eight typical ones:
* **Momentum**: Do you sometimes observe that a rising stock price continues to rise beyond a reasonable level, or keeps falling below an unbelievable level? There seems a momentum that drives asset prices beyond their expected values.
* **“January” comes back**: This anomaly is the “January effect” and perhaps logical. Stocks that performed poorly in the fourth quarter of the previous year tend to outperform the market in January. This “calendar effect” has a good explanation: investors tend to sell their losers before the end of the year in order to write the loss off their taxes. However, this phenomenon does not repeat reliably in market history. So buying the losers of December in January does not guarantee a profitable trading strategy.
* **Days of the week**: Stocks tend to have positive results on Fridays rather than Mondays. This phenomenon is sometimes called the weekend effect and has been documented since the 1970s. But it is not sizable enough to become a profitable trading strategy. The possible explanation is that companies tend to hold bad news until after the market closes on Fridays.
* **Book-to-market ratio**: This is probably the oldest effect documented in the literature. It compares the book value of a company to its price. A large book-to-market ratio means the stock price is undervalued, otherwise overvalued. The book value of a company is derived from its historical cost or accounting value. The market value of a company is its share price in the stock market multiplying its number of outstanding shares, i.e., market capitalization. This anomaly is well-described in the classical Fama and French research paper (1993). One explanation is that investors overreact to growth aspects for growth stocks, and value stocks are therefore undervalued.
* **Neglected stocks**: It is documented in the literature that stocks of lesser-known companies are able to generate higher returns. Small stocks tend to be less analyzed by market analysts. However, is it because of a lack of attention or because it is small? The literature also found the smaller firms can exhibit better performance because of the higher risk and higher reward.
* **Price reversals**: There is a huge body of plausible studies in the literature on this topic. Stocks that did very well reversed and underperformed the market for as much a year. Similarly, stocks that underperformed for a period of time can start to outperform the market for a long period of time. This phenomenon can occur even without the fundamental financial statements to justify the price movements. What is the reason for a price reversal? This may be due to investor psychology. Unfortunately, it can be quite hard to predict the time investor sentiment starts to cause a price to suddenly increase or decrease.
* **Earnings surprises**: Investors form their expectations based on analysts’ reports. When the actual reported earnings vary greatly from the expectations, An earnings surprise can lead to a large price movement for an extended time. Foster, Olsen, and Shevlin show positive surprises lead to a price rise for as long as two months after the announcement, and negative surprises cause a large decline in the following seven days. Their study indicates anomalies can be realized if an investor simply watches earnings surprises and responds swiftly. They also show price changes are not as quick as EMH suggests.
* **Small-firm effect**: Smaller firms tend to outperform larger companies. This small-firm effect was first documented by Banz (1981) and Reinganum (1981). Many other subsequent studies found small-firm effects in other assets and markets. However, the small-firm anomaly seems disappeared since the initial publication of the papers that discovered it.


## The Dataset 
For this project, we obtained our data (in CSV format) from Yahoo Finance and contains records of SP 500 index from 1986 to 2020 with: 
1. Daily timestamp
2. Daily Open and Close price
3. Daily High and Low price
4. Daily Volume


## Project Detailed Steps
1. Import Libraries
2. Load and Inspect the S&P 500 Index Data
3. Data Preprocessing
4. Temporalizing Data and Creating Training and Test Splits
5. Build an LSTM Autoencoder
6. Train the Autoencoder
7. Plot Metrics and Evaluate the Model
8. Detect Anomalies in the S&P 500 Index Data
9. Visualize the Anomalies based on threshold

## About LSTM Autoencoder

### What is [Autoencoder](https://en.wikipedia.org/wiki/Autoencoder#:~:text=An%20autoencoder%20is%20a%20type,to%20ignore%20signal%20%E2%80%9Cnoise%E2%80%9D)?
> An autoencoder is a type of artificial neural network used to learn efficient data codings in an unsupervised manner. The aim of an autoencoder is to learn a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore signal “noise”. 


![Autoencoder](images/AE.png)

### What is [LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory)?
> Long short-term memory is an artificial recurrent neural network architecture used in the field of deep learning. Unlike standard feedforward neural networks, LSTM has feedback connections. It can not only process single data points, but also entire sequences of data. 

![LSTM](images/LSTM3-chain.png)


### What is [LSTM Autoencoder](https://machinelearningmastery.com/encoder-decoder-long-short-term-memory-networks/#:~:text=The%20Encoder%2DDecoder%20LSTM%20is,sequence%20problems%2C%20sometimes%20called%20seq2seq.&text=The%20challenge%20of%20sequence%2Dto,it%20was%20designed%20to%20address)?
> The Encoder-Decoder LSTM is a recurrent neural network designed to address sequence-to-sequence problems, sometimes called seq2seq. This architecture is comprised of two models: one for reading the input sequence and encoding it into a fixed-length vector, and a second for decoding the fixed-length vector and outputting the predicted sequence. The use of the models in concert gives the architecture its name of Encoder-Decoder LSTM designed specifically for seq2seq problems. 


## Results
![Date Vs Closing price anomalies](images/newplot_2_snip.png)

