# mercedes-clk-perception

## 1. Install ROS melodic:
Instructions are available at:
http://wiki.ros.org/melodic/Installation/Ubuntu

## 2. install dependencies:
```bash
pip3 install -r requirements.txt
```
Most of the packages are already provided with ROS. Virutal environment is preferable.

## 3. Download rosbags:


## 4. Run nodes:
```bash
python3 fusion_node/main.py
python3 gps_node/main.py
python3 radar_node/main.py
python3 2d_detection_node/main.py #(additional instructions in 2d_detection_node/README.md)
```

## 5. Play rosbag:
```bash
rosbag play 720loop1.bag
```

## 6. Check if nodes are working:
If everything worked out successfully
```bash
$ rostopic list
```
Should give the following output:
```
/2d_node/results
/clicked_point
/clock
/fix
/fusion/results
/gps_node/heading
/gps_node/speed
/initialpose
/move_base_simple/goal
/mrcnn/output_image
/radar_pipeline/clusters
/rosout
/rosout_agg
/tf
/tf_static
/ti_mmwave/radar_scan_pcl
/zed_node/left/image_rect_color
```