# Youtube Comments Sentiment Analysis Project
## Overview
Welcome to my YouTube Sentiment Analysis Project! This project aims to delve into the fascinating 
realm of online interactions by exploring the relationship between sentiment in comments and the gender 
of content creators on YouTube. The primary focus of this analysis is to investigate whether there exists 
an observable disparity in how male and female creators are treated within the gaming community, as perceived 
through the sentiments expressed in the comments on their videos.

## Motivation
The motivation behind this project originates from the keen observation of the differential treatment 
experienced by men and women in the gaming community, both from the audience and fellow team members. 
This difference in treatment that is rooted in misogyny is a topic of discussion and concern within various online communities
By conducting sentiment analysis on YouTube comments, I aim to quantify and assess this perceived difference objectively.

## Methodology
### Data Collection
I first conducted some online research to get 14 popular male and female gamers. I look at ranking websites such as Social Blade and read various articles about
current most popular gamers that are still actively uploading gaming content. I used Youtube's API to extract comments and the date of the comment. I also obtained
total number of views, subscriber count, and number of videos for each YouTuber.

I created multiple smaller datasets to be then combined into a larger one with 20,500 data points.

### Preprocessing
I employed NLTK to preprocess the data, which involved tasks such as tokenization, removing punctuation, eliminating stop words, 
and standardizing capitalization. I also removed comments that were longer than 250 words and/or contained words that were
longer than 11 characters to filter out spam and bots. 

### Gender Classification
I manually classified the gender of each Youtuber based on the categories they appeared on in the ranking website and whether they are male or female-presenting.
However, I understand that gender classification by assumption is not a foolproof method and can lead to inaccuracies, biases, and ethical concerns.
I'm actively looking into alternative more ethical methods for this portion of this project, such as focusing solely on sentiment analysis without classifying gender, 
or incorporating self-reported gender data if available.

### Sentiment Analysis
Utilize sentiment analysis techniques (such as sentiment lexicons or machine learning models) to assess the sentiment expressed in the collected comments.
### Statistical Analysis
Analyze the sentiment scores and explore potential patterns using statistical methods.
### Visualization
Create visualizations (e.g., bar charts, scatter plots) to visually represent the relationship between creator gender and sentiment.
### Interpretation
Interpret the results to determine whether there is a noticeable difference in sentiment towards male and female creators.
