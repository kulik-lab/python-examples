import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 3333

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
pause=.1
data = [10,200,300,500,100,2000,0x01020304050607ff,1024,4096,0xffffffffffffffff,127000,32767]
for i in range(10):
    for d in data:
        sock.sendto(d.to_bytes(8, byteorder='big'), (UDP_IP, UDP_PORT))
        print("sent:   ", d)
        time.sleep(pause)
