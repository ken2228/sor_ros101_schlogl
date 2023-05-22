#!/usr/bin/env python

import rospy
import math
import time

from geometry_msgs.msg import Point, Twist
from turtlesim.msg import Pose

target_received = False
pose_received = False

targetPoint= Point()
current_pose = Pose()

def targetCallback(data):
	global targetPoint
	global target_received
	targetPoint = data
	target_received = True
		
def poseCallback(data):
	global current_pose
	global pose_received
	current_pose = data
	pose_received = True


def rotate2target():
	twistMsg = Twist()
	multiplier = 1
	rospy.loginfo("rotating to: %f !", current_pose.theta)
	targetHeading = math.atan2(targetPoint.x - current_pose.x, targetPoint.y - current_pose.y)
 	
 	
	while float(current_pose.theta) != float(targetHeading):
		rospy.loginfo("currentheading = %f, targetheading = %f", current_pose.theta, targetHeading)
		twistMsg.linear.x = 0.0
		
		if current_pose.theta > targetHeading:
			multiplier = -1
		
		twistMsg.angular.z = abs(current_pose.theta - targetHeading)* multiplier # -1*math.pi/2.0
		pub.publish(twistMsg)
		rospy.sleep(0.1)
		if int(current_pose.theta * 100) == int(targetHeading * 100):
			break
			
	twistMsg.angular.z = 0.0
	pub.publish(twistMsg)
	rospy.loginfo("End of turning reached!")
 	
 	
 	
def move2target():
	#make calculations to move to the target
	if target_received and pose_received:
		rospy.loginfo("targetPoint and pose received, calculating!")
		rospy.loginfo("Current Pose: %f, %f | theta %f", current_pose.x, current_pose.y, current_pose.theta)
		rotate2target()
		


rospy.init_node('move2point')
rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
rospy.Subscriber("/targetpoint", Point, targetCallback) # Create a subscriber
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)

while not rospy.is_shutdown():
	move2target()
	rospy.sleep(0.1)
