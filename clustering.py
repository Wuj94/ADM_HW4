import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as matplt
from sklearn.preprocessing import StandardScaler


# Define K-Means class
class KM:
    
    def __init__(self, df):
        
        self.df = df
    
    # Define clustering function: it takes a dataframe and performs a K-Means clustering of its rows (i.e.
    # assigning a cluster to each row), and returns a group of clusters (a dictionary of lists)
    def clustering(self, n_clusters):
        
        self.n_clusters = n_clusters
        
        # Perform clustering
        kmeans = KMeans(n_clusters = self.n_clusters).fit(self.df)
        
        # Create clusters column in the dataframe
        self.df["cluster"] = kmeans.labels_
        
        # Initialize clusters dictionary
        clust_dict = dict()

        # Fill the dictionary with the clusters
        for i in range(len(self.df)):
            cluster = self.df["cluster"].iloc[i]
            if cluster not in clust_dict:
                clust_dict[cluster] = [i]
            else:
                clust_dict[cluster].append(i)
                
        # Return clusters dictionary
        return clust_dict
        
        
    # Define find_elbow function: it takes a dataframe, and performs K-Means clustering of its rows
    # with different values of k, plotting the sum of squared distances vs the number of clusters
    def find_elbow(self):
        
        ssd_dict = dict()

        for k in range(1, 10):
            kmeans = KMeans(n_clusters = k).fit(self.df)
            ssd_dict[k] = kmeans.inertia_
            
        matplt.figure()
        matplt.plot(list(ssd_dict.keys()), list(ssd_dict.values()))
        matplt.xlabel("Number of clusters")
        matplt.ylabel("Sum of squared distances")
        matplt.show()
        

# Define Jaccard Similarity class
class JS:
    
    def __init__(self, clust_dict1, clust_dict2):
        
        self.clust_dict1 = clust_dict1
        self.clust_dict2 = clust_dict2
        
    # Define __jaccard__ function: it takes two groups of clusters (two dictionaries of lists),
    # computes the Jaccard Similarity scores among them, and returns the similarity matrix
    def __jaccard__(clust_dict1, clust_dict2):
        
        # Initialize the similarity matrix, filling it with 0s
        sim_matrix = [[0 for i in range(len(clust_dict2))] for j in range(len(clust_dict1))]

        # Compute the Jaccard Similarity score for each pair of clusters in the clusters dictionaries
        for cl1 in clust_dict1:
            for cl2 in clust_dict2:
                intersection = set(clust_dict1[cl1]).intersection(set(clust_dict2[cl2]))
                n_int = len(intersection)
                union = set(clust_dict1[cl1]).union(set(clust_dict2[cl2]))
                n_uni = len(union)
                sim_matrix[cl1][cl2] = n_int/n_uni
                
        # Return similarity matrix
        return sim_matrix
        
    # Define find_top_3 function: it returns the 3 most similar pairs (tuples) of clusters in the two
    # different groups of clusters
    def find_top_3(self):
        
        # Compute the similarity matrix
        sim_matrix = JS.__jaccard__(self.clust_dict1, self.clust_dict2)
        
        # Initialize similarity list
        sim_list = list()

        # Fill the similarity list with all the scores in the similarity matrix
        for row in sim_matrix:
            sim_list = sim_list + [cl for cl in row]

        # Organize the similarity list in decreasing order
        sim_list = sorted(sim_list)[::-1]
        
        # Initialize list of top 3 couples of similar clusters
        top_3 = list()
        
        # Initialize lists of already chosen clusters (one for each group)
        chosen1 = list()
        chosen2 = list()

        # Fill it with the couples (tuples) of clusters corresponding to the top 3 similarity scores
        for k in range(len(sim_list)):
            for i in range(len(sim_matrix)):
                for j in range(len(sim_matrix[i])):
                    if (sim_list[k] == sim_matrix[i][j]) and (len(top_3) < 3):
                        if not (i in chosen1) and not (j in chosen2):
                            top_3.append((i, j))
                            chosen1.append(i)
                            chosen2.append(j)

        # Return top 3 pairs of clusters
        return top_3