import numpy as np
import rospy 
from sensor_msgs.msg import Image as ROS_Image
from rospy.numpy_msg import numpy_msg
import time
from PIL import Image as PIL_Image
import numpy as np

def vis_callback( data ):
    print(data.width)
    im = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, 4)
    # print(data.height)

    # # w, h = 512, 512
    # # data = np.zeros((h, w, 3), dtype=np.uint8)
    # # data[256, 256] = [255, 0, 0]
    print(im[:,:,0:2].shape)
    im = im[:,:,::-1]
    img = PIL_Image.fromarray(im[:,:,0:3], 'RGB')
    # #img.save('my.png')
    img.show()
    time.sleep(1)




if __name__ == '__main__':
    rospy.init_node('image_reader', anonymous=True)
    image_sub = rospy.Subscriber("/zed_node/left/image_rect_color", numpy_msg(ROS_Image), vis_callback)
    rospy.spin()