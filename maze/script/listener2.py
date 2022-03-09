#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import LaserScan, PointCloud2
import laser_geometry.laser_geometry as lg
import sensor_msgs.point_cloud2 as pc2
from math import sqrt
from numpy import mean,abs

pub_mode = rospy.Publisher('/mode',Int32,queue_size = 1)

global angle,cmin,cmax,dmax
angle = 0
cmin = 7000
cmax = 9000
dmax = 6000
lp = lg.LaserProjection()

def writ(data):
    file = open("/home/prof/lebhou_ws/src/maze/script/integer.txt","w")
    file.write(data)
    file.close()
    #print("message ecrit")

def callback(data):
    global angle,cmin,cmax,dmax
    cone = 45
    pcl = lp.projectLaser(data)

    point_generator = pc2.read_points(pcl)

    

  #  rospy.loginfo(len(pc2.read_points_list(pcl)))
  #  pub.publish(pcl)
    
    # we can access a generator in a loop
    total = 0
    nbr = 0

    angle = 90
    cone = 20
    a0 = [[],[]]
    a90 = [[]]*8
    for point in point_generator:

        x = point[0]
        y = point[1]
        angle_mes = int(point[4])
        distance = sqrt(x**2 + y**2)*100

        #Angle devant
        if (angle == 0):
            if (angle_mes > 360-cone and angle_mes <= 360):
                a0[1].append(distance)                          #droite
            elif (angle_mes >= 0 and angle_mes < cone):
                a0[0].append(distance)                          #gauche

        #Angle cote
        if (angle == 90):
            if (angle_mes >=0 and angle_mes < cone):
                a90[7].append
            elif (angle_mes >= 220):
                a90[int((angle_mes-220)/20)].append(distance)
    
#    a00m = mean(a0[0])
#    a01m = mean(a0[1])

    '''
    a0m = [0]*2
    for i in range(2):
        a0m[i] = mean(a0[i])
 #   print(a00m,a01m)
    if (abs(a0m[0] - a0m[1]) > 1):
        if (a0[0] > a0[1]):
            mode = 1
        else:
            mode = 2

    '''
    
    a90m = [0]*8
    print(mean(a90[0]))
    print(mean(a90[1]))
    for i in range (8):
        a90m[i] = mean(a90[i])

    a90m2 = a90m.sort()
#    print(a90m,a90m2)
    if (a90m2[0] != a90m[3] and a90m2[0] != a90m[4]):
        mode = 1
    


        pub_mode.publish(int(mode))


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

 #   global pub
 #   pub = rospy.Publisher("test_pc", PointCloud2, queue_size=10)

    sub = rospy.Subscriber('/scan', LaserScan, callback, queue_size=10)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

'''
polaire to cartésian
import laser_geometry.laser_geometry as lg

lp = lg.LaserProjection()
pcl = lp.projectLaser(msg)


'''