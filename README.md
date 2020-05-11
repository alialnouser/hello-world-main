
# ROS package: |my_topics|

|Short introductory paragraph about your package. What does it do? Why is it useful?|
this package has a publisher/subscriber


## Requirements


This runs on ROS melodic installed on unbuntu 18.04

## Installation and configuration
First thing to do here is cd ~/ros_ws_01/src
then we do
catkin_create_pkg <package_name> <package_dependecies>
catkin_create_pkg my_topics rospy std_msgs message_runtime message generation.

Basically the package_name is the name of the package we want to create
and package_dependecies these are the names of other ROS pacages that our package depends on
now that we have created the package, we can add the dependecies
this packge (my_topics) contained:
doubler.py             topic_publisher.py
message_publisher.py   topic_subscriber.py
message_subscriber.py

we first do command as the following
touch <package_name> <package_dependecies>
touch my_topics/src/doubler.py
then to make sure it is excutable file
we do the following command
chmod u+x <package_name> <package_dependecies>
chmod u+x my_topics/src/doubler.py
and last to add the code to the file we open it with sublime
using the following command:
subl <package_name> <package_dependecies>
now we edit the package.xml to make sure it containes the required dependines 

## Getting started

|A short guide to using your package. Include important commands, etc.|

## Usage

|Usage information for key methods and commands.|


----------------------------------------------------------------------------------------------------------------------------------------



# ROS package: |my_services|

|Short introductory paragraph about your package. What does it do? Why is it useful?|


## Requirements

This runs on ROS melodic installed on unbuntu 18.04

## Installation and configuration

|Instructions for installation and configuration. Assume users know how to install ROS packages and can use `git`.|

## Getting started

|A short guide to using your package. Include important commands, etc.|

## Usage

|Usage information for key methods and commands.|


-----------------------------------------------------------------------------------------------------------------------------


# ROS package: |my_actions|

|Short introductory paragraph about your package. What does it do? Why is it useful?|


## Requirements

This runs on ROS melodic installed on unbuntu 18.04

## Installation and configuration

|Instructions for installation and configuration. Assume users know how to install ROS packages and can use `git`.|

## Getting started

|A short guide to using your package. Include important commands, etc.|

## Usage

|Usage information for key methods and commands.|
