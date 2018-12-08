# coding: utf-8
import pandas as pd 
df = pd.read_csv('/home/data/MScDS/ADM/ADM_HW4/datasetIndex_tfidf.csv')

# We remove the columns that have sum below the 25% percentile of the distribution of summed columns.    
counts = []
for i in range(len(df.columns)):
    counts.append(df.iloc[:, i].values.sum())
    
c = pd.Series(counts)
c.describe()

good_columns = c[c > c.describe()['25%']]
good_columns = list(good_columns.index)

df = df.iloc[:, good_columns]
