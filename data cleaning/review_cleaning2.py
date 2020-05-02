# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:05:37 2020

@author: Cheng Jiang
"""
import pandas as pd

data_review = pd.read_csv('D:/yelp/IL_review.csv',index_col=0)
data_review.head(3)

#USERS' FREQUENCIES
data_review.groupby('user_id').count()['business_id'].describe()

# Load data
data_business = pd.read_csv('D:/yelp/business_cj.csv',index_col=0)
data_users = pd.read_csv('D:/yelp/IL_users.csv',index_col=0)

# create user tag by merging
user_tag = data_review.merge(data_business, left_on='business_id', right_on='business_id')
user_tag.columns

# creating a group by
user_tag2 = user_tag.groupby('user_id').sum().iloc[:,12:]
user_tag2.shape

# creating tags
tag = []
for i in range(user_tag2.shape[0]):
    tmp = user_tag2.iloc[i,:].sort_values(ascending=False)[:2].index.tolist()
    tag.extend(tmp)

#len(set(tag))

tag_all = user_tag2.idxmax(axis=1)
tag_list = list(set(tag_all))
tag_all_df = pd.DataFrame(tag_all).reset_index()

# updating tags

for tag in tag_list:
    data_users[tag] = 0

for ind,val in enumerate(tag_all):
    row = list(data_users['user_id']).index(tag_all_df['user_id'][ind])
    data_users.loc[row,val] = 1
    
data_users.iloc[:,24:].describe()

# creating outfile
data_users.to_csv("D:/yelp/uers_tag.csv")