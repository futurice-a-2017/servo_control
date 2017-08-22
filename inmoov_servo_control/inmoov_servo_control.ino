#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/UInt16.h>

ros::NodeHandle  nh;

Servo servo; // Create servo object

// Callback function on receiving a message
void servo_cb( const std_msgs::UInt16& cmd_msg){
  servo.write(cmd_msg.data); //set servo angle  
}


ros::Subscriber<std_msgs::UInt16> sub("servo", servo_cb); // Create subscriber

void setup(){
  nh.initNode(); // Initialize ROS node
  nh.subscribe(sub); // Activate subscriber
  
  servo.attach(9); //attach it to pin 9
}

void loop(){
  nh.spinOnce(); // Run ROS loop
  delay(1);
}
