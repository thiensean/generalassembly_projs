# Project 3 - Web scraping and Subreddit Classification


### Problem Statement

(MIB) is a secret association that keeps top secret information regarding extraterrestrials under wraps. Think "Area 51" and the "Roswell incident".
But, nothing is foolproof. Things get leaked out anyway.

Some information is leaked out into the internet via reddit, most of which are to "Aliens" and "Space" subreddits.

They do not want to completely shut down reddit, or delete the subreddit, Instead they would like to monitor what people are talking about.

The goal of the project is to use machine learning to accurately predict whether a post in "Space" or any other subreddit belongs to "Aliens".

Besides predicting its classification, they would also like to know what the latest trends are, not only to have an idea of what's hot, but to feed said information to their other departments such as their marketing effort on social media, events and even podcasts.

Future work are sentiment analysis and topic modelling and will allow MIB to further their understanding on what people are posting and ensuring effective monitoring.

### Stakeholders and why is it important to investigate
Men In Black (MIB) is a government association that researches & promotes extraterrestrial knowledge.

To fulfill their short term goals (this project):
1. Classify posts accurately to achieve the aim of collecting suitable posts for analysis
2. To get key words that the model classifier uses to accurately classify these posts to understand its method for its marketing and research efforts.

To fulfill their long term goals (future work):
1. Sentiment analysis of possible extraterrestrial on Earth to determine if its suitable to release information that might cause panic among citizens.
2. Understand how ordinary citizens think about extraterrestrial activities on Earth
3. Topic modelling to understand what topics ordinary citizens are discussing about Aliens to: 
    a. Market products 
    b. Push their agenda (whether its required to block or release sensitive information) 
    c. Whether public are getting closer to the truth about Aliens


## Executive Summary

Part 1:
1. Problem statement
2. Scope of project
3. Import relevant libraries
4. Web scraping through pushshift API and wrapper "pmaw", while considering server requests.
5. Scrape "Aliens" subreddit and "Space" subreddit.

Part 2:
1. Importing all necessary libraries
2. Importing scraped datasets "aliens_posts.csv" and "space_posts.csv"
3. Data Cleaning using libraries and custom functions
4. EDA
5. Feature Engineering
6. Visualization
7. NLP Preprocessing using NLTK and SpaCy
8. NLP classification modeling
9. Confusion Matrix
10. Accuracy, precision and F1 scoring
11. AUC/ROC curve
11. SHAP interpretation
12. Conclusion and recommendation
13. Future steps to move the project forward
14. Sources

readme.md:
1. Recommendations
2. Future steps forward for the project
3. Research about the topic
4. Sources


### Importing all necessary libraries

1. All libraries required for the project were imported

### Web scraping

### Data collection and storage was optimized through custom functions, pipelines, and/or automation:

Using a wrapper called "pmaw", this library can be used to automate post collection beyond its post limit and also allows useful parameters in consideration of the server receiving the requests.

### Thought given to the server receiving the requests such as considering number of requests per second

### By setting the following parameters:

#### "rate_limit=60, max_sleep=10"

Thought is given to the server receiving the requests by setting parameters such as rate limit and max sleep after every 100 posts, we do not flood the server with requests and our requests do not get rejected as possible DDoS attack on the server.

## Data Cleaning for Space and Aliens subreddit

### Framing data cleaning and EDA steps
### Handling missing data & cleaning

1. Keep "subreddit", "title", "selftext" in dataframes.

2. Missing values such as "[Removed]" or "[Deleted]" will be substituted with empty string and dropped.

3. Text will be converted to lower case

4. Non-ASCII characters will be substituted with empty strings

5. Punctuations will be removed

6. Reddit-specific markdown formatting will be substituted with empty strings

7. Links and URLs will be substituted with empty strings and removed

8. Duplicate rows will be identified and removed

9. Output descriptive statistics, distributions, identify and remove outliers

10. Append "Aliens" and "Space" dataframes


## Visualizations

## Identification of common words that are likely to appear in feature importance after modeling using visualization tools like word cloud.

#### Modelling results

Logistic Regression was used to classify our posts into the respective subreddits. Its algorithm allows mapping of the predicted values to probabilities through the use of a sigmoid function.

This allows the function to map the predicted value between 0 and 1.

Logistic regression has better interpretability and thus will be selected as production model.


#### Intepretation of results using SHAP - A game theory approach to model interpretation

Using a game theoretic approach to explain the output of the machine learning model for better interpretation.

