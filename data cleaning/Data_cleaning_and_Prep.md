# Data Cleaning and Data Preaparation
The purpose of this directory is to perform data cleaning.

## Business
Following are the ways in which we cleaned and prpared our Business dataset:
1. It was found that there are no duplicate entries, as there are no recurring business ids
2. There were few cities who were not counted as one though they were same. For example, St, Joseph was also recorded as Saint Joseph which was creating two different records though they were same.
3. Standardize the date format of hours variable
4. Businesses with open = 1 tag were only considered
5. Considered only Illinois-based restaurants in our dataset since we focussed on Illinois for building recommender system.
6. Out of 436 tags we decided to keep top 60 tags with highest popularities
7. We have incorporated the median income for each zip code from the secondary dataset 

## Users
1. Computed tenure for each user using start year of the user.
2. Computed TF-IDF for each tag which will be used as weights during model fitting

## Review
1. We cross checked the ‘review_count’ variable in the user dataset by aggregating the number of reviews given by each user from the review dataset
2. We found that there were cases where a unique user would rate one restaurant several times throughout his/her history. For such case, we only kept the most recent review since it reflected the user’s latest preference.
3. Removed user biases from the ratings provided by the user, we have standardized the users’ rating by subtracting their mean rating, and converting it to (-1,1). The reason why we did that transformation is that we wanted to focus more on ranking the user liked restaurants and disliked restaurants in the correct order, rather than predicting user ratings on each restaurant, which would result in high variance over time.
 





