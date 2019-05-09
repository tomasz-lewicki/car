import numpy as np
from sklearn import cluster
from math import sqrt

import rospy
from sensor_msgs.msg import NavSatFix
 
class Speedometer:
    def __init__(self):
        self._prev_data = None
        self._current_data = None

    def feed(self, data):
        self._prev_data = self._current_data
        self._current_data = data

    def speed(self):
        if not self._prev_data or not self._current_data:
            return 0
        else: 
            return self._current_data.latitude - self._prev_data.latitude 

    def heading(self):
        pass

    def callback_gps(self, data):

        self.feed(data)
        print(self.speed())

    def listener(self):

        rospy.init_node('gps_node', anonymous=True)

        rospy.Subscriber("/fix", NavSatFix, self.callback_gps)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

if __name__ == '__main__':

    sp = Speedometer()

    sp.listener()

