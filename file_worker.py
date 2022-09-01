
class FileWorker(object):
    def __init__(self, path_to_file) -> None:
        self.points = None
        self.file = path_to_file


    def get_points(self):
        try:
            f = open(self.file, 'r', encoding="Utf-8")
            points = []
            for line in f:
                points.append([int(line.split()[0]), int(line.split()[1])])

            # This was a test what if there will be a lot of points and how it will cluster it
            # U are able to uncomment this and see results

            # minimum = list(min(points, key = lambda t: t[1]))
            # maximum = list(max(points))
            # k = 100
            # delta_x = (maximum[0] - minimum[0])
            # delta_y = (maximum[1] - minimum[1])
            # for i in range(k):
            #     xi = (1 / k) * i
            #     iN = delta_x * xi + minimum[0]
            #     for j in range(k):
            #         yj = (1 / k) * j
            #         yN = delta_y * yj + minimum[1]
            #
            #         points.append([iN, yN])

            self.points = points
        except:
            raise Exception(f"Error with {self.file}")