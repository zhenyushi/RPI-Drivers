#include <stdio.h>
#include <stdlib.h>

#include "ros/ros.h"

#include "std_msgs/MultiArrayLayout.h"
#include "std_msgs/MultiArrayDimension.h"

#include "std_msgs/Int32MultiArray.h"

int main(int argc, char **argv)
{
    

	ros::init(argc, argv, "arrayPublisher");

	ros::NodeHandle n;

	ros::Publisher pub = n.advertise<std_msgs::Int32MultiArray>("array", 100);

	ros::Rate loop_rate(10);

	while (ros::ok())
	{
		std_msgs::Int32MultiArray array;
		
		array.data.clear();
		
		for (int i = 0; i < 90; i++)
		{
			//assign array a random number between 0 and 255.
			array.data.push_back(rand() % 255);
		}
		
		pub.publish(array);
		
		ROS_INFO("I published something!");
		
		ros::spinOnce();
		
		loop_rate.sleep();
	}

}
