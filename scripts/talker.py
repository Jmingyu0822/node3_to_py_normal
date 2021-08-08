#!/usr/bin/env python

import rospy
from py_two.msg import name 

def talker():
      pub = rospy.Publisher('T1',name,queue_size=10) 
      rospy.init_node('N1', anonymous = True)
      rate = rospy.Rate(10) #10hz
      msg =name()
      msg.firstname = "J"
      msg.age=23
      while not rospy.is_shutdown():
            rospy.loginfo(msg.firstname)
            pub.publish(msg)
            rate.sleep()

if __name__=='__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
