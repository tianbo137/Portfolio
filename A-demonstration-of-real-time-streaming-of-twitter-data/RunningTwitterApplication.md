# Running the application:

1. For running the application, you will require access tokens from Twitter. If you don't have, refer <a href='https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html'> this</a>.

2. Before running the application, make sure that you have installed Twitter's tweepy API and findspark
    ```
    sudo pip3 install tweepy
    sudo pip3 findspark
    ```

3. Open ```TwitterTagsDashboard.ipynb``` on Jupyter Notebook.
    ```
    jupyter notebook
    ```
    
4. Run the blocks until it says ```Run the TweetRead.py file at this point```.

5. Before running TweetRead.py, setup ```consumer_key```, ```consumer_secret```, ```access_token``` and ```access_secret``` (these can be found from step 1).

6. Now open another terminal and run TweetRead.py (this will start reading the tweets).
    ```
    python3 TweetRead.py
    ```
   Note: TweetRead.py is configured to filter tweets containing ```cricket```. You can change the filter criteria at ```twitter_stream.filter(track=['cricket'])```.
 
6. Run next blocks, before ```ssc.stop()```.

7. Now you can see real-time top tags from the tweet stream related to cricket in the seaborn bar.
