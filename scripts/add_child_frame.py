#!/usr/bin/python
# coding=utf8
# 因为stage发布的odom数据child_frame_id是空的，需要自己添加
import rospy
from nav_msgs.msg import Odometry
# main
if __name__ == '__main__':
    # log message
    print('----------------------')
    print('----------------------')
    print('add_child_frame start')
    print('----------------------')
    print('----------------------')
    # init node
    rospy.init_node('add_child_frame')
    pub = rospy.Publisher('/odom_update', Odometry, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # 订阅/odom数据
        odom_msg = rospy.wait_for_message('/odom', Odometry)
        odom_msg.child_frame_id = 'base_footprint'
        pub.publish(odom_msg)
        rate.sleep()
    rospy.spin()