#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt16

# ROS Publisher function
def talker():
    # Create publisher
    pub = rospy.Publisher('servo', UInt16, queue_size=10)
    # Initialize new ROS node 
    rospy.init_node('test')
    # Create timer (Hz) for loop execution
    rate = rospy.Rate(10)

    new_angle = 0
    angle_change = 2
    # Angle increase(1) or decrease(2)
    direction = 1
    # Loop as long as roscore is running
    while not rospy.is_shutdown():
        # Set new direction if limits are reached
        if direction == 1 and new_angle > (180 - angle_change):
            direction = 0
        elif direction == 0 and new_angle < (angle_change):
            direction = 1
        # Set new position depending on current direction
        if direction == 1:
            new_angle += angle_change
        elif direction == 0:
            new_angle -= angle_change


        # Create new joint state message
        angle_msg = UInt16()

        # Set joint names
        angle_msg.data = new_angle

        # Publish the message
        pub.publish(new_angle)

        # Sleep timer
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass