#!/usr/bin/env python

import rospy
from py_two.msg import name

class Middle:
	
	def __init__(self): 

		self.msg=name()
		rospy.init_node('N2',anonymous=True)
		self.sub=rospy.Subscriber('T1',name,self.callback) 
		self.midpub = rospy.Publisher('T2',name,queue_size=10) 
		
	def callback(self,data):
		rospy.loginfo("%s is age: %d "%(data.firstname,data.age))
		self.midtalk(data) 
	def midtalk(self,data): 
		
		self.msg.firstname=data.firstname
		self.msg.secondname="MG"

		rate = rospy.Rate(10)

		while not rospy.is_shutdown():
			rospy.loginfo(self.msg.secondname)
			self.midpub.publish(self.msg)
			rate.sleep()

if __name__=='__main__':
	
	try:	
		Middle = Middle()
		rospy.spin()
	except rospy.ROSInterruptException:
		pass




		
		

