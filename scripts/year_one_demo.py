import math
import sys
import rospy
from iai_avatar_msgs.srv import *
#from iai_avatar_msgs.msg import *
#from geometry_msgs.msg import Pose, Point, Quaternion


def send_command(comm):
    print("Waiting for service")
    service_name = '/avatar/send_command'

    rospy.wait_for_service( service_name )
    try:
        send_command_service = rospy.ServiceProxy(service_name, Command)
        req = CommandRequest()
        req.command = comm

        print("Sending service request")
        resp1 = send_command_service(req)
        print("Got service response")
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def move_to(coords):
    print("Waiting for service")
    service_name = '/avatar/move_to'

    rospy.wait_for_service( service_name )
    try:
        move_to_service = rospy.ServiceProxy(service_name, MoveTo)
        req = MoveToRequest()
        req.position.x = coords[0]
        req.position.y = coords[1]
        req.position.z = coords[2]

        print("Sending service request")
        resp1 = move_to_service(req)
        print("Got service response")
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def move_head(pan,tilt):
    print("Waiting for service")
    service_name = '/avatar/move_head'

    rospy.wait_for_service( service_name )
    try:
        move_head_service = rospy.ServiceProxy(service_name, PanTilt)
        req = PanTiltRequest()
        req.pan = pan
        req.tilt = tilt

        print("Sending service request")
        resp1 = move_head_service(req)
        print("Got service response")
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def set_rotation(roll,pitch,yaw):
    print("Waiting for service")
    service_name = '/avatar/set_rotation'

    rospy.wait_for_service( service_name )
    try:
        set_rotation_service = rospy.ServiceProxy(service_name, AvatarRotation)
        req = AvatarRotationRequest()
        req.rotation.x = roll
        req.rotation.y = pitch
        req.rotation.z = yaw

        print("Sending service request")
        resp1 = set_rotation_service(req)
        print("Got service response")
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# target must be a list of 3 elements or a triple
def start_enablement(name, target, duration=0):
    print("Waiting for service")
    service_name = '/avatar/body_part_manipulation/start_enablement'

    rospy.wait_for_service( service_name )
    try:
        start_enablement_service = rospy.ServiceProxy(service_name, NamedTargetInterpolation)
        req = NamedTargetInterpolationRequest()
        req.name = name
        req.duration = duration
        req.target.x = target[0]
        req.target.y = target[1]
        req.target.z = target[2]

        print("Sending service request")
        resp1 = start_enablement_service(req)
        print("Got service response")
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    
# target must be a list of 3 elements or a triple
def set_interpolation_target(name, target, duration=0):
    print("Waiting for service")
    service_name = '/avatar/body_part_manipulation/set_interpolation_target'

    rospy.wait_for_service( service_name )
    try:
        set_interpolation_target_service = rospy.ServiceProxy(service_name, NamedTargetInterpolation)
        req = NamedTargetInterpolationRequest()
        req.name = name
        req.duration = duration
        req.target.x = target[0]
        req.target.y = target[1]
        req.target.z = target[2]

        print("Sending service request")
        resp1 = set_interpolation_target_service(req)
        print("Got service response")
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    

def start_disablement(name, target, duration=0):
    print("Waiting for service")
    service_name = '/avatar/body_part_manipulation/start_disablement'

    rospy.wait_for_service( service_name )
    try:
        start_enablement_service = rospy.ServiceProxy(service_name, NamedTargetInterpolation)
        req = NamedTargetInterpolationRequest()
        req.name = name
        req.duration = duration
        req.target.x = target[0]
        req.target.y = target[1]
        req.target.z = target[2]

        print("Sending service request")
        resp1 = start_enablement_service(req)
        print("Got service response")
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    
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
    move_to((525,440,97))
    rospy.sleep(3)

    print("Call SetRotation (Rotate to milk box)")
    set_rotation(0,0,180)
    rospy.sleep(1.5)

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

    print("Call SetInterpolationTarget (left hand ik)")
    set_interpolation_target("left_hand_ik",(20,50,90))
    rospy.sleep(3.5)



    print("Call Detach Object")
    send_command("detach_object")
    rospy.sleep(1.5)

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
