RGB_TOPIC="/zed_node/left/image_rect_color"
DEPTH_TOPIC="/zed_node/depth/depth_registered"
BAG_FILENAME="rosbags/depthandimage.bag"
RADAR_TOPIC="/ti_mmwave/radar_scan_pcl"
GPS_TOPIC="/fix"

rosbag record $RGB_TOPIC $RADAR_TOPIC $GPS_TOPIC -O rosbags/$(date +%H:%M:%S).bag
