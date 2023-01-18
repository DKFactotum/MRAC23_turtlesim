#!/usr/bin/env python

import sys

import rospy
from geometry_msgs.msg import Twist, Vector3
from turtlesim.msg import Pose


def publishTurtlesimPose(lv, av):
    publisher = rospy.Publisher('/turtle1/pose', Pose)
    rospy.init_node('turtle_twistpose_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    data = Pose()
    data.linear_velocity = lv
    data.angular_velocity = av
    while not rospy.is_shutdown():
        rospy.loginfo(
            'Publishing Turtle Pose by linear and angular components')
        publisher.publish(data)
        rate.sleep()


def publishTwist(lx, ly, lz, ax, ay, az):
    publisher = rospy.Publisher('/turtle1/twist', Twist)
    rospy.init_node('turtle_twist_publisher', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    data = Twist()
    data.linear = Vector3(lx, ly, lz)
    data.angular = Vector3(ax, ay, az)
    while not rospy.is_shutdown():
        rospy.loginfo('Publishing Turtle Twist')
        publisher.publish(data)
        rate.sleep()


if __name__ == '__main__':
    if len(sys.argv) == 3:
        lv = float(sys.argv[1])
        av = float(sys.argv[2])
        publishTurtlesimPose(lv, av)
    elif len(sys.argv) == 7:
        lx = float(sys.argv[1])
        ly = float(sys.argv[2])
        lz = float(sys.argv[3])
        ax = float(sys.argv[4])
        ay = float(sys.argv[5])
        az = float(sys.argv[6])
        publishTwist(lx, ly, lz, ax, ay, az)
    else:
        print('Input 2 floats for linear and angular velocities or 3 linear and 3 angular float components for twist')
        sys.exit(1)
