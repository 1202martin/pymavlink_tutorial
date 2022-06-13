from pymavlink import mavutil

#Start a connection listening to a UDP port
conn = mavutil.mavlink_connection('udpin:localhost:14551')

#Wait for the first heartbeat
#   This sets the system and component ID of remote system for the link
conn.wait_heartbeat()
# print("Heartbeat from system (system %u component %u)"%(conn.target_system, conn.target_component))

#Receive all available messages
while True:
    msg = conn.recv_match(blocking=True)
    print("\n", msg)
    print("type: " ,type(msg))