# Project 2 - Ames Housing Data and Kaggle Challenge


### Problem Statement

As real estate analysts in Iowa, we are responsible for managing our organization's real estate holdings.
We are tasked with understanding real estate market trends and to minimize current and future real estate holding risks.

We will be conducting data analysis on the Iowa real estate market and determine which are the factors that affects property prices.
The purpose of this analysis is to better understand a property price and provide suitable insights to management and potential buyers of the organization's real estate.


## Executive Summary

Part 1:
1. Importing all necessary libraries
2. Importing training dataset "train.csv".
3. Data Cleaning
4. EDA

Part 2:
1. Importing all necessary libraries
2. Importing training dataset "test.csv".
3. Data Cleaning
4. EDA

Part 3:
1. Feature Engineering
2. Modelling, L1 & L2 regularization
3. Residuals and model evaluation
4. Results interpretation

readme.md:
1. Recommendations
2. Future steps forward for the project
3. Research about the topic
4. Sources

### Kaggle Score

'./images/kagglescore.png'


### Importing all necessary libraries

1. All libraries required for the project were imported


### Importing datasets

1. Datasets "train.csv" and "test.csv" were imported for data cleaning

Relative path:
'./datasets/train.csv'
'./datasets/test.csv'


#### Data Cleaning and EDA

1. Null values in the datasets were explored and upon determining that those belongs to categories where it means that it "does not exist" instead of "missing data", those null values were changed to "NA".
2. Outliers were checked and corrected.
3. Checking and correcting datatypes
4. "others" that are "int64" dtype were replaced with -1.0
5. Ordinal data was replaced with rankings in 0-5
6. Categorical data was converted using one hot encoding.
7. Data distributions were shown using seaborn
8. Pearson and Spearman's correlation for each feature were feature engineered
9. Each high correlation data was visualized with seaborn.
10. Low correlation features with low predictive capabilities were dropped to reduce noise to the model


#### Data Dictionary can be found here (as all the columns remained the same, the same data dictionary can be used):

http://jse.amstat.org/v19n3/decock/DataDocumentation.txt).


#### Modelling results

The modelling coefficients path can be found as follows:

Relative path:
'./datasets/model_coeff.csv'

Submission CSV is as follows:
'./datasets/submission.csv'


#### Intepretation of results

From the correlation coefficients as well as the model's coefficients, we can infer that quality and floor area was the 2 major factors directly affecting the property price.
Other house features like basement quality and external quality played a part in the property prices too.


##### Model's coefficients

	features	        coefficients
Neighborhood_StoneBr	36336.554746
Neighborhood_NridgHt	28447.210792
Neighborhood_NoRidge	21005.676492
Lot Area_log	        15283.131206
Sale Type_New	        13847.031460

Bldg Type_Duplex	    -7924.577496
Exterior 1st_Wd Sdng	-8296.185377
Bldg Type_Twnhs	        -10500.026765
Neighborhood_Edwards    -10924.042557
Bldg Type_TwnhsE	    -12278.910995


##### Correlation

	feature	            corr
Overall Qual	        0.806923
Gr Liv Area	            0.727025
smt Qual_ord	        0.698305
Exter Qual_ord	        0.696716

MS Zoning_RM	        -0.362435
Foundation_CBlock	    -0.377445
Mas Vnr Type_None	    -0.432921
Garage Type_Detchd	    -0.451841
Garage Finish_Unf	    -0.498263


#### Business Recommendations

Hence, as real estate analysts working for a private organization it is important that the organization understands what is a good strategy for the company to turn a profit.
By understanding the negative coefficients it is possible to purchase and flip houses for a profit by turning the negatives into positives.

By making use of the model, it is also a good strategy to allow the organization to gain a better understanding on how to maintain the property value and resale value.
Proper maintenance schedules can be drawn up to maintain the property periodically as the quality was a major factor in affecting the property prices.


#### Future Steps Forward

To compare the results with other states in the country to determine if the housing features determined in this study affects other states in a similar fashion too.
This could potentially determine the buyer's purchase decision as well as the developer's decision to achieve a better price for the house.

1. Comparing correlations to other states
2. Finding the features with the highest coefficients on a national level
3. Understanding shifting trends over the years
4. Explore the next rising feature that would affect property the most
5. Looking for features that can be turned from negative to positive (potential profit area of interest)


#### Research

1. Local market conditions, interest rates also affects property prices to a certain extent hence invalidating some of the features analysis unless this project involves more historical data.
2. Adding pools might affect property prices for expensive houses more than for lower or mid tier house; features are dependent on the original house value.
3. Design can affect the property prices and is dependent on the local state's taste for design.


#### Research Sources

https://www.investopedia.com/articles/mortages-real-estate/11/factors-affecting-real-estate-market.asp
https://www.newrez.com/blog/home-buying-selling/5-things-that-influence-home-prices-in-2021/
https://www.investopedia.com/articles/mortages-real-estate/11/the-truth-about-the-real-estate-market.asp
https://www.whitehouse.gov/cea/written-materials/2021/09/09/housing-prices-and-inflation/
https://www.americanactionforum.org/insight/understanding-the-national-increase-in-house-prices/
https://www.opendoor.com/w/blog/factors-that-influence-home-value