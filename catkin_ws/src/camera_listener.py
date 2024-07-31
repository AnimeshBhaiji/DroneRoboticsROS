#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

# Initialize global variables for drone control
linear_x = 0.0
linear_y = 0.0
linear_z = 0.0
angular_z = 0.0

def on_press(key):
    global linear_x, linear_y, linear_z, angular_z

    try:
        if key.char == 'w':
            linear_z = 1.0  # Increase altitude (takeoff)
        elif key.char == 's':
            linear_z = -1.0  # Decrease altitude (landing)
        elif key.char == 'a':
            linear_y = 1.0  # Move left
        elif key.char == 'd':
            linear_y = -1.0  # Move right
    except AttributeError:
        if key == keyboard.Key.up:
            linear_x = 1.0  # Move forward
        elif key == keyboard.Key.down:
            linear_x = -1.0  # Move backward
        elif key == keyboard.Key.left:
            angular_z = 1.0  # Rotate left (yaw)
        elif key == keyboard.Key.right:
            angular_z = -1.0  # Rotate right (yaw)

def on_release(key):
    global linear_x, linear_y, linear_z, angular_z

    try:
        if key.char in ['w', 's']:
            linear_z = 0.0
        elif key.char in ['a', 'd']:
            linear_y = 0.0
    except AttributeError:
        if key in [keyboard.Key.up, keyboard.Key.down]:
            linear_x = 0.0
        elif key in [keyboard.Key.left, keyboard.Key.right]:
            angular_z = 0.0

    if key == keyboard.Key.esc:
        # Stop listener
        return False

def control_drone():
    global linear_x, linear_y, linear_z, angular_z

    rospy.init_node('drone_keyboard_control', anonymous=True)
    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = linear_x
        twist.linear.y = linear_y
        twist.linear.z = linear_z
        twist.angular.z = angular_z
        cmd_vel_pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    # Start the keyboard listener in a separate thread
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    # Start controlling the drone
    try:
        control_drone()
    except rospy.ROSInterruptException:
        pass

    # Wait for the listener thread to finish
    listener.join()

