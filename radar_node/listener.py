import numpy as np
from sklearn import cluster
from matplotlib import pyplot as plt
from math import sqrt

import rospy
from std_msgs.msg import String
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2
 
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/ti_mmwave/radar_scan_pcl", PointCloud2, callback_pointcloud)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

THR_DIST = 5

def callback_pointcloud(data):

    assert isinstance(data, PointCloud2)

    gen = point_cloud2.read_points(data)

    array = np.array(list(gen))

    print(array)

if __name__ == '__main__':
    listener()

