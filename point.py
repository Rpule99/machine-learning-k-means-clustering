class Point:
    def __init__(self, point_id, point_x,point_y):
        self.point_id = point_id
        self.point_x = point_x
        self.point_y = point_y
        ###self.cluster_number = randomly assigned cluster

    def get_id(self):
        return self.point_id

    def get_point(self):
        return '{}{}{}'.format(self.point_x,',',self.point_y)

    ###def get_cluster(self):
       ### return self.cluster_number

    ###def set_clusterNo(self):