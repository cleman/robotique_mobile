#!usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from random import randrange

def read():
    file = open("/home/prof/lebhou_ws/src/maze/script/integer","r")
    data = file.readlines()
    file.close()
    return data[0]
        
def talker():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    
    while not rospy.is_shutdown():

        print(read())
   
        msg = Twist()
        msg.linear.x = randrange(-5,5)
        msg.angular.z = randrange(-3,3)
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass