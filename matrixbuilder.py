import pandas as pd
import numpy as np
from collections import defaultdict
from math import log


class MatrixBuilder:

    def __init__(self, df, ):
        self.df = df

    def information_matrix(self, columns_of_interest=["price", "locali", "superficie", "bagni", "piano"]):
        """ information matrix creator
        input: dataframe with all the information, pre-processed
        output format: dataframe"""
        return self.df[columns_of_interest]

    def __vocabulary__(self, column_name='description'):
        """input:dataframe with all the information, pre-processed
        output: a list with all the unique words of the descriptions"""
        voc_list = set()
        for index in range(len(self.df)):
            for word in str(self.df.loc[index, column_name]).split():
                voc_list.add(word)
        return list(voc_list)

    def __inv_freq__(self, column_name='description'):
        """input: dataframe with all the information, pre-processed
        output: a dictionary, with key: word; value: inverse document frequent of the word"""
        # A list with all the unique words of the dataframe
        voc_list = self.__vocabulary__()
        # Total numbers of documents
        Tot_num_docs = len(self.df)
        # Number of documents where the term appears(dictionary)
        num_doc_dict = defaultdict(int)
        for word in voc_list:
            for i in range(len(self.df)):
                if word in self.df.loc[i, column_name].split():
                    num_doc_dict[word] += 1
                i += 1
        # Inverse document frequency for each word
        inv_freq_dict = defaultdict(float)
        for word in voc_list:
            inv_freq_dict[word] = log((Tot_num_docs / num_doc_dict[word]), 10)
        return inv_freq_dict

    def __frequency__(L):
        """input: a list of words
        output: a dictionary, with key: word; value: frequency of that word in the list"""
        d_freq = defaultdict(int)
        for word in L:
            d_freq[word] += 1
        for key in d_freq:
            d_freq[key] = d_freq[key] / len(L)
        return d_freq

    def Tfidf(self, column_name='description'):
        """input: dataframe with all the information, pre-processed
        output: a dictionary with key1: id_document(# row) value1: another dictionary
        with key2: the words in the document; value2: the tfidf of each word"""
        d = {}
        # Create a dictionary with all the words and the inverse document frequent of each word
        inv_freq_dict = self.__inv_freq__()
        # Create a frequency dictionary: as key1: id_doc; value1: dictionary
        # key2: word in document; value2: frequency of each word
        for i in range(len(self.df)):
            L = str(self.df.loc[i, column_name]).split()
            d[i] = MatrixBuilder.__frequency__(L)
        # Create the final dictionary, with the tifidf of each word in each document
        for i in range(len(self.df)):
            for key in d[i]:
                d[i][key] = d[i][key] * inv_freq_dict[key]
        D = pd.DataFrame(d).T
        D.fillna(value=0, inplace=True)
        return D


df = pd.read_csv("immobiliare2preprocessed.csv")
mb = MatrixBuilder(df)
mb.information_matrix().to_csv('inf_matrix.csv')
mb.Tfidf().to_csv('tfidf_matrix.csv')