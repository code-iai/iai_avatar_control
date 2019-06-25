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

    # Assumption: Starting at -36 237 106
    print("Call MoveTo (bowl)")
    move_to((-36, -78,106))
    rospy.sleep(3.5)


    print("Call SetRotation (Rotate towards bowl)")
    set_rotation(0,0,-180)
    rospy.sleep(1.5)


    print("grasp bowl")
    send_console_command("grasp SM_BigBowl_2 hold")
    rospy.sleep(3)

    # approach microwave and open
    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-20)
    rospy.sleep(1.5)

    print("Call MoveTo (microwave)")
    move_to((43, -25.5, 99))
    rospy.sleep(2.5)

    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-20)
    rospy.sleep(1.3)

    print("Call press open (microwave")
    send_console_command("press open")
    rospy.sleep(4)

    print("Call SetRotation (Rotate towards microwave TO PLACE)")
    set_rotation(0,0,-35)
    rospy.sleep(1.3)

    # move to mw center in order to place
    print("Call MoveTo (microwave, to place)")
    move_to((44, -60, 99))
    rospy.sleep(1.5)
    
    # exit for now
    # sys.exit(0) # EXIT FOR NOW
    # exit for now

    print("Call place right microwave")
    send_console_command("place right microwave")
    rospy.sleep(3.5)

    print("Call close microwave")
    send_console_command("close microwave")
    rospy.sleep(3.5)
    
    print("Call press start (microwave")
    send_console_command("press start")
    rospy.sleep(3.7)

    print("Call press open (microwave")
    send_console_command("press open")
    rospy.sleep(3.7)

    print("grasp bowl again")
    send_console_command("grasp SM_BigBowl_2 hold")
    rospy.sleep(3.5)

    print("Call close microwave")
    send_console_command("close microwave")
    rospy.sleep(3.5)

    print("Call SetRotation (Rotate roughly towards table )")
    set_rotation(0,0,160)
    rospy.sleep(1.5)

    print("Call MoveTo (table)")
    move_to((-402, -15, 99))
    rospy.sleep(4.5)

    print("Call SetRotation (Rotate towards table for placemen)")
    set_rotation(0,0,240)
    rospy.sleep(1.7)


    # assumption: grasped bowl should be at -408 -72 88
    print("Place right table")
    send_console_command("place right table")
    rospy.sleep(3)

    print("Call SetRotation (Rotate away from table)")
    set_rotation(0,0,180)
    rospy.sleep(1.7)

    print("Call MoveTo (away)")
    move_to((-630, 0, 99))
    rospy.sleep(2)

    print("Call SetRotation")
    set_rotation(0,0,270)
    rospy.sleep(1.7)

    print("Call MoveTo (table on the other side)")
    move_to((-630, -254, 99))
    rospy.sleep(2)

    print("Call SetRotation")
    set_rotation(0,0,0)
    rospy.sleep(1.7)

    print("Call MoveTo (move towards table again)")
    move_to((-420, -254, 99))
    rospy.sleep(2)

    print("Call SetRotation")
    set_rotation(0,0,90)
    rospy.sleep(1.7)

