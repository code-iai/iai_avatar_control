#!/usr/bin/env python
import math
import sys
import rospy
from avatar_services import *
    
if __name__ == "__main__":
    print("Init rospy node")
    rospy.init_node("year_two_demo")
    print("Starting program")
    rospy.sleep(2)

    # Assumption: Starting at -234 215 106
    print("Call MoveTo (bowl)")
    move_to((-112, -12, 99))
    rospy.sleep(3)



    print("grasp bowl")
    send_console_command("grasp SM_BigBowl_5 hold")
    rospy.sleep(3)

    # approach microwave and open
    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-40)
    rospy.sleep(1.5)

    # Assumption: Starting at -234 215 106
    print("Call MoveTo (microwave)")
    move_to((43, -25, 99))
    rospy.sleep(3)

    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-20)
    rospy.sleep(1.5)

    print("Call press open (microwave")
    send_console_command("press open")
    rospy.sleep(3)

    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-40)
    rospy.sleep(1.5)

    # move to mw center in order to place
    print("Call MoveTo (microwave)")
    move_to((42, -45, 99))
    rospy.sleep(3)

    print("Call place right microwave")
    send_console_command("place right microwave")
    rospy.sleep(1.5)

    print("Call close microwave")
    send_console_command("close microwave")
    rospy.sleep(1.5)
