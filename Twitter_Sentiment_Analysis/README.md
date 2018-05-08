
# News Analysis

The purpose of this project was to learn about the general sentiment of the news published by various news organizations. Twitter's API was used to pulldown tweets from BBC World, CBS, CNN, Fox News, and the New York Times. The senitments of the tweets were then analyzed using [vaderSentiment][1], a natural language processing library for determining the posivity and negativty contained in sentences. This library is attuned for text published on social media.

[1]: https://github.com/cjhutto/vaderSentiment#features-and-updates

![alt text](https://www.worldatlas.com/r/w728-h425-c728x425/upload/dd/36/4f/shutterstock-415584550.jpg)

### Data
The data was collected on 3/23/2018 and consists of the last 100 tweets posted by the above-mentioned news organizations. Since news organziations tweet often, the data set contains tweets from about three days in March.

Here is an example of a couple of tweets from BBC World:

    "Half of African species 'face extinction' https://t.co/EndEdlKO9r"
    
    "Elon Musk pulls brands from Facebook https://t.co/4BxPvragQf![image.png](attachment:image.png)"
    


### Analysis 

All of the tweets were run through the SentimentIntensityAnalyzer function. The function breaks down what percentage of the tweet is positive, neutral, and negative. In addition, the function returns an overall sentiment score on a scale of -1.0 to 1.0. Scores less than -0.5 are negative, scores between -0.5 and 0.5 are neutral, and scores greater than 0.5 are positive. 

Here is an example of a tweet with its vaderSentiment scores:

Tweet: "RT @BullCBS: The verdict is in...#Bull is the perfect Valentine! ‚Happy #ValentinesDay! https://t.co/poEejI4AnC"

Results: Negative: 0, Neutral: 0.534. Positive: 0.466, Overall: 0.8619

We can get an understanding here of how the function works. The function detected no negativity because there were no obviously negative words. About half of the tweet was determined to be neutral and the other half was said to be positive because there is a lot of text in the tweet that is neutral, such as "The verdict is in", and there is also positivity with the words "perfect" and "Happy".


The vaderSentiment analyzer is far from perfect. Take a look at this tweet about tariffs.


Tweet: "BREAKING: China plans to slap tariffs on $3 billion worth of US products ranging from pork to steel pipes"

Results: Negative: 0, Neutral: 0.851, Positive:	0.149, Overall: 0.3612

Someone might feel that the tone of this tweet is negative because the word "slap" can mean to punish someone with something. The sentiment analyzer guessed, however, that the tweet was neutral. The sentiment analyzer also detected some positivity even though it is not clear what is positive in this tweet.

This method of analyzing sentiment is clearly flawed but it does have some success at determining the sentiment of text.

### Graphs

To get an idea of the distribution of tweet sentiments for the various news groups, I plotted the overall sentiment of the tweets on the y-axis, how many tweets ago a tweet was posted on the x-axis, and color-coded the tweets based on who posted them.

![png](https://github.com/amatthi55/Portfolio/blob/master/Twitter_Sentiment_Analysis/Graphs/Individual%20Tweet%20Analysis.png) 

One observation is that many of the tweets are considered completely neutral, which is understandable because many news organization typically try to refrain from expressing an opinion in a headline. Another observation is that CBS is the one group to tweet mainly positive content. The other organization's tweets are evenly divided between positive and negative.


To have a clearer idea of how an organization's tweet sentiment compared with one another, I created a bar chart showing the average for each organization's overall sentiment scores.

![png](https://github.com/amatthi55/Portfolio/blob/master/Twitter_Sentiment_Analysis/Graphs/Overall%20Sentiment%20Analysis.png)

We can see that CBS clearly has the most positive sentiments overall and that the rest of the news organziations have a net senitment score closer to zero. This indicates that the amount of positivty and negativty for each of these organziations is fairly balanced. These organization also have a negative average sentiment score.

While the above graphs can give us an idea of how a news group's positivity compares with its negativity, it does not show how extreme their sentiments are. This next graph is a bar chart showing the sum of the squares of each group's overall senitment scores. The taller bar graphs belong to the companies that express the most extreme sentiments.


![png](Graphs/Overall Sentiment Analysis_SS.png)


CBS expressed the most extreme sentiments over this time period, followed by the New York Times, and Fox News.


### Observations
It is clear that this method for analyzing sentiment can be very innaccurate. If we trust the accuracy of the sentiment analyzer, then our data suggests that CBS expresses more positivity than the other news organizations. The data also indicates that CBS, NYT, and Fox News express more of an opionion in their tweets than BBC and CNN do.

We can find interesting insights in the data even if this senitment analyzer cannot guess sentiment well. CBS has a dramatically more positive score than the other news organizations. This may not mean that CBS's tweets are far more positive than other news tweets but, knowing what we know about vaderSentiment, we are fairly certain that they use far fewer words with generally negative connotations and far more words with generally positive connotations. CBS's greater use of positive concepts may just be a result of this news cycle or it may be a deliberate choice by their newsroom.

