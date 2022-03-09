#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan, PointCloud2
import laser_geometry.laser_geometry as lg
import sensor_msgs.point_cloud2 as pc2

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
    for point in point_generator:
#        rospy.loginfo(point)
        point = str(point)
        point = point.replace("(","").replace(")","")
        point = point.split(",")
        point[4] = int(point[4])
        point[3] = float(point[3])
        if ((point[4]+360) >= (angle-cone+360) and (point[4]+360) <= (angle+cone+360)):
            #print(point)
            total += point[3]
            nbr += 1
    distance = total/nbr
    #print(distance)
#    if (distance >= 6800 and distance <= 9700):
#        print("je vois le mur")
#    else:
#        print("trop loin ou trop proche")

    
    #writ(str(distance))

    print(angle)    
    '''
    if (angle == 0 and distance > 5000):
        mode = 1        #tourne
        angle = 0
    elif (angle == 0 and distance < 5000):
        mode = 2        #avance
        angle = 270
    elif (angle == 270 and distance > 10000):
        mode = 3        #eloigne du mur
        angle = 0
    elif (angle == 270 and distance < 6500 and distance > 5000):
        mode = 4        #vers le mur
        angle = 0
    elif (angle == 270 and distance <= 5000):
        mode = 5
        angle = 0
    elif (angle == 270 and distance >= 6500 and distance <= 10000):
        mode = 2        #continue droit
        angle = 0

    '''
    if (angle == 270):
        if (distance >= cmin and distance <= cmax):
            mode = 1        #Avance
            angle = 0
        elif (distance > cmin):
            mode = 2        #Toune gauche peu
            angle = 0
        else:
            mode = 3        #Tourne droite peu
            angle = 0
    elif (angle == 0):
        if (distance > dmax):
            mode = 4        #Tourne gauche beaucoup
            angle = 0
        else:
            mode = 1        #Avance
            angle = 270

    print("angle: ", angle)
    print("mode", mode)
    print("intensite", distance)
    print()
    
    writ(str(mode))
    

    #pause = input()
    
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