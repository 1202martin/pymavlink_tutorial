from pymavlink import mavutil
import time

#Start a connection listening to a UDP port
conn = mavutil.mavlink_connection('udpin:localhost:14551')

#Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
conn.wait_heartbeat()
# print("Heartbeat from system (system %u component %u)"%(conn.target_system, conn.target_component))
print("Heartbeat from system (system %u component %u)"%(conn.target_system, conn.target_component))

#first arm the copter to be capable for takeoff
conn.mav.command_long_send(conn.target_system, conn.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0, 0)
msg = conn.recv_match(type='COMMAND_ACK',blocking=True)
print(msg)
time.sleep(1)

#send the takeoff packet to the copter
## There may be slight differences between packet format between those defined in pymavlink.mavutil and those defined in ardupilot.
## Double check if they are correspondant just to be safe.
conn.mav.run_cmd(conn.target_system, conn.target_component, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 
                            0, 0, 0, 0, 0, 0, 0, 0, 10)

#receive and print ack packet from the copter
msg = conn.recv_match(type='COMMAND_ACK',blocking=True)
print(msg)