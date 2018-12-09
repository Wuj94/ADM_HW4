
# Libraries
#main(['install', 'wordcloud']) # Install package wordcloud
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pip
import wordcloud
import nltk
from os import path
from PIL import Image
from pip._internal import main
from wordcloud import WordCloud

# Word Cloud Generator
def WordCloud_generator(df, L):
    """ inputs: a list with the indexes of the rows of the appartaments that belong to a cluster and 
    a dataframe that contains the description of the appartament
    output: a wordcloud (image)"""
    text = ""
    for index in L:
        text += df["description"][index] + " "
    wordcloud = WordCloud().generate(text)
    wordcloud = WordCloud(max_words=100, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()