#!/usr/bin/env python

import rospy
from py_two.msg import name

def callback(data):
      rospy.loginfo("FINAL %s %s "%(data.firstname,data.secondname))

def listener():
      rospy.init_node('N3',anonymous=True)

      rospy.Subscriber("T2", name, callback)

      rospy.spin()

if __name__=='__main__':
      
	try:
		listener()
	except rospy.ROSInterruptException:
		pass

