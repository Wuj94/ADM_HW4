from nltk.corpus import stopwords
import string
from nltk.stem.snowball import EnglishStemmer
import pandas as pd


class Preprocesser:

    def __init__(self, df, field_name='Description'):
        self.df = df
        self.__field_name__ = field_name

    def preprocess(self):
        descr = self.df[self.__field_name__].apply(Preprocesser.tokenize)
        descr = descr.apply(Preprocesser.remove_punctuation)
        descr = descr.apply(Preprocesser.remove_stopwords)
        descr = descr.apply(Preprocesser.stemming)
        self.df[self.__field_name__] = descr
        return self.df

    def remove_stopwords(data):
        """Remove stopwords"""
        stop_words = set(stopwords.words("english"))
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
        stemmer = EnglishStemmer()
        filtered = []
        for word in data:
            filtered.append(stemmer.stem(word))
        return filtered

    def tokenize(data):
        """Tokenize a string"""
        return data.split()

df = pd.DataFrame([[1,2,'Hi my name is preprocesser'],
                   [4,5,'It\'s better to test our code'],
                   [7,8,'My best friend might be a little bit crazy unconciousness']],
                  columns=['A', 'B', 'Description'])
print(df)
print('---preprocessing---')
p = Preprocesser(df)
p.preprocess()
print(df)
