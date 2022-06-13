from pymavlink import mavutil

#Start a connection listening to a UDP port
conn = mavutil.mavlink_connection('udpin:localhost:14551')

#Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
conn.wait_heartbeat()
print("Heartbeat from system (system %u component %u)"%(conn.target_system, conn.target_component))

#fields conn.target_system and conn.target_component, and command type are automatically filled in when conn receives a heartbeat msg
conn.mav.command_long_send(conn.target_system, conn.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0, 0)
msg = conn.recv_match(type='COMMAND_ACK',blocking=True)
print(msg)