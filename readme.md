This package includes four different packages: gmapping, cartographer, karto, and hector, and uses stage for simulation. You can change the simulation scene by modifying the image files in the stage directory. 
PS: The relevant ROS packages need to be installed separately, and you also need to install [evo](https://github.com/MichaelGrupp/evo) for error calculation.

1. Use the command `roslaunch slam_method_evaluation stage_simulation.launch slam_method:=gmapping` to perform SLAM.

2. Use the command `rosrun teleop_twist_keyboard teleop_twist_keyboard.py` for simulation control.

3. Use the command `python src/slam_method_evaluation/scripts/record_trajectory.py` to record the SLAM pose. The pose will be saved as a file.

4. Use the command `evo_traj tum /home/xxx/catkin_ws/src/slam_method_evaluation/traj/footprint_pose.txt --ref=/home/xxx/catkin_ws/src/slam_method_evaluation/traj/ground_truth_pose.txt --plot --plot_mode xy` to view the trajectory.

5. Use the command `evo_rpe tum /home/xxx/catkin_ws/src/slam_method_evaluation/traj/footprint_pose.txt /home/xxx/catkin_ws/src/slam_method_evaluation/traj/ground_truth_pose.txt -p --plot_mode=xy` to view the relative error.

6. Use the command `evo_ape tum /home/xxx/catkin_ws/src/slam_method_evaluation/traj/footprint_pose.txt /home/xxx/catkin_ws/src/slam_method_evaluation/traj/ground_truth_pose.txt -p --plot_mode=xy` to view the absolute error.

7. Use the command `rosrun map_server map_saver -f /home/xxx/catkin_ws/src/slam_method_evaluation/map/map_gmapping` to save the map. This is my command, and you need to modify the path.

8. Use the jupyter file in the `mapping_accuracy_calculate` directory to calculate the accuracy of the map. The [icp](https://github.com/ClayFlannigan/icp) package is used for 2D point cloud registration in it.
