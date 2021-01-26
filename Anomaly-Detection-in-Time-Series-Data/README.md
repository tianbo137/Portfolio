# Anomaly Detection in Time Series Data

by **Bo Tian**

## Overview of Project

In this project, I designed and trained an LSTM autoencoder (using the Keras API with Tensorflow) to detect sudden price changes in the S&P 500 index in 2020. I also created interactive charts and plots using Python Plotly and Seaborn for data visualization.

> The S&P 500 is a stock performance indicator for the top 500 companies listed on the stock exchange in the United States. It is considered as one of the best representations of the United States stock market.

### The dataset (CSV format) is obtained from Yahoo Finance and contains records of SP 500 index from 1986 to 2020 with: 
1. Daily timestamp
2. Daily Open and Close price
3. Daily High and Low price
4. Daily Volume


### The Project will follow the below steps:
1. Import Libraries
2. Load and Inspect the S&P 500 Index Data
3. Data Preprocessing
4. Temporalizing Data and Creating Training and Test Splits
5. Build an LSTM Autoencoder
6. Train the Autoencoder
7. Plot Metrics and Evaluate the Model
8. Detect Anomalies in the S&P 500 Index Data
9. Visualize the Anomalies based on threshold

## Background

### What is [anomaly detection](https://en.wikipedia.org/wiki/Anomaly_detection)?
> In data mining, anomaly detection is the identification of rare items, events or observations which raise suspicions by differing significantly from the majority of the data. 



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

## Note
> Download the python notebook and given data set and run the code in jupyter-notebook or Google Colab to experiance the interactive plots.
