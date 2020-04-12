#!/usr/bin/env python  #2020/4/12



import rospy
from std_msgs.msg import String
	
def callback(msg):
	    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)
	    
def listener():


	    rospy.init_node('listener', anonymous=False)
	
	    rospy.Subscriber("/chatter", String, callback)
	    rospy.spin()



	
if __name__ == '__main__':
	    listener()
