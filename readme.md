本功能包包含了gmapping、cartographer、karto、hector四种不同的功能包，使用stage进行仿真。你可以通过修改stage文件夹下的图像文件来改变仿真的场景。
PS：相关ROS功能包需要自行安装，另外还需要安装[evo](https://github.com/MichaelGrupp/evo)进行误差计算。

1. 使用命令`roslaunch slam_method_evaluation stage_simulation.launch slam_method:=gmapping`进行slam

2. 使用命令`rosrun teleop_twist_keyboard teleop_twist_keyboard.py`进行仿真控制

3. 使用命令`python src/slam_method_evaluation/scripts/record_trajectory.py`记录slam位姿,位姿会保存为文件。

4. 使用命令`evo_traj tum /home/jimazeyu/catkin_ws/src/slam_method_evaluation/traj/footprint_pose.txt --ref=/home/jimazeyu/catkin_ws/src/slam_method_evaluation/traj/ground_truth_pose.txt --plot --plot_mode xy`查看轨迹

5.  使用命令`evo_rpe tum /home/jimazeyu/catkin_ws/src/slam_method_evaluation/traj/footprint_pose.txt /home/jimazeyu/catkin_ws/src/slam_method_evaluation/traj/ground_truth_pose.txt -p --plot_mode=xy`查看相对误差

6.  使用命令`evo_ape tum /home/jimazeyu/catkin_ws/src/slam_method_evaluation/traj/footprint_pose.txt /home/jimazeyu/catkin_ws/src/slam_method_evaluation/traj/ground_truth_pose.txt -p --plot_mode=xy`查看绝对误差

7. 使用命令`rosrun map_server map_saver -f /home/jimazeyu/catkin_ws/src/slam_method_evaluation/map/map_gmapping`保存地图，这是我的命令，你需要修改路径。

8. 使用`mapping_accuracy_calculate`文件夹中的jupyter文件来计算地图的准确度，其中使用了[icp](https://github.com/ClayFlannigan/icp)包进行2D点云配准。
