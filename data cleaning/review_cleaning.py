# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:05:37 2020

@author: Cheng Jiang
"""

import json
import pandas as pd

#since pd.readjson will cause memeory error, we read the file line by line
path = 'yelp_academic_dataset_review.json'
review = []
with open(path, encoding = 'utf-8') as fin:
    i = 0 
    for line in fin:
        line_contents = json.loads(line)
        review.append(line_contents)
        
review = pd.DataFrame(review)
review.shape

#WRITE THE REVIEW FILE INTO CSV FORMAT
review.to_csv("reviews.csv")


#GRAB THE REVIEWS FOR ILLINOIS ONLY
review = pd.read_csv('reviews.csv')
business = pd.read_csv('business.csv')

business_id_ls = business.business_id.unique()
review_idx = [i for i in range(review.shape[0]) if review.business_id[i] in business_id_ls]

review = review.iloc[review_idx,:]
review = review.drop(columns=['Unnamed: 0'])

review.index = range(review.shape[0])

yr_ls = [eval(x.split('-')[0]) for x in review.date]
review['year'] = yr_ls

#WRITE THE FILE INTO CSV FORMAT
review.to_csv('IL_review.csv')
























