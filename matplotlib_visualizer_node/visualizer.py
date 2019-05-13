import time 
import jsonpickle
import numpy as np
from sklearn import cluster

from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib.cm as cm

import rospy
from std_msgs.msg import String
from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2
 
PC = None
CLUSTERS = None

def callback_pointcloud(msg):

    assert isinstance(msg, PointCloud2)

    gen = point_cloud2.read_points(msg)
    global PC
    PC = np.array(list(gen))

def callback_clusters(msg):
    global CLUSTERS
    CLUSTERS = jsonpickle.decode(msg.data)

if __name__ == '__main__':

    rospy.init_node('matplotlib_visualizer', anonymous=True)

    rospy.Subscriber("/ti_mmwave/radar_scan_pcl", PointCloud2, callback_pointcloud)
    rospy.Subscriber("/radar_pipeline/clusters", String, callback_clusters)

    fig, [ax1, ax2] = plt.subplots(1,2)

    while(True):
        ax1.clear()
        ax2.clear()
        ax1.set(xlim=[-20, 20], ylim=[0,20], xlabel='X [m]', ylabel='Y [m]', title='Raw Point Cloud')
        ax2.set(xlim=[-20, 20], ylim=[0,20], xlabel='X [m]', ylabel='Y [m]', title='Clusters')

        ax1.grid(which='major', alpha=0.5)
        ax2.grid(which='major', alpha=0.5)

        #Pre-inference
        Y = PC[:,0]
        X = PC[:,1]
        intensity = PC[:,3]
        ax1.scatter(X, Y, c=intensity, s=intensity)

        #Post-inference:
        centroids = CLUSTERS['centroids']
        sizes = CLUSTERS['sizes']
        clusters = CLUSTERS['clusters']
        sizesxy = CLUSTERS['sizesxy']

        for idx, c in enumerate(centroids):
            s = 6 * sizesxy[idx]
            width = s[1]
            height = s[0]
            print(height)
            rect = patches.Rectangle((c[0]-width/2, c[1]-height/2), width, height, linewidth=1,edgecolor='r',facecolor='none')
            ax2.add_patch(rect)


        colors = cm.rainbow(np.linspace(0, 1, len(clusters)))
        for idx, pc in enumerate(clusters):
            #print(idx)
            ax2.scatter(pc[:,0], pc[:,1], c=colors[idx], s=pc[:,2])

        plt.show(block=False)
        plt.pause(.001)
        

