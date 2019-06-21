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

def send_console_command(comm):
    print("Waiting for service")
    service_name = '/avatar/send_console_command'

    rospy.wait_for_service( service_name )
    try:
        send_console_command_service = rospy.ServiceProxy(service_name, Command)
        req = CommandRequest()
        req.command = comm

        print("Sending service request")
        resp1 = send_console_command_service(req)
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
