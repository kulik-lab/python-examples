import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 3333
#MESSAGE = b"7"
#i = ['1','2','3','4','5','6','7','8','9','0']
#j = [2,4,6,8,10,12,14,16,18,20,22,24,26]
l1=0x01020304050607ff
l2=1024
l3=4096
l4=0xffffffffffffffff

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
pause=2
for m in range(5):
    sock.sendto(l1.to_bytes(8, byteorder='big'), (UDP_IP, UDP_PORT))
    print(l1,"   ")
    time.sleep(pause)
    sock.sendto(l2.to_bytes(8, byteorder='big'), (UDP_IP, UDP_PORT))
    print(l2,"   ")
    time.sleep(pause)
    sock.sendto(l3.to_bytes(8, byteorder='big'), (UDP_IP, UDP_PORT))
    print(l3,"   ")
    time.sleep(pause)
