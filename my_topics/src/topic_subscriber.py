#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32 # Importing Int32 from std_msgs.msg

def callback(msg):  # callback for receiving messages
  print(msg.data)   # print to the Terminal when running

rospy.init_node('topic_subscriber') # initialize  topic_subscriber node

sub = rospy.Subscriber('counter', Int32, callback) 

rospy.spin() # wait for node to be shut down