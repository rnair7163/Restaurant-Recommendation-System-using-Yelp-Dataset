# Dependencies
from flask import Flask, request, jsonify
import traceback
import pandas as pd
import numpy as np
import string
from nltk.corpus import stopwords
import pickle
from flask_cors import CORS, cross_origin
import json
from scipy import sparse
from annoy import AnnoyIndex

# Your API definition
app = Flask(__name__)
CORS(app)

stop_words = list(stopwords.words('english'))

# Function for text processing
def text_process(text):
	"""
	removes punctuation
	removes the stop words

	"""
	nopunc = [char for char in text if char not in string.punctuation]
	return " ".join([word for word in nopunc if word.lower() not in stop_words])


# Function for new users
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
        temp['rating'] = df_business[df_business['business_id']==i]['stars'].iloc[0]
        required.append(temp)
    return required[:5]

# Function for existing users
def sample_recommender(user_id):
	n_users, n_items = train.shape
	known_positives = business['name'][train.tocsr()[user_id].indices]
	top_items = [business['name'][i] for i in u.get_nns_by_vector(np.append(user_embeddings[user_id], 0), 600)]
	s_required = []
	for x in top_items[:5]:
	    s_temp = {}
	    s_temp['name'] = x
	    s_temp['category'] = business[business.name == x]['category'].iloc[0]
	    s_temp['rating'] = business[business.name == x]['stars'].iloc[0]
	    s_required.append(s_temp)
	return s_required

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/<string:query>')
def predict(query):
    try:
        prediction = recommender(query)

        return jsonify(prediction);

    except:

        return jsonify({'trace': traceback.format_exc()})

@app.route('/user/<int:userid>')
def recommend(userid):
    try:
        recommend = sample_recommender(userid)

        return jsonify(recommend);

    except:

        return jsonify({'trace': traceback.format_exc()})

# Execution starts here
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 5000 # If you don't provide any port the port will be set to 12345

    # For new users
    df_business = pickle.load(open('model/recom_business.pkl', 'rb'))
    Q = pickle.load(open('model/recom_q.pkl', 'rb'))
    user_id_vectorizer = pickle.load(open('model/recom_user_id_vec.pkl', 'rb'))

    # For existing users
    business = pd.read_csv("business_model_2.csv")
    train = sparse.load_npz("model/train_2_model.npz")
    model = pickle.load(open('model/model_opt.pkl', 'rb'))
    _, user_embeddings = model.get_user_representations()

    f = 59
    u = AnnoyIndex(f)
    u.load('model/yelp_item_Annoy_member_idx.ann') # super fast, will just mmap the file

    # For running the api
    app.run(port=port, debug=True)
