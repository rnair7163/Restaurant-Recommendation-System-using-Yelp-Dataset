## Restaurant-Recommendation-System-using-Yelp-Dataset
This is our academic project for CSP-571 "Data Preparation And Analysis". 
In this project we built a personalized recommender web app using Yelp dataset of restaurants. We tested various models like Pure Collaborative, Approximate Nearest Neighbour, K-NN, Naive Bayes and Hybrid Maxtrix Factorization on various hyperparameters which were tuned using the library "scikit optimizer"
We tested the models using AUC which is a decision-support metric that checks whether customers like the item or not. In our case, figuring out customer preference in general is more important and practical. 
And for deployment, we used Angular8 and Flask frameworks.

### Datasets:- 
#### Primary Dataset
The primary dataset for our model was [Yelp dataset](https://www.yelp.com/dataset). From that, we used 3 datasets namely business.json, reviews.json and users.json. 

#### Secondary Dataset
The Secondary dataset for our model was [median income for each postal code](https://www.census.gov/) which was then mapped to businesses.

### Data Cleaning and Data Preaparation
#### Business
Following are the ways in which we cleaned and prepared our Business dataset:

1. It was found that there are no duplicate entries, as there are no recurring business ids
2.There were few cities who were not counted as one though they were same. For example, St, Joseph was also recorded as Saint Joseph which was creating two different records though they were same.
3. Standardize the date format of hours variable
4. Businesses with open = 1 tag were only considered
5. Considered only Illinois-based restaurants in our dataset since we focussed on Illinois for building recommender system.
6. Out of 436 tags we decided to keep top 60 tags with highest popularities
7. We have incorporated the median income for each zip code from the secondary dataset

#### Users
1. Computed tenure for each user using start year of the user.
2. Computed TF-IDF for each tag which will be used as weights during model fitting

#### Review
1. We cross checked the ‘review_count’ variable in the user dataset by aggregating the number of reviews given by each user from the review dataset
2. We found that there were cases where a unique user would rate one restaurant several times throughout his/her history. For such case, we only kept the most recent review since it reflected the user’s latest preference.
3. Removed user biases from the ratings provided by the user, we have standardized the users’ rating by subtracting their mean rating, and converting it to (-1,1). The reason why we did that transformation is that we wanted to focus more on ranking the user liked restaurants and disliked restaurants in the correct order, rather than predicting user ratings on each restaurant, which would result in high variance over time.

### Exploratory Data Analysis 
#### Business
1. Business dataset contains geographical information about 192,609 businesses, categories and attributes, such as average star rating, hours, whether they offer parking etc.
2. It majorly consists of Business from North America.
3. The yelp business dataset consists of variety of different businesses indicated by the column ‘attributes’. Number of entries for the category ‘Restaurants’ was the highest.

#### Users
1. Dataset user includes information like how long ago the user has joined Yelp, the number of reviews he/she has written, the number of specific compliments received, and his/her friend mapping on Yelp about 1,637,138 users.
2. There are outliers observed in the value of review_count in the user's dataset. 

#### Review
1. We have performed sentiment analysis on the review dataset text. People seem to be more likely to write a review for a positive experience than a negative one
2. Most of the users have given more positive ratings to the restaurants.


### Contributors:-
1. [Cheng Jiang](https://github.com/okcheng0504mm)
2. [Kausar Perveen](https://github.com/kperveen)
3. [Rahul Nair](https://github.com/rahulmnair1997)
4. [Shouvik Sharma](https://github.com/shouvik19)
5. [Sohan Puthran](https://github.com/sohansputhran)
