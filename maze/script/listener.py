#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan, PointCloud2
import laser_geometry.laser_geometry as lg
import sensor_msgs.point_cloud2 as pc2

#global pub
lp = lg.LaserProjection()

def writ(data):
    file = open("integer","w")
    file.write(data)
    file.close()

def callback(data):
    cone = 30
    angle = 270
    pcl = lp.projectLaser(data)

    point_generator = pc2.read_points(pcl)

    

  #  rospy.loginfo(len(pc2.read_points_list(pcl)))
  #  pub.publish(pcl)
    
    # we can access a generator in a loop
    total = 0
    nbr = 0
    for point in point_generator:
#        rospy.loginfo(point)
        point = str(point)
        point = point.replace("(","").replace(")","")
        point = point.split(",")
        point[4] = int(point[4])
        point[3] = float(point[3])
        if (point[4] >= angle-cone and point[4] <= angle+cone):
            print(point)
            total += point[3]
            nbr += 1
    distance = total/nbr
    print(distance)
    if (distance >= 6800 and distance <= 9700):
        print("je vois le mur")
    else:
        print("trop loin ou trop proche")

    writ(distance)

    # pause = input()
    
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