# Dependencies
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
import pickle

# API definition
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

stop_words = list(stopwords.words('english'))

# Function for text processing
def text_process(text):
	"""
	removes punctuation
	removes the stop words

	"""
	nopunc = [char for char in text if char not in string.punctuation]
	return " ".join([word for word in nopunc if word.lower() not in stop_words])

def recommender(words):
    test_df= pd.DataFrame([words], columns=['text'])
    test_df['text'] = test_df['text'].apply(text_process)
    test_vectors = user_id_vectorizer.transform(test_df['text'])
    test_v_df = pd.DataFrame(test_vectors.toarray(), index=test_df.index, columns = user_id_vectorizer.get_feature_names())
    predictItemRating=pd.DataFrame(np.dot(test_v_df.loc[0],Q.T),index= Q.index,columns=['Rating'])
    topRecommendations=pd.DataFrame.sort_values(predictItemRating,['Rating'],ascending=[0])[:7]
    required = []
    for i in topRecommendations.index:
        temp = {}
        temp['name'] = df_business[df_business['business_id']==i]['name'].iloc[0]
        temp['categories'] = df_business[df_business['business_id']==i]['categories'].iloc[0]
        temp['rating'] = str(df_business[df_business['business_id']==i]['stars'].iloc[0])+ ' '+str(df_business[df_business['business_id']==i]['review_count'].iloc[0])
        required.append(temp)
    return required

@app.route('/<string:query>')
def predict(query):
    try:
        prediction = recommender(query)

        return jsonify({'recommendations': str(prediction)})

    except:

        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    df_business = pickle.load(open('model/recom_business.pkl', 'rb'))
    Q = pickle.load(open('model/recom_q.pkl', 'rb'))
    user_id_vectorizer = pickle.load(open('model/recom_user_id_vec.pkl', 'rb'))

    app.run(port=port, debug=True)
