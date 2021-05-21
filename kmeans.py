from point import Point
from cluster import Cluster
import random

class kmeans:
    ### list of all our data points
    global point_map
    point_map = {
        1:(2,10),
        2:(2,5),
        3:(8,4),
        4:(5,8),
        5:(7,5),
        6:(6,4),
        7:(1,2),
        8:(4,9)
    }
    global points_list
    points_list = []
    ### list of clusters
    global cluster_list
    cluster_list = []
    ### this is a mapping for cluster_id to a list of points belonging to that cluster
    global cluster_points
    cluster_points = {}

    initial_clusters = [1,4,7]
    
    def generate_points_list():
        for example_number in range(1,len(point_map) + 1):
            x_coord = point_map[example_number][0]
            y_coord = point_map[example_number][1]
            initial_cluster = random.randint(0,3)
            point = Point(example_number,x_coord,y_coord,initial_cluster)
           ### print(initial_cluster)
            points_list.append(point)

    def generate_clusters(initial_centroids = [1,4,7], no_of_clusters = 3):
        for id in range (3):
            centroid_x = points_list[initial_centroids[id]-1].point_x
            centroid_y = points_list[initial_centroids[id] - 1].point_y

            cluster = Cluster(no_of_clusters,centroid_x,centroid_y)
            cluster_list.append(cluster)

    def main():
            print("Testing")
    if __name__ == "__main__":
        generate_points_list()
        generate_clusters()
        main()

