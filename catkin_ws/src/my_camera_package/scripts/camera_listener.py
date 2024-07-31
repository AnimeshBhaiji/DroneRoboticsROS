#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def image_callback(msg):
    # Create a CvBridge object
    bridge = CvBridge()

    try:
        # Convert ROS Image message to OpenCV image
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        rospy.loginfo("Received image data")
    except CvBridgeError as e:
        rospy.logerr("CvBridgeError: {0}".format(e))

def main():
    # Initialize the ROS node
    rospy.init_node('camera_listener', anonymous=True)

    # Subscribe to the camera image topic
    image_topic = '/camera/image_raw'  # Change this to your actual camera topic
    rospy.Subscriber(image_topic, Image, image_callback)

    # Keep the node running
    rospy.loginfo("Camera listener started, waiting for images...")
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

