## ADM_HW4
Repository for the 4th homework of the course ADM @ Sapienza University of Rome from group group #23 composed by Francisca Alliende, Giuseppe  Calabrese and Francesco Russo  

Incoming, a summary of the files of this repository. To access to a document just press the link in the name of the corresponding file.

### **[Homework_4](https://github.com/Wuj94/ADM_HW4/blob/master/Homework_4.ipynb)**
Jupiter Notebook, with the code and coments of the entire homework

### First Part: Does basic house information reflect house's description?

#### **Functions**:

- **[scraper.py](https://github.com/Wuj94/ADM_HW4/blob/master/scraper.py):** functions related to the scraping process. 
- **[preprocessing.py](https://github.com/Wuj94/ADM_HW4/blob/master/preprocessing.py):** functions related to the preprocesing process.
- **[matrixbuilder.py](https://github.com/Wuj94/ADM_HW4/blob/master/matrixbuilder.py):** functions that build the information and the description matrices. 
- **[clustering.py](https://github.com/Wuj94/ADM_HW4/blob/master/clustering.py):** functions of k-means, Elbow Method and Jaccard Similarity. 
- **[wordcloudgenerator.py](https://github.com/Wuj94/ADM_HW4/blob/master/wordcloudgenerator.py):** wordcloud generator function. 
 
#### **Databases:**

- **[datasetindex.csv](https://raw.githubusercontent.com/Wuj94/ADM_HW4/master/datasetIndex.csv):** database with all the announcements after the scrapping process.
- **[datasetIndex_preprocessed.csv](https://github.com/Wuj94/ADM_HW4/blob/master/datasetIndex_preprocessed.csv):** database that contains the data from "datasetindex.csv", prepocessed.
- **[datastIndex_infmatrix.csv](https://github.com/Wuj94/ADM_HW4/blob/master/datastIndex_infmatrix.csv):** database with the informatrion matrix. Input for clusterization. 
- **datastIndex_tfidf.csv:** database, with the description matrix. Input for clusterization. Unfortunately not available due to its weight.

### Second Part: Find the duplicates!

#### **Functions**:



