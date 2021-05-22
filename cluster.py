import numpy as np
class Cluster:
    def __init__(self, centroid_id, centroid_x, centroid_y):
        self.centroid_id = centroid_id
        self.centroid_x = centroid_x
        self.centroid_y = centroid_y
        self.cluster_points = []

    def get_centroid_id(self):
        return self.centroid_id

    def get_centroid_pos(self):
        return '{}{}{}'.format(self.centroid_x, ',', self.centroid_y)

    def calculate_distance(self, point):
        x1 = point.point_x
        x2 = self.centroid_x
        y1 = point.point_y
        y2 = self.centroid_y
        print(str(x1) + "," + str(x2))
        print("Distance is " + str(np.sqrt(np.sum(x1-x2)**2)))
        return np.sqrt(np.sum(x1-x2)**2)

    def remove_point(self, point):
        coordinate = (point.point_x,point.point_y)
        if self.cluster_points.count(coordinate) != 0:
            self.cluster_points.remove(coordinate)
    def update_centroid(self):
        return 1


