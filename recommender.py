# import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
import string
import warnings
warnings.filterwarnings('ignore')


# load data
review_IL = pd.read_csv("Review_IL_restaurants.csv")
business_IL = pd.read_csv("Business_in_Illinois.csv")
data = review_IL[['business_id', 'user_id', 'stars', 'text']]


# creating a list of stop words
stop_words = list(stopwords.words('english'))


# Function for text processing
def text_process(text):
	""" 
	removes punctuation
	removes the stop words

	"""

	nopunc = [char for char in mess if char not in string.punctuation]
	return " ".join([word for word in nopunc if word.lower() not in stop_words])


# Applying text processing functions
data['text'] = data['text'].apply(text_process)


# Splitting the data into test and train data
X_train, X_test, y_train, y_test = train_test_split(review_IL['text'], review_IL['business_id'], test_size = 0.2)


# Creating tables of users and business
users_df = review_IL[['user_id','text']]
business_df = review_IL[['business_id', 'text']]


# Combining the reviews for each business id
business_df = business_df.groupby('business_id').agg({'text': ' '.join})


# Combining the reviews for each user id
users_id = users_df.groupby('user_id').agg({'text': ' '.join})



