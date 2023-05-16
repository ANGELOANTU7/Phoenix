#!/usr/bin/env python

import rospy
import pcl
from sensor_msgs.msg import PointCloud2, Imu
from sensor_msgs.msg import PointField
import sensor_msgs.point_cloud2 as pc2
import numpy as np

def pointcloud_callback(data):
    # Convert PointCloud2 to numpy array
    pc_data = pc2.read_points(data, field_names=("x", "y", "z"), skip_nans=True)
    pc_np = np.array(list(pc_data))

    # Create a PCL point cloud object
    pc = pcl.PointCloud()
    pc.from_array(pc_np.astype(np.float32))

    # Process point cloud data using PCL
    # ...

def imu_callback(data):
    # Extract relevant IMU data
    orientation = data.orientation
    angular_velocity = data.angular_velocity
    linear_acceleration = data.linear_acceleration

    # Process IMU data
    # ...

def mapping_node():
    rospy.init_node('mapping_node')
    rospy.Subscriber('/zed2/point_cloud/cloud_registered', PointCloud2, pointcloud_callback)
    rospy.Subscriber('/zed2/imu/data', Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    mapping_node()

