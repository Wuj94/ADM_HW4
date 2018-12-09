## ADM_HW4
Repository for the 4th homework of the course ADM @ Sapienza University of Rome from group group #23 composed by Francisca Alliende, Giuseppe  Calabrese and Francesco Russo  

Incoming, a summary of the files of this repository. To access to a document just press the link in the name of the corresponding file.

### 1. **[Homework_4](https://github.com/Wuj94/ADM_HW4/blob/master/Homework_4.ipynb)**: 

### 2. First Part: Does basic house information reflect house's description?

#### **Functions**:

- **[scraper.py](https://github.com/Wuj94/ADM_HW4/blob/master/scraper.py):** class fu that takes from the site www.inmobiliare.it: title, link, price, locali, superficie, bagni, piano snd description, for # appartaments.  
- **[preprocessing.py](https://github.com/Wuj94/ADM_HW4/blob/master/preprocessing.py):** class that takes as an input, the raw data, and returns the data preprocessed. 
- **[matrixbuilder.py](https://github.com/Wuj94/ADM_HW4/blob/master/matrixbuilder.py):** class, that takes as an input, the preprocessed data, and return the information matrix and the desription matrix.
- **[clustering.py](https://github.com/Wuj94/ADM_HW4/blob/master/clustering.py):** thid file contains a class that preforms the K-Means clustering and a function that preforms the elbow method, that computes the desire numeber of clusters, and the Jaccard Similarity ì, useful for finding the most similar clusters between methods. 
- **[wordcloud.py](https://github.com/Wuj94/ADM_HW4/blob/master/wordcloud.py):** take as an input a list of indexes and a dataset, and returns a wordclous.
 
#### **Databases:**

- **[datasetindex.csv](https://raw.githubusercontent.com/Wuj94/ADM_HW4/master/datasetIndex.csv):** 
- **[datasetIndex_preprocessed.csv](https://github.com/Wuj94/ADM_HW4/blob/master/datasetIndex_preprocessed.csv):** 
- **[datastIndex_infmatrix.csv](https://github.com/Wuj94/ADM_HW4/blob/master/datastIndex_infmatrix.csv):** 
- **[datastIndex_infmatrix.csv](https://github.com/Wuj94/ADM_HW4/blob/master/datastIndex_infmatrix.csv):** 
- **datastIndex_tfidf.csv:**


### 3. Second Part: Find the duplicates!

#### **Functions**:

#### **Databases:**


