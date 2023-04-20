#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
	radius = data.data
	squared_radius = radius * radius
	pub.publish(squared_radius)
	

rospy.init_node("radius_squarer") #init the node
pub = rospy.Publisher("/radius_squared", Float64, queue_size=10) #create the publisher " squared radius
rospy.Subscriber("/radius", Float64, callback) # Create a subscriber
rospy.spin() # ROS "infinit loop" 


