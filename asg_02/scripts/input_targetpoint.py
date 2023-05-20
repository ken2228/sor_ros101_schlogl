#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Point

point = Point()

rospy.init_node('inputpoint')

point.x = float(input("Give the target location X coordinate:"))
point.y = float(input("Give the target location Y coordinate:"))

publisher = rospy.Publisher('/targetpoint', Point, queue_size=10)

rospy.loginfo("I will publish to the topic move2point")

while not rospy.is_shutdown():
	publisher.publish(point)
	rospy.sleep(0.1)
