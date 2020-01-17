#!/usr/bin/env python
import math
import sys
import rospy
from avatar_services import *
    
if __name__ == "__main__":
    print("Init rospy node")
    rospy.init_node("year_two_demo")

    print("Setting up Action Client")
    pub = rospy.Publisher('Question/goal', QnAActionGoal, queue_size=10)
    rate = rospy.Rate(5)
    rate.sleep()
    client = actionlib.SimpleActionClient('Question',QnAAction)

    print("Starting program")
    
    result = send_question("Hola k ase?**")
    print "Result:", result
    #rospy.sleep(0.5)
    result = send_question("Do you want this topin?")
    print "Result:", result



