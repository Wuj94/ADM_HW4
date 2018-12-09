import numpy as np
from collections import defaultdict


class Kmeans:

    def __sq_euclid_distance__(p1, p2):
        if len(p1) != len(p2):
            raise ValueError('p1 and p2 must be in the space')
        return ((p1-p2)**2).sum()

    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.clusters, self.centers = self.__kmeans__()

    def __compute_clusters__(self, centers):
        clusters = defaultdict(list)
        for i in range(len(self.data)):
            distances = []
            for j in range(len(centers)):
                distances.append(Kmeans.__sq_euclid_distance__(self.data[i], centers[j]))
            clusters[distances.index(min(distances))].append(i)
        return clusters

    def __compute_centers__(self, clusters):
        centers = np.zeros((len(clusters),len(self.data[0])))
        for i in clusters:
            centers[i] = np.mean(self.data[clusters[i]], axis=0)
        return centers

    def __kmeans__(self):
        centers = []
        clusters = dict()
        newcenters = self.data[np.random.choice(self.data.shape[0], self.k, replace=False)]
        while not np.array_equal(centers, newcenters):
            centers = newcenters
            clusters = self.__compute_clusters__(centers)
            newcenters = self.__compute_centers__(clusters)
        return clusters, newcenters


data = np.array([[1.5, 2.6], [2.8, 9.4], [4.5, 7.7], [5.3, 4.3]])
init_centers = np.array([[2.8, 9.4], [4.5, 7.7]])
k = Kmeans(data, 2)
print("---clusters----")
print(k.clusters)
print("---centers----")
print(k.centers)