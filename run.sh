#run roscore and then run the following instructions:
# (run in separate terminals because otherwise it's hard to catch errors)
roscore &
roslaunch zed_wrapper zed_camera.launch &
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyACM2 _baud:=115200 &
roslaunch ti_mmwave_rospkg 1642es2_short_range.launch

#for transform between radar and camera
#rosrun tf static_transform_publisher 0 0 0 0 0 0 ti_mmwave base_link 50
