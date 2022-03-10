#!usr/bin/env python
import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from random import randrange
from time import sleep

def move(data):
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(100) # 100hz
    msg = Twist()

    print(data.data)
    mode = data.data

    if (mode == 1):
        msg.linear.x = 0.05
    elif (mode == 2):
        msg.linear.x = 0.05
        msg.angular.z = -0.1
    elif (mode == 3):
        msg.linear.x = 0.05
        msg.angular.z = 0.1
    elif (mode == 4):
        msg.linear.x = 0.03
        msg.angular.z = -0.6
    elif (mode == 5):
        msg.linear.x = 0.03
        msg.angular.z = 0.8
    elif (mode == 6):
        msg.angular.z = -1
    elif (mode == 7):
        msg.angular.z = 1

    pub.publish(msg)
    rate.sleep()


def read():
    file = open("/home/prof/lebhou_ws/src/maze/script/integer.txt","r")
    data = file.readlines()
    file.close()
    try :
        return data[0]
    except:
        return 1

def talker():
    
    rospy.init_node('talker', anonymous=True)
    rospy.Subscriber('/mode', Int32,move)
    
    
    while not rospy.is_shutdown():

        mode = int(read())
        #pause = input()
   
        msg = Twist()

        

      #  pub.publish(msg)
      #  rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass