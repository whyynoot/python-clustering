from file_worker import FileWorker
from clustering import Clustering
from painter import Painter

data_path = 'data.txt'

def main():
    file_worker = FileWorker(data_path)
    file_worker.get_points()


    clusterer = Clustering(file_worker.points)
    clusterer.cluster_all()

    painter = Painter()
    painter.paint(clusterer.cluster_dict, file_worker.points)

if __name__ == '__main__':
    main()
