#! /usr/bin/env python3
import rospy
rospy.init_node('hello_python')

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    print("Hello World")
    rate.sleep()
