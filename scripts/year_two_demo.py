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
    send_console_command("grasp SM_BigBowl_2 hold")
    rospy.sleep(4)

    # approach microwave and open
    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-30)
    rospy.sleep(1.5)

    # Assumption: Starting at -234 215 106
    print("Call MoveTo (microwave)")
    move_to((43, -25.5, 99))
    rospy.sleep(3)

    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-20)
    rospy.sleep(1.5)

    print("Call press open (microwave")
    send_console_command("press open")
    rospy.sleep(4)


    print("Call SetRotation (Rotate towards microwave)")
    set_rotation(0,0,-40)
    rospy.sleep(1.5)

    # move to mw center in order to place
    print("Call MoveTo (microwave)")
    move_to((44, -65, 99))
    rospy.sleep(3)
    
    # exit for now
    # sys.exit(0) # EXIT FOR NOW
    # exit for now

    print("Call place right microwave")
    send_console_command("place right microwave")
    rospy.sleep(3.5)

    print("Call close microwave")
    send_console_command("close microwave")
    rospy.sleep(3.5)
    
    # TODO: cooking/ press start

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
    move_to((-391, -12, 99))
    rospy.sleep(4)

    print("Call SetRotation (Rotate towards table for placemen)")
    set_rotation(0,0,240)
    rospy.sleep(1.7)

    print("Place right table")
    send_console_command("place right table")
    rospy.sleep(2.5)
