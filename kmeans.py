import numpy as np

from point import Point
from cluster import Cluster
import random


class kMeans:
    def __init__(self, k = 3, point_map = {1: (2, 10),
                                            2: (2, 5),
                                            3:(8, 4),
                                            4: (5, 8),
                                            5: (7, 5),
                                            6: (6, 4),
                                            7: (1, 2),
                                            8: (4, 9)}
                 ):
        self.point_map = point_map
        # list of all our data points
        self.points_list = []
        # list of clusters
        self.cluster_list = []
        # this is a mapping for cluster_id to a list of points belonging to that cluster
        self.cluster_points = {}

    initial_clusters = [1, 4, 7]
    
    def generate_points_list(self):
        for example_number in range(1,len(self.point_map) + 1):
            x_coord = self.point_map[example_number][0]
            y_coord = self.point_map[example_number][1]
            initial_cluster = random.randint(0,2)
            point = Point(example_number, x_coord, y_coord, initial_cluster)
            self.points_list.append(point)

    def generate_clusters(self, initial_centroids=[1, 4, 7], no_of_clusters=3):
        for id in range(3):
            centroid_x = self.points_list[initial_centroids[id]-1].point_x
            centroid_y = self.points_list[initial_centroids[id] - 1].point_y

            cluster = Cluster(id, centroid_x, centroid_y)
            self.cluster_list.append(cluster)

            for point in self.points_list:
                if point.get_cluster() == id:
                    self.cluster_list[id].add_point(point)

    def find_closest_centroid(self,point):
        distances = [cluster.calculate_distance(point) for cluster in self.cluster_list]
        closest_centroid = np.argmin(distances)
        return closest_centroid

    def is_converged(self, old_centroids, current_centroids):
        distances = [current_centroids[i].convergence_distance(old_centroids[i]) for i in range(len(self.cluster_list))]
        return sum(distances) == 0

    def run_k_means(self):
        j = 1
        while j < 10:
            print("Iteration " + str(j))
            for i in range(len(self.cluster_list)):
                print(" Cluster " + str(i + 1) + ":", end=" ")
                for ids in self.cluster_list[i].cluster_points:
                    print(str(ids.point_id), end=",")
                print("")
                print("Centroid: " + "(" + str(round(self.cluster_list[i].centroid_x,2)) + ", " +
                      str(round(self.cluster_list[i].centroid_y,2)) + ")")

            old_centroids = []
            for cluster in self.cluster_list:
                cluster_pair = (cluster.centroid_x, cluster.centroid_y)
                old_centroids.append(cluster_pair)

            for point in self.points_list:
                closest_centroid = self.find_closest_centroid(point)
                current_cluster = point.cluster_number
                # once I have the id of the closest centroid, I need to update that point's associated cluster
                if closest_centroid != current_cluster:
                    self.cluster_list[current_cluster].remove_point(point)  # removes the point from its cluster
                    point.set_cluster_number(closest_centroid)  # update the point's centroid value
                    self.cluster_list[closest_centroid].add_point(point)
            for cent in self.cluster_list:
                cent.update_centroid()
                # check for convergence
            if self.is_converged(old_centroids, self.cluster_list):
                break
            j += 1

    def start_Kmeans(self):
        self.generate_points_list()
        self.generate_clusters()
        self.run_k_means()


class driverClass:
    def main():
        kmeans = kMeans()
        kmeans.start_Kmeans()
    if __name__ == "__main__":
        main()


