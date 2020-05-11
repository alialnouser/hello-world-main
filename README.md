
# ROS package: |my_topics|

|First communicaton mechanism in ROS|
this package has a publisher/subscriber for topic and message and a doubler , first one is topic_publisher
explaining the while loop for topic_publisher:
it publsihers the count to topic 'counter' through the publish method of the object pub made by rospy.Publisher, then increment the count, and finally wait till the sleep method says to iterate. rate has sleep method sleep to keep the loop running at chosen rate. Next, topic_subscriber this subscribes topics with rospy by defining a callback function which is called upon the arrival of every new message. And registering the subscription with roscore. message subscriber prints real and imaginary parts. doubler.py node subscribes to topic number, multiplies the received msg.data Int32 by 2, and it publishes the results doubled to topic. This is useful to create sort of comunication between real live and robots works as source guidence for the machine. 


## Requirements

This runs on ROS melodic installed on unbuntu 18.04.

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
now we edit the package.xml to make sure it containes the required dependecies.
using  git -A, then git commit -m , and git push to make sure it's updated. this send the work to github raspratory hello-world-main.

## Getting started

catkin_make to make our package available to be executable.
then,
source devel/setup.bash , this is to source the workspace
now open a new terminal and start 'roscore' service
we can run our node
rosrun my_topics topic_publisher.py
check which ros nodes are working
using, rostopic list, now it's ready to be used.


## Usage
Its used to view what is being published using:
rostopic echo counter -n 5 
this -n to shut down rostopic after five messages.
if not assigned we can shut it off using the C-Ctrl

 
---------------------------------------------------------------------------------------------------------------------------



# ROS package: |my_services|

|Second main communicaton mechanism in ROS|
my_services is a ROS package contained of two dependices that gets a sensor value, sets parameters, and run a compution. service.server this imports the service, also make wait for service, following that setting up the proxy server for communiction, and to use the service. then comes the service_client, this prints out what is happening in therosnode. this is widley used for wordcount like the on in microsoft word.


## Requirements

This runs on ROS melodic installed on unbuntu 18.04

## Installation and configuration
First thing to do here is cd ~/ros_ws_01/src
then we do
catkin_create_pkg <package_name> <package_dependecies>
catkin_create_pkg my_services rospy std_msgs message_runtime message generation.

Basically the package_name is the name of the package we want to create
and package_dependecies these are the names of other ROS pacages that our package depends on
now that we have created the package, we can add the dependecies
this packge (my_services) contained:
service_client.py  service_server.py


we first do command as the following
touch <package_name> <package_dependecies>
touch my_services/src/service_client.py
then to make sure it is excutable file
we do the following command
chmod u+x <package_name> <package_dependecies>
chmod u+x my_services/src/service_client.py
and last to add the code to the file we open it with sublime
using the following command:
subl <package_name> <package_dependecies>
now we edit the package.xml to make sure it containes the required dependecies.
using  git -A, then git commit -m , and git push to make sure it's updated. this send the work to github raspratory hello-world-main.
## Getting started

we can start it with roscore, source the workspace
rosrun package and dependencies.


## Usage

Running it with roscore to test if everything works well. 


-----------------------------------------------------------------------------------------------------------------------------


# ROS package: |my_actions|

|Third main communicaton mechanism in ROS|
my_actions is the third main communication mechanism in ROS and it has two python dependcies fancy_action_server and fancy_action_server
this is to navgate to a location, performing a complex manipulation, or performing a long calculation. this sets requests for errors. using action interfernce to send goal, then move on to other task while the robot is driving

.

## Requirements

This runs on ROS melodic installed on unbuntu 18.04

## Installation and configuration
First thing to do here is cd ~/ros_ws_01/src
then we do
catkin_create_pkg <package_name> <package_dependecies>
catkin_create_pkg my_actions roscpp rospy actionlib_msgs
 mkdir action
touch action/Timer.action
Basically the package_name is the name of the package we want to create
and package_dependecies these are the names of other ROS pacages that our package depends on
now that we have created the package, we can add the dependecies
this packge (my_actions) contained:
fancy_action_client.py  fancy_action_server.py


we first do command as the following
touch <package_name> <package_dependecies>
touch my_services/src/fancy_action_server.py
then to make sure it is excutable file
we do the following command
chmod u+x <package_name> <package_dependecies>
chmod u+x my_services/src/fancy_action_server.py
and last to add the code to the file we open it with sublime
using the following command:
subl <package_name> <package_dependecies>
now we edit the package.xml to make sure it containes the required dependecies.
using  git -A, then git commit -m , and git push to make sure it's updated. this send the work to github raspratory hello-world-main.

## Getting started

this is started with roscore. 

## Usage

|roslaunch is used to test if everthing works right|