Looking beyond just the surface level or just the coefficients of the model, we wanted to look at global interpretability and its local interpretability.
We used SHAP - a model explainer that uses a game theory approach to explaining the model in detail - which applies to tree based models too.

SHAP summary plot was used to display 3 important information:
1. Feature importance
2. Impact
3. Correlation

Global interpretability - It allows features to be interpreted on a global level, where we are able to see not only how the feature weighs on the model, but its:
Impact - determined by the X location on the scale.
Correlation - whether it has a positive/negative or a mix of both correlations on the model feature.

This greatly pushes our understanding of the model and allows us to understand the decision making process.


Source: https://github.com/slundberg/shap

Please refer to proj3_part2 for the plot of the model interpretation.

## SHAP summary plot - Logistic Regression

From the summary plot, we can conclude that the top words for classifying the model as "Aliens" were:

1. "aliens"
2. "believe"
3. "ufo"
4. "theory"
5. "disclosure"


From the summary plot, we can conclude that the top words for classifying the model as "Space" were:

1. "space"
2. "universe"
3. "mar"
4. "question"
5. "moon"

From the summary plot, we can conclude that there are a few words that might have caused the classification to be incorrect:

1. "alien" seems to have appeared in both aliens and space subreddits
2. "space" seems to have appeared in both aliens and space subreddits
3. "universe" is a close classification for both subreddits
4. "question" is a close classification for both subreddits


## Context to connect individual steps back to overall project

1. Outliers and short posts of less than 3 were removed as they often contained links and pictures.
2. Using both TFIDF and CVec, data was modeled using 4 different classification techniques: 
    a. MultinominalNB
    b. RandomForest Classifier
    c. CatboostClassifier 
    d. LogisticRegression 
3. As test dataset scores does not mean much for accuracy, confusion matrix were plotted for each model.
4. Accuracy, F1 scores became the focus point and benchmark for the models as they represent accurate classification
5. SHAP - using a game theoretic approach to explain the output of the selected production model was used as they have 2 important plots.
    a. Force plot - Represents the "force" each classification word contributed to the classification decision making process.
    b. Summary plot - Summarizes and shows how each word affected the decision making, and displays words that were close to boundaries of the decision making process.

#### Conclusions and Recommendations

The model conclusion were made based on: 
    1. Accuracy 
    2. Interpretability 
    3. Processing speed 
    
Among the models, the accuracy were fairly close representing close percentages within each other.

3 main scores for accuracy were considered:
1. Accuracy
2. Precision
3. F1 score

F1 score provides a balance between precision and recall and would be suitable for this application.

However, the randomforest and catboost traded off processing power and time to achieve a similar score as logisticregression.

Similarly, during model interpretation, randomforest took the longest time to run SHAP and likely needed a GPU to complete the step within a reasonable amount of time.

Hence, in terms of the 3 metrics defined above, logisticregression which did not have the best accuracy, had considerably better interpretability and processing speed which was important for future use.

Furthermore, its score was not far off from the best accuracy scoring model.

It can be concluded that LogisticRegression classification method was the most desirable among all the other models.

### Applying findings of research for benefit of stakeholders

For the benefit of stakeholders, there were a few words that the stakeholders needed to take note of as these words appeared to be very strong indicators of classification as can be seen from the SHAP model interpretation.

"Aliens", "Space", "Universe", "Telescopes", "ET"

These were strong predictors of the respective subreddits and hence should be taken note of for any future work.


#### Future Steps Forward

1. Sentiment Analysis
2. Topic modelling using BERT, Latent Dirichlet Allocation

Sentiment analysis helps our primary and secondary stakeholders by providing them with necessary information on how citizens think about Aliens and Space.

This will give MIB and media groups (secondary stakeholders) useful information of citizen's sentiments before they publish or market any information or products.

Topic modelling is another important area to look into as topic modelling is an unsupervised learning method to inform the primary and secondary stakeholders on the topics discussed through reddits.

By understanding the topics discussed, it gives MIB and media groups control and understanding over whether any undesirable topics were being discussed.

Being unsupervised, it allows the model to understand any changing topics discussed and allows MIB to take swift action if necessary.


#### Research Sources

Sources:

https://medium.com/@akankshamalhotra24/introduction-to-libraries-of-nlp-in-python-nltk-vs-spacy-42d7b2f128f2

https://christophm.github.io/interpretable-ml-book/shapley.html

https://proceedings.neurips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html

https://github.com/slundberg/shap