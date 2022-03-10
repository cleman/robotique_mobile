#!/usr/bin/env python
from re import M
from xml.sax.handler import feature_namespace_prefixes
import rospy
from std_msgs.msg import Int32
from sensor_msgs.msg import LaserScan, PointCloud2
import laser_geometry.laser_geometry as lg
import sensor_msgs.point_cloud2 as pc2
from math import sqrt
from numpy import mean,abs

pub_mode = rospy.Publisher('/mode',Int32,queue_size = 1)

global suivi,mur,ouvert,ferme
suivi = 0
mur = False
ouvert = False
ferme = False
lp = lg.LaserProjection()

def writ(data):
    file = open("/home/prof/lebhou_ws/src/maze/script/integer.txt","w")
    file.write(data)
    file.close()
    #print("message ecrit")

def callback(data):
    global suivi,mur,ouvert,ferme
    cone = 45
    pcl = lp.projectLaser(data)

    point_generator = pc2.read_points(pcl)

    

  #  rospy.loginfo(len(pc2.read_points_list(pcl)))
  #  pub.publish(pcl)
    
    # we can access a generator in a loop

    mesure = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    mesure_moy = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for point in point_generator:

        x = point[0]
        y = point[1]
        angle_mes = int(point[4])
        distance = sqrt(x**2 + y**2)*100

        mesure[int(angle_mes/20)].append(distance)
    
    for i in range (18):
        mesure[i].sort()
        mesure_moy[i] = mean(mesure[i])

    print(mesure_moy)

    dif34 = abs(mesure_moy[3]-mesure_moy[4])
    dif45 = abs(mesure_moy[4]-mesure_moy[5])

    if ((mesure_moy[4] > 15 and mesure_moy[4] < 20)):       #Suivi mur
        if (mesure_moy[3] < mesure_moy[4]):
            mode = 2
        elif (mesure_moy[5] < mesure_moy[4]):
            mode = 3
        else:
            mode = 1
    
    else:
        if (mesure_moy[4] <= 15):
            mode = 2
        elif (mesure_moy[3] > (mesure_moy[4])):
            mode = 3
        else:
            mode = 1
    
    if (not mesure[4]):                                     #trop proche mur (valeur non lisible)
        mode = 2

    if (mesure_moy[0] < 25 or mesure_moy[17] < 25):         #angle ferme
        mode = 4

    if (mesure_moy[3] > mesure_moy[4]+20 or (mesure_moy[5] > mesure_moy[4]+20 and mesure_moy[3] > 20)):
        mode = 5
    
    
    
    
    print(mode)
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