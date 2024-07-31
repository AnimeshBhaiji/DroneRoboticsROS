#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
import numpy as np
import cv2

def callback(data):
    # Convert LaserScan data to a 2D image
    angle_min = data.angle_min
    angle_max = data.angle_max
    angle_increment = data.angle_increment
    ranges = np.array(data.ranges)

    # Replace 'inf' values with a maximum distance
    max_distance = data.range_max
    ranges[ranges == np.inf] = max_distance

    # Create a 2D array to visualize
    width = 360  # Width of the visualization image
    height = 360  # Height of the visualization image
    image = np.zeros((height, width), dtype=np.uint8)

    for i, r in enumerate(ranges):
        angle = angle_min + i * angle_increment
        x = int((r * np.cos(angle) + max_distance) / (2 * max_distance) * width)
        y = int((r * np.sin(angle) + max_distance) / (2 * max_distance) * height)
        if 0 <= x < width and 0 <= y < height:
            image[y, x] = 255

    # Show the image using OpenCV
    cv2.imshow("LIDAR Visualization", image)
    cv2.waitKey(1)  # Wait for a key press (1ms)

def listener():
    rospy.init_node('lidar_listener', anonymous=True)
    rospy.Subscriber('/laserscan', LaserScan, callback)
    rospy.loginfo("LIDAR listener node started. Waiting for data...")
    rospy.spin()

if __name__ == '__main__':
    listener()
    cv2.destroyAllWindows()

