#!/usr/bin/env python

# the first line will ensure the interpreter used is the first one
# in your enviromnet's $PATH
# all python files start with this line, like the 1st line.
import rospy
# importing the rospy, that is a python library for ROS
from std_msgs.msg import Int32 # importing the standard IntInt32 
#from std_msgs.msg 

# setup: intialzing node with rospy, setting default name
rospy.init_node('topic_publisher')
pub = rospy.Publisher('counter' # register w/roscore, # topic name
  Int32, # topic type
  queue_size=5 # queue size
)
# start loop
rate = rospy.Rate(2) # adaptive rate in Hz

# Loop: publish, count, sleep
count = 0
while not rospy.is_shutdown(): # shut down by ctrl-c
    pub.publish(count) # publish count
    count += 1 # increment
    rate.sleep() # set by rospy.Rate above
    # end loop