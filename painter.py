import matplotlib.pyplot
import seaborn

class Painter(object):
    def get_colums(self, points):
        xy_array = []
        x_values = []
        y_values = []
        for i in range(len(points)):
            x_values.append(points[i][0])
            y_values.append(points[i][1])
        xy_array.append(x_values)
        xy_array.append(y_values)
        return xy_array

    def paint(self, cluster_dict, points):
        points = self.get_colums(points)
        palette = seaborn.color_palette(palette='tab20', as_cmap=True)
        matplotlib.pyplot.set_cmap(palette)
        for cluster in cluster_dict:
            new_plot = matplotlib.pyplot.subplot()
            new_plot.set_title(cluster)
            new_plot.scatter(points[0], points[1], s=6, c=cluster_dict[cluster].labels_)
            if cluster != "agglomerative_clustering" and cluster != "DBCSAN":
                centers_points = self.get_colums(cluster_dict[cluster].cluster_centers_)
                new_plot.scatter(centers_points[0], centers_points[1], s=6, c="black")
            matplotlib.pyplot.show()