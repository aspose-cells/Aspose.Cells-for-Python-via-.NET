import numpy as np
from sklearn.cluster import KMeans


class ClusteringAnalysis:

    @staticmethod
    def cluster(values, k=3):

        arr = np.array(values).reshape(-1, 1)

        model = KMeans(n_clusters=k, n_init=10)
        labels = model.fit_predict(arr)

        return labels.tolist()