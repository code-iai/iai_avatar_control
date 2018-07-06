import math
import sys
import rospy
from avatar_services import *
    
if __name__ == "__main__":
    print("Init rospy node")
    rospy.init_node("year_one_demo")
    print("Starting program")
    rospy.sleep(2)

    #print("Call StartEnablement (left_hand up)")
    #start_enablement("left_hand_ik",(20,56,118))
    #rospy.sleep(2)


    # Assumption: Starting at 570 70 07.3
    print("Call MoveTo (Kitchen Main)")
    move_to((891,381,97))
    rospy.sleep(3)

    print("Call SetRotation (Rotate to milk box)")
    set_rotation(0,0,-177)
    rospy.sleep(1.5)

    print("Call MoveTo (Fridge)")
    move_to((530,280,97))
    rospy.sleep(3)

    print("Call StartEnablement (left hand ik)")
    start_enablement("left_hand_ik",(20,60,70))
    rospy.sleep(0.1)

    print("Call StartEnablement (left hand rotation)")
    start_enablement("left_hand_rotation",(-40,40,40))
    rospy.sleep(0.6)

    print("Call SetInterpolationTarget (left hand ik)")
    set_interpolation_target("left_hand_ik",(20,60,100))
    rospy.sleep(1.7)

    print("Call SetInterpolationTarget (left hand ik)")
    set_interpolation_target("left_hand_ik",(5,50,100))
    rospy.sleep(0.4)

    print("Call StartDisablement (left hand ik)")
    start_disablement("left_hand_ik",(0,0,0))
    rospy.sleep(0.1)

    print("Call StartDisablement (left hand rotation)")
    start_disablement("left_hand_rotation",(0,0,0))
    rospy.sleep(1.2)

    print("Call MoveTo (Fridge)")
    move_to((517,280,97))
    rospy.sleep(1)


    print("Call StartEnablement (spine)")
    start_enablement("spine",(33,0,0))
    rospy.sleep(0.1)

    print("Call StartEnablement (left hand rotation)")
    start_enablement("left_hand_rotation",(-40,40,40))
    rospy.sleep(0.5)


    print("Call StartEnablement (left hand ik)")
    start_enablement("left_hand_ik",(-5,60,70))
    rospy.sleep(0.6)

    print("Call SetInterpolationTarget (left hand ik)")
    set_interpolation_target("left_hand_ik",(-13,90,90))
    rospy.sleep(1.0)

    # print("Call SetInterpolationTarget (ik)")
    # set_interpolation_target("left_hand_ik",(20,80,100))
    # rospy.sleep(3.2)

    # spine x:36,0,0
    # hand rotation -40 40 40


    sys.exit(0)

    # TODO
    # start 20 50 50
    # set -40 40 40


    print("Call Start Grasp")
    send_command("start_grasp")
    rospy.sleep(1.5)

    print("Call Stop Grasp")
    send_command("stop_grasp")
    rospy.sleep(1.3)

    print("Call SetRotation (Rotate to kitchen island)")
    set_rotation(0,0,0)
    rospy.sleep(1.5)


    print("Call MoveTo (Go to kitchen island)")
    move_to((570,440,97))
    rospy.sleep(2.0)

    print("Call SetRotation (Rotate to kitchen island 2)")
    set_rotation(0,0,0)
    rospy.sleep(1)


    print("Call StartEnablement (spine)")
    start_enablement("spine",(35,0,0))
    rospy.sleep(0.1)

    print("Call StartEnablement (left hand ik)")
    start_enablement("left_hand_ik",(20,30,100))
    rospy.sleep(0.1)

    print("Call StartEnablement (left hand rotation)")
    start_enablement("left_hand_rotation",(10,60,120))
    rospy.sleep(0.6)

    print("Call Move Head")
    move_head(-20,20)
    rospy.sleep(0.2)

    print("Call SetInterpolationTarget (left hand ik)")
    set_interpolation_target("left_hand_ik",(20,50,93))
    rospy.sleep(3.2)

    print("Call Detach Object")
    send_command("detach_object")
    rospy.sleep(1.5)

    print("Call Move Head")
    move_head(0,0)
    rospy.sleep(0.2)

    print("Call Stop Grasp")
    send_command("stop_grasp")
    rospy.sleep(1)

    #sys.exit(0)
    #Placing the object END


    print("Call SetRotation (Rotate towards bread)")
    set_rotation(0,0,90)
    rospy.sleep(1.5)


    print("Call MoveTo (Go to bread)")
    move_to((570,520,97))
    rospy.sleep(2.3)

    print("Call SetRotation (Final Rotate to bread)")
    set_rotation(0,0,0)
    rospy.sleep(2)

    print("Call grasp r")
    send_command("start_grasp_r")
    rospy.sleep(1)

    print("Call stop_grasp_r")
    send_command("stop_grasp_r")
    rospy.sleep(2)


    print("Call cut 1")
    send_command("cut")
    rospy.sleep(7)

    print("Call cut 2")
    send_command("cut")
    rospy.sleep(1)


    #print("Call SetRotation")
    #set_rotation(0,0,180)
    #rospy.sleep(1)

    #print("Call Move Head")
    #move_head(-20,35)
    #rospy.sleep(1)

    #print("Call Start Grasp")
    #send_command("start_grasp")
    #rospy.sleep(3)

    #print("Call Stop Grasp")
    #send_command("stop_grasp")
    #rospy.sleep(1)

    #print("Call Move Head")
    #move_head(0,0)
    #rospy.sleep(1)

    #print("Call Lift Arm")
    #send_command("lift_arm")
    #rospy.sleep(3)

    #print("Call Detach Object")
    #send_command("detach_object")
    #rospy.sleep(1)

    #print("Call Stop Grasp")
    #send_command("stop_grasp")
    #rospy.sleep(1)

    #print("Call MoveTo")
    #move_to((740,470,103))
    #rospy.sleep(2)

    #print("Call SetRotation")
    #set_rotation(0,0,180)
    #rospy.sleep(1)

    #print("Call Move Head")
    #move_head(0,35)
    #rospy.sleep(0.5)

    #print("Call grasp r")
    #send_command("start_grasp_r")
    #rospy.sleep(1)

    #print("Call stop_grasp_r")
    #send_command("stop_grasp_r")
    #rospy.sleep(2)


    #print("Call cut")
    #send_command("cut")
    #rospy.sleep(1)


    # start_grasp_r
    # stop_grasp_r
    # cut
