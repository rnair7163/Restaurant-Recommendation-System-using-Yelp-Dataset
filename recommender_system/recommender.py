# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
import string
import pickle
import warnings
warnings.filterwarnings('ignore')


# load data
review_IL = pd.read_csv("Review_IL_restaurants.csv")
# business_IL = pd.read_csv("Business_in_Illinois.csv")
data = review_IL[['business_id', 'user_id', 'stars', 'text']]


# creating a list of stop words
stop_words = list(stopwords.words('english'))


# Function for text processing
def text_process(text):
	""" 
	removes punctuation
	removes the stop words

	"""

	nopunc = [char for char in text if char not in string.punctuation]
	return " ".join([word for word in nopunc if word.lower() not in stop_words])


# Applying text processing functions
data['text'] = data['text'].apply(text_process)


# Splitting the data into test and train data
X_train, X_test, y_train, y_test = train_test_split(review_IL['text'], review_IL['business_id'], test_size = 0.2)


# Creating tables of users and business
users_df = review_IL[['user_id','text']]
business_df = review_IL[['business_id', 'text']]


# Combining the reviews for each business id
business_id_df = business_df.groupby('business_id').agg({'text': ' '.join})


# Combining the reviews for each user id
user_id_df = users_df.groupby('user_id').agg({'text': ' '.join})

# Vectorizing the reviews
# user_id vectorizer
user_id_vectorizer = TfidfVectorizer(tokenizer = WordPunctTokenizer().tokenize, max_features = 5000)
user_id_vectors = user_id_vectorizer.fit_transform(user_id_df['text'])

# busniess_id vectorizer
business_id_vectorizer = TfidfVectorizer(tokenizer = WordPunctTokenizer().tokenize, max_features = 5000)
busniess_id_vectors = business_id_vectorizer.fit_transform(business_id_df['text'])

# Create a matrix with user_id and business_id as its rows and columns respectively
user_business_matrix = pd.pivot_table(data, values = 'stars', index = ['user_id'], columns = ['business_id'])
P = pd.DataFrame(user_id_vectors.toarray(), index = user_id_df.index, columns = user_id_vectorizer.get_feature_names())
Q = pd.DataFrame(busniess_id_vectors.toarray(), index = business_id_df.index, columns = business_id_vectorizer.get_feature_names())

# Matrix factorization
def matrix_factorization(R, P, Q, steps = 10, lamda = 0.02, gamma = 0.01):
	for step in range(steps):
		for i in R.index:
			for j in R.columns:
				if R.loc[i,j] > 0:
					eij = R.loc[i,j] - np.dot(P.loc[i] - Q.loc[j])
					P.loc[i] += gamma*(eij*Q.loc[j] - lamda*P.loc[i])
					Q.loc[j] += gamma*(eij - np.dot(P.loc[i] - lamda*Q.loc[j]))
		e = 0
		for i in R.index:
			for j in R.columns:
				if R.loc[i,j] > 0:
					e += pow(R.loc[i,j] - np.dot(P.loc, Q.loc[j]), 2) + lamda*(pow(np.linalg.norm(P.loc[i]), 2) + pow(np.linalg.norm(Q.loc[j]) ,2))
		if e < 0.001:
			break

	return P,Q

# run matrix factorization
P, Q = matrix_factorization(user_business_matrix, P, Q, steps=10, gamma=0.001,lamda=0.02)

# export model
output = open('recommender_model.pkl', 'wb')
pickle.dump(P,output)
pickle.dump(Q,output)
pickle.dump(userid_vectorizer,output)
output.close()



















