#! /usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)
    print('dddd')

def First_Subscriber_Node():
    rospy.init_node('First_Subscriber_Node', anonymous = True)
    rospy.Subscriber('numbers',Int32,callback)
    rospy.spin()

    
if __name__ == '__main__':
    First_Subscriber_Node()
