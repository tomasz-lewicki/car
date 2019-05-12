import numpy as np
import json
import rospy

from std_msgs.msg import String

def callback_clusters(message):
    d = json.loads(message.data)

    print(np.array(d['centroids']))

if __name__ == '__main__':

    rospy.init_node('radar_camera_fusion', anonymous=True)

    rospy.Subscriber("/radar_pipeline/clusters", String, callback_clusters)

    rospy.spin()