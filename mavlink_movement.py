#File describing how to send movement commands to drones with pymavlink
from pymavlink import mavutil

#Start a connection listening to a UDP port
conn = mavutil.mavlink_connection('udpin:localhost:14551')

#Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
conn.wait_heartbeat()
print("Heartbeat from system (system %u component %u)"%(conn.target_system, conn.target_component))


######send to a target localtion

#set_position_target_local_ned
# type_mask = int(0x0DF8)

# To enable each placeholder bits, set the bits to 0; to disable, set the bits to 1.
# bits in the type mask are ordered in reverse; least significant bits are to the left, moving towards the right.
# ** yaw : angle at which the copter will be facing
# ** yaw_rate : velocity at which the copter will be rotating
# type_mask = int(0b100111111000)


# conn.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, conn.target_system, conn.target_component,
#         mavutil.mavlink.MAV_FRAME_LOCAL_NED, type_mask, 60, 0, -10, 0, 0, 0, 0, 0, 0, 1.57, 0))

# while True:
#     # msg = conn.recv_match(type='NAV_CONTROLLER_OUTPUT', blocking=True)
#     # print(msg)

#     msg = conn.recv_match(type='LOCAL_POSITION_NED', blocking=True)
#     print(msg)

#set_posi8tion_taget_global_ned
type_mask = int(0b110111111000)


conn.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, conn.target_system, conn.target_component,
        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, type_mask, int(-35.3629552*10**7), int(149.1650480*10**7), 10, 0, 0, 0, 0, 0, 0, 0, 0))

while True:
    # msg = conn.recv_match(type='NAV_CONTROLLER_OUTPUT', blocking=True)
    # print(msg)

    msg = conn.recv_match(type='LOCAL_POSITION_NED', blocking=True)
    print(msg)