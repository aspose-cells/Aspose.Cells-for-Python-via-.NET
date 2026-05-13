from sklearn.decomposition import PCA
import pandas as pd

class PCAAnalysis:

    @staticmethod
    def analyze(df):

        numeric = df.select_dtypes(include=['number'])

        pca = PCA(n_components=2)

        components = pca.fit_transform(numeric)

        return {
            "explained_variance": pca.explained_variance_ratio_.tolist(),
            "components": components.tolist()
        }