#!/usr/bin/env python

import rospy
# from geometry_msgs.msg import Pose2D
from turtlesim.msg import Pose


def callback(data):
    rospy.loginfo('Received a Pose: (%s; %s)', data.x, data.y)


def listener():
    rospy.init_node('turtle_pose_subscriber', anonymous=True)
    # rospy.Subscriber('/turtle1/pose', Pose2D, callback)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
