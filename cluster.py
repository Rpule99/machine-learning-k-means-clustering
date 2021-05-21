import numpy as np
class Cluster:
    def __init__(self, centroid_id, centroid_x, centroid_y):
        self.centroid_id = centroid_id
        self.centroid_x = centroid_x
        self.centroid_y = centroid_y

    def get_centroid_id(self):
        return self.centroid_id

    def get_centroid_pos(self):
        return '{}{}{}'.format(self.centroid_x, ',', self.centroid_y)

    def calculate_distance(self):
        print(np.sqrt(np.sum(x1-x2)**2))
        return np.sqrt(np.sum(x1-x2)**2)

    def update_centroid(self):
        return 1


