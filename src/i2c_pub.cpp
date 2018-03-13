#include <ctime>


#include <unistd.h>				//Needed for I2C port
#include <fcntl.h>				//Needed for I2C port
#include <sys/ioctl.h>			//Needed for I2C port
#include <linux/i2c-dev.h>		//Needed for I2C port

#include <stdio.h>
#include <string>

#include <ros/ros.h>
#include <visualization_msgs/Marker.h>

#include <stdint.h>

using namespace std;
using namespace ros;





	int file_i2c;
	int length;
	int16_t reading[7]={0};
	float imu[7]={0};
	unsigned char buffer[60] = {0};
	char *filename = (char*)"/dev/i2c-1";


int main(int argc,char **argv)
{
	     ros::init(argc, argv, "state_publisher");
	     ros::NodeHandle n;
       	     ros::Rate loop_rate(30);
	     ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("visualization_marker", 10);

	file_i2c = open(filename, O_RDWR);


	int addr = 0x68;          //<<<<<The I2C address of the slave
	ioctl(file_i2c, I2C_SLAVE, addr);
	

	//----- WRITE BYTES -----
	buffer[0] = 0x6b;
	buffer[1] = 0x00;
	length = 2;			//<<< Number of bytes to write
	write(file_i2c, buffer, length);		//write() returns the number of bytes actually written, if it doesn't match then an error occurred (e.g. no response from the device)
	




    visualization_msgs::Marker base_resultant;

    base_resultant.header.frame_id = "map";
    base_resultant.header.stamp = ros::Time::now();
    base_resultant.ns = "basic_shapes";
    base_resultant.type = visualization_msgs::Marker::ARROW;
    base_resultant.action = visualization_msgs::Marker::ADD;
        base_resultant.points.resize(2);
	base_resultant.points[0].x = 0.0;
	base_resultant.points[0].y = 0.0;
	base_resultant.points[0].z = 0.0;
	base_resultant.points[1].x = 0;
	base_resultant.points[1].y = 0;
	base_resultant.points[1].z = 0;
    base_resultant.scale.x = 0.1;
    base_resultant.scale.y = 0.2;
    base_resultant.scale.z = 0.3;
    base_resultant.color.r = 1.0f;
    base_resultant.color.g = 0.0f;
    base_resultant.color.b = 0.0f;
    base_resultant.color.a = 1.0;
    base_resultant.lifetime = ros::Duration();


while(ros::ok()){



	cout << clock() << endl;

	int addr = 0x68;          //<<<<<The I2C address of the slave
	ioctl(file_i2c, I2C_SLAVE, addr); 
	

	//----- WRITE BYTES -----
	buffer[0] = 0x3b;
	length = 1;			//<<< Number of bytes to write
	write(file_i2c, buffer, length);		//write() returns the number of bytes actually written, if it doesn't match then an error occurred (e.g. no response from the device)



	//----- READ BYTES -----
	length = 14;			//<<< Number of bytes to read
	read(file_i2c, buffer, length);		//read() returns the number of bytes actually read, if it doesn't match then an error occurred (e.g. no response from the device)

                for(int i=0;i<7;i++)
		{
               		reading[i] = buffer[i*2]<<8 | buffer[i*2+1];
             		cout << i+1<<" , "<< reading[i] <<endl;
		}
		//cout<<endl;


float mid=reading[0];

imu[0] = (mid-750)/16395;

mid=reading[1];
imu[1] = (mid-200)/16403;

mid=reading[2];
imu[2] = (mid-55)/16725;



cout<<imu[0]<<endl;
cout<<imu[1]<<endl;
cout<<imu[2]<<endl<<endl;



        base_resultant.points[1].x = imu[0]*5;
	base_resultant.points[1].y = imu[1]*5;
	base_resultant.points[1].z = imu[2]*5;

        marker_pub.publish(base_resultant);



loop_rate.sleep();
}//for while loop

}//for main
