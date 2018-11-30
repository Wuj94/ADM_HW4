import math
import numbers
from nltk.corpus import stopwords
import string
from nltk.stem.snowball import ItalianStemmer
import pandas as pd
import numpy as np


class Preprocesser:

    def __init__(self, df, text_field='description',unmodified_fields=['title', 'link']):
        self.df = df
        self.__field_name__ = text_field
        self.__unmodified_fields__ = unmodified_fields

    def preprocess(self):
        """Preprocess the description"""
        # drop rows with any na value
        self.df.dropna(inplace=True)

        # preprocess description
        descr = self.df[self.__field_name__].apply(Preprocesser.tokenize)
        descr = descr.apply(Preprocesser.remove_punctuation)
        descr = descr.apply(Preprocesser.remove_stopwords)
        descr = descr.apply(Preprocesser.stemming)
        self.df[self.__field_name__] = descr

        # make fields numeric
        self.__preprocess_numeric_fields__()

        self.df.dropna(inplace=True)
        return self.df

    def __preprocess_numeric_fields__(self):
        for field in self.df.columns:
            if field not in self.__unmodified_fields__ and field not in self.__field_name__:
                col = self.df[field].apply(self.__make_numeric__)
                self.df[field] = col

    def __make_numeric__(self, data):
        res = data
        if not isinstance(data, numbers.Number):
            res = res.replace('&nbsp', '')
            price = False
            if '€' in res:
                res = res.replace('€', '').replace('.', '')
                price = True
            if '11+' in res:
                return np.nan
            if '+' in res:
                res = res.replace('+', '')
            if 'T' in res:
                return 0
            if 'A' in res:
                return np.nan
            if 'R' in res:
                return 0.5
            if 'S' in res:
                return -1
            if '-' in res:
                split = res.split('-')
                low = float(split[0])
                hi = float(split[1])
                mid = (hi + low) / 2
                res = mid
                if not price:
                    res = math.floor(res)
        return res

    def remove_stopwords(data):
        """Remove stopwords"""
        stop_words = set(stopwords.words("italian"))
        filtered = []
        for word in data:
            if word not in stop_words:
                filtered.append(word)
        return filtered

    def remove_punctuation(data):
        """Remove punctuation"""
        remove_punct = str.maketrans('', '', string.punctuation + '“”–’')
        filtered = []
        for word in data:
            filtered.append(word.translate(remove_punct))
        return filtered

    def stemming(data):
        """Stemming"""
        stemmer = ItalianStemmer()
        filtered = []
        for word in data:
            filtered.append(stemmer.stem(word))
        return filtered

    def tokenize(data):
        """Tokenize a string"""
        return data.split()


df = pd.read_csv("/home/data/MScDS/ADM/ADM_HW4/immobiliare2.csv")
print('---preprocessing---')
p = Preprocesser(df)
p.preprocess()
df.to_csv("immobiliare2preprocessed.csv")
