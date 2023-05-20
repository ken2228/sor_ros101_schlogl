#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Point, Twist
from turtlesim.msg import Pose

import math

target_received = False
pose_received = False

target = Point()
current_pose = Pose()

def targetCallback(data):
	global target
	global target_received
	target = data
	target_received = True
		
def poseCallback(data):
	global current_pose
	global pose_received
	current_pose = data
	pose_received = True

def move2target():
	#make calculations to move to the target
	if target_received and pose_received:
		rospy.loginfo("target and pose received, calculating!")
		rospy.loginfo("Current Pose: %f, %f | theta %f", current_pose.x, current_pose.y, current_pose.theta)
		


rospy.init_node('move2point')
rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
rospy.Subscriber("/targetpoint", Point, targetCallback) # Create a subscriber
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)

while not rospy.is_shutdown():
	move2target()
	rospy.sleep(0.1)
