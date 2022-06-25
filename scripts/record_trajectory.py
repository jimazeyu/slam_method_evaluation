#!/usr/bin/python
# coding=utf8
# 订阅slam估计位姿
import rospy
import tf
from nav_msgs.msg import Odometry

# 将位姿数组写入文件
def write_pose_to_file(pose_array, file_name):
    with open(file_name, 'w') as f:
        for pose_ in pose_array:
            pose = pose_.pose.pose
            # 获取时间戳
            time_stamp = pose_.header.stamp.secs + pose_.header.stamp.nsecs * 1e-9
            f.write(str(time_stamp)+" ") # 时间戳
            f.write(str(pose.position.x) + ' ' + str(pose.position.y) + ' ' + str(pose.position.z) + ' ') # 位置
            f.write(str(pose.orientation.x) + ' ' + str(pose.orientation.y) + ' ' + str(pose.orientation.z) + ' ' + str(pose.orientation.w) + '\n') # 姿态
    f.close()

# main
if __name__ == '__main__':
    # 提示开始
    print('Start to record trajectory...')
    # 初始化节点
    rospy.init_node('get_footprint_tf')
    # listener监听slam估计位姿态
    listener = tf.TransformListener()
    rate = rospy.Rate(10.0)
    # 位姿数组
    footprint_pose = []
    ground_truth_pose = []
    while not rospy.is_shutdown():
        # 订阅真实位姿
        ground_truth = rospy.wait_for_message('/base_pose_ground_truth', Odometry)
        # 接收slam估计位姿
        try:
            (trans,rot) = listener.lookupTransform('/map', '/base_footprint', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        estimate_pose = Odometry()
        estimate_pose.header = ground_truth.header
        estimate_pose.pose.pose.position.x=trans[0]
        estimate_pose.pose.pose.position.y=trans[1]
        estimate_pose.pose.pose.position.z=trans[2]
        estimate_pose.pose.pose.orientation.x=rot[0]
        estimate_pose.pose.pose.orientation.y=rot[1]
        estimate_pose.pose.pose.orientation.z=rot[2]
        estimate_pose.pose.pose.orientation.w=rot[3]
        # 计算位姿数组
        footprint_pose.append(estimate_pose)
        ground_truth_pose.append(ground_truth)
        # print("estimate",estimate_pose.pose.pose)
        # print("ground_truth",ground_truth.pose.pose)
        # 将位姿数组写入文件
        write_pose_to_file(footprint_pose, './src/slam_method_evaluation/traj/footprint_pose.txt')
        write_pose_to_file(ground_truth_pose, './src/slam_method_evaluation/traj/ground_truth_pose.txt')
        rate.sleep()