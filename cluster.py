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
        # print(str(x1) + "," + str(x2))
        # print("Distance is " + str(np.sqrt(np.sum((x1-x2)**2)))
        # print(round(np.sqrt(np.sum([(13-7)**2, (8-4)**2])),2))
        return round(np.sqrt(np.sum([(x2-x1)**2, (y2-y1)**2])),2)

    def remove_point(self, point):
        if self.cluster_points.count(point) != 0:
            self.cluster_points.remove(point)

    def add_point(self, point):
        self.cluster_points.append(point)

    def update_centroid(self):
        x_sum = 0
        y_sum = 0
        for point in self.cluster_points:
            x_sum = x_sum + point.point_x
            y_sum = y_sum + point.point_y

        self.centroid_x = x_sum / len(self.cluster_points)
        self.centroid_y = y_sum / len(self.cluster_points)

        # print("Centroid " + str(self.centroid_id) + ": " + str(self.centroid_x) + ", " + str(self.centroid_y))
        return 1


