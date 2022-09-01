from sklearn.cluster import KMeans, DBSCAN, AffinityPropagation, MeanShift, AgglomerativeClustering



class Clustering(object):
    cluster_methods = ["kmeans", "affinity_propagation", "mean_shift", "agglomerative_clustering", "DBCSAN"]

    def __init__(self, points):
        self.clusters_numbers = 2
        self.points = points
        self.cluster_dict = {}

    def cluster_kmeans(self):
        kmeans = KMeans(n_clusters=self.clusters_numbers).fit(self.points)
        return kmeans

    def cluster_affinity_propagation(self):
        clustering = AffinityPropagation(damping=0.975, convergence_iter=5, preference=-890000000).fit(self.points)
        return clustering

    def cluster_mean_shift(self):
        clustering = MeanShift(bandwidth=50000, max_iter=50, bin_seeding=True).fit(self.points)
        return clustering

    def cluster_agglomerative_clustering(self):
        clustering = AgglomerativeClustering(n_clusters=self.clusters_numbers).fit(self.points)
        return clustering

    def cluster_DBCSAN(self):
        clustering = DBSCAN(eps=57000, min_samples=166).fit(self.points)
        return clustering

    def cluster_all(self):
        for method in self.cluster_methods:
            self.cluster_dict[method] = getattr(self, f"cluster_{method}")()


