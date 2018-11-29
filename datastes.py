
# coding: utf-8

# In[ ]:


# Libraries
import pandas as pd
import numpy as np
from collections import defaultdict
from math import log

# Information Matrix
def information_matrix(df):
    """ input: dataframe with all the information, pre-processed
    output: information matrix with dataframe format"""
    columns_of_interest = ["price", "locali", "superficie", "bagni", "piano"]
    return df[columns_of_interest]

# Description Matrix

# Sub-functions
def vocabulary(df):
    """input:dataframe with all the information, pre-processed
    output: a list with all the unique words of the descriptions"""
    voc_list = []
    for index in range(len(df)):
        for word in str(df.values[index][0]).split():
            if word not in voc_list:
                voc_list.append(word)
    return voc_list

def inv_freq(df):
    """input: dataframe with all the information, pre-processed
    output: a dictionary, with key: word; value: inverse document frequent of the word"""
    # A list with all the unique words of the dataframe
    voc_list = vocabulary(df)
    # Total numbers of documents
    Tot_num_docs = len(df)
    # Number of documents where the term appears(dictionary)
    num_doc_dict = defaultdict(int)
    i = 0
    for word in voc_list:
        for i in range(len(df)):
            if word in df.values[i][0].split():
                num_doc_dict[word] += 1
            i += 1
    # Inverse document frequency for each word
    inv_freq_dict = defaultdict(float)
    for word in voc_list:
        inv_freq_dict[word] = log((Tot_num_docs/num_doc_dict[word]),10)
    return inv_freq_dict

def frequency(L):
    """input: a list of words
    output: a dictionary, with key: word; value: frequency of that word in the list"""
    d_freq = defaultdict(int)
    for word in L:
        d_freq[word] += 1
    return d_freq

# Final function
def Tfidf(df):
    """input: dataframe with all the information, pre-processed
    output: a dictionary with key1: id_document(# row) value1: another dictionary
    with key2: the words in the document; value2: the tfidf of each word"""
    d = {}
    # Create a dictionary with all the words and the inverse document frequent of each word
    inv_freq_dict = inv_freq(df)
    # Create a frequency dictionary: as key1: id_doc; value1: dictionary
    # key2: word in document; value2: frequency of each word
    for i in list(df.index.values):
        L = str(df.values[i][0]).split()
        d[i] = frequency(L)
    # Create the final dictionary, with the tifidf of each word in each document 
    for i in range(len(df)):
        for key in d[i]:
            d[i][key] = d[i][key]*inv_freq_dict[key]
    return d

information_matrix = information_matrix(df)
description_matrix = Tfidf(df)

print(information_matrix)
print(description_matrix)

