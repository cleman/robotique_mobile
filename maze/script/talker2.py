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
        msg.angular.z = -0.3
    else:
        msg.angular.z = 0.3

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