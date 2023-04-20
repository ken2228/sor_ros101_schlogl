#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

rospy.init_node("cylinder_input")
radius_pub = rospy.Publisher("/radius", Float64, queue_size=10)
height_pub = rospy.Publisher("/height", Float64, queue_size=10)
mass_pub = rospy.Publisher("/mass", Float64, queue_size=10)

radius = float(input("Enter radius in meter: "))
height = float(input("Enter height in meter: "))
mass = float(input("Enter the mass (kg/m3) "))

while not rospy.is_shutdown():
	radius_pub.publish(radius)
	height_pub.publish(height)
	mass_pub.publish(mass)
	rospy.sleep(0.1)

