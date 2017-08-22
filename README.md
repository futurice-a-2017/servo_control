Repository for controlling servos connected to Arduino via ROS. 

Currently includes an example Arduino sketch and an example ROS-node for publishing servo position.

Steps to make it work:

1. Make sure you have ROS installed and a catkin workspace setup, refer to README.md in simulation-repository for instructions

2. Clone repository to ~/catkin_ws/src (or whatever your catkin workspace is), navigate to ~/catkin_ws/ and run 'catkin_make' and 'source devel/setup.bash'

3. Follow http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup and install required packages. Follow steps below or http://wiki.ros.org/rosserial_arduino/Tutorials/Servo%20Controller

4. Open Arduino IDE and upload the Sketch (in case of permission problem, run 'sudo chmod 666 /dev/ttyACM0' for whatever port the Arduino is connected to)

5. Run 'roscore'

6. Open new tab and run 'rosrun rosserial_python serial_node.py /dev/ttyACM0' (For whatever port the Arduino is connected to)

7. Open new tab and run 'rosrun inmoov_servo_control servo.py'
