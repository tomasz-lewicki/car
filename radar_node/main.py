import numpy as np
import json
from clustering import clusters
from matplotlib import pyplot as plt

import rospy
from std_msgs.msg import String
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2
from rospy.numpy_msg import numpy_msg

def callback_pointcloud(data):

    assert isinstance(data, PointCloud2)

    gen = point_cloud2.read_points(data)

    array = np.array(list(gen))

    cluster_dict = clusters(array)


    # for k, v in cluster_dict.items():
    #     print(type(v))

    pub.publish(json.dumps(cluster_dict))

    # print(cluster_dict['no_clusters'])
    # cluster_dict['centroids']
    # cluster_dict['masses']
    # cluster_dict['sizes']


if __name__ == '__main__':

    rospy.init_node('radar_pipeline', anonymous=True)

    rospy.Subscriber("/ti_mmwave/radar_scan_pcl", PointCloud2, callback_pointcloud)
    pub = rospy.Publisher("/radar_pipeline/clusters", String, queue_size=10)
    rospy.spin()

