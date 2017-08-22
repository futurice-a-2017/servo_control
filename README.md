Repository for controlling servos connected to Arduino via ROS. 

Currently includes an example Arduino sketch and an example ROS-node for publishing servo position.

Dependencies:
Rosserial-packages, see http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup

Steps (or see http://wiki.ros.org/rosserial_arduino/Tutorials/Servo%20Controller):

1. Open Arduino IDE and upload the Sketch (in case of permission problem, run 'sudo chmod 666 /dev/ttyACM0' for whatever port the Arduino is connected to)

2. Run 'roscore'

3. Open new tab and run 'rosrun rosserial_python serial_node.py /dev/ttyACM0' (For whatever port the Arduino is connected to)

4. Open new tab and run 'rosrun inmoov_servo_control servo.py'
