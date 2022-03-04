#!usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from random import randrange

def read():
    file = open("/home/prof/lebhou_ws/src/maze/script/integer.txt","r")
    data = file.readlines()
    file.close()
    try :
        return data[0]
    except:
        return 1

def talker():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 10hz
    
    while not rospy.is_shutdown():

        mode = int(read())
        #pause = input()
   
        msg = Twist()
        
        print(mode)
        if (mode == 1):
            msg.linear.x = -0.05
            msg.angular.z = 1.6
        elif (mode == 2):
            msg.linear.x = 0.15
        elif (mode == 3):
            msg.linear.x = 0.02
            msg.angular.z = 0.1
        elif (mode == 4):
            msg.linear.x = 0.02
            msg.angular.z = -0.1
        elif (mode == 5):
            msg.linear.x = -0.05
            msg.angular.z = -1

        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass