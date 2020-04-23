# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:59:00 2020

@author: Cheng Jiang
"""

import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt

review = pd.read_csv("IL_review.csv", index_col= 0)

stopwords = set(STOPWORDS)
stopwords.add("place")
stopwords.add("one")

good_review = review[review.stars > 3.5]
text_g = " ".join(comments for comments in good_review.text)
mask_g = np.array(Image.open("up.jpg"))
wc_g = WordCloud(stopwords=stopwords,background_color="white",height=500, width=500, max_words=150, mask=mask_g).generate(text_g)
wc_g.to_file("goodReviw_WC.png")
plt.figure(figsize=[20,10])
plt.title("good reviews")
plt.imshow(wc_g, interpolation='bilinear')
plt.axis("off")
plt.show()


bad_review = review[review.stars < 2.5]
text_b = " ".join(comments for comments in bad_review.text)
mask_b = np.array(Image.open("down.png"))
wc_b = WordCloud(stopwords=stopwords,background_color="white",height=500, width=500, max_words=150, mask=mask_b).generate(text_b)
wc_b.to_file("badReviw_WC.png")
plt.figure(figsize=[20,10])
plt.title("bad reviews")
plt.imshow(wc_b, interpolation='bilinear')
plt.axis("off")
plt.show()