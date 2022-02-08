#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import laser_geometry.laser_geometry as lg
import sensor_msgs.point_cloud2 as pc2


lp = lg.LaserProjection()

def callback(data):
    pcl = lp.projectLaser(data)

    point_generator = pc2.read_points(pcl)
    
    # we can access a generator in a loop
    for point in point_generator:
        rospy.loginfo(point)


    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

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