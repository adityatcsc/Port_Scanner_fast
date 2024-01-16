import socket
import sys
import time
import threading


msg ="python3 port_scan_fast.py -t Target -p start_port end_port"

start_time=time.time()
if (len(sys.argv) != 6):
	print("---argument must be---")
	print(msg)
	sys.exit()

try:
    if (sys.argv[1]=="-t"):
      target = socket.gethostbyname(sys.argv[2])
    else:
      print("target must have -t argument")
      sys.exit()
except socket.gaierror:
    print("name resolution error")
    sys.exit()

if (sys.argv[3]=='-p'):
      start_port=int(sys.argv[4])
      end_port=int(sys.argv[5])
else:
      print("for port must have -p argument")
      sys.exit()

def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    connt = s.connect_ex((target,port))
    if (not connt):
    	print("port {} is open".format(port))
    s.close()

for port in range(start_port,end_port+1):

    thread =threading.Thread(target = scan_port,args = (port,))
    thread.start()

end_time=time.time()

print("time taken",end_time-start_time)
