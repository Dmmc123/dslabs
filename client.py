from alive_progress import alive_bar
from pathlib import Path
import socket
import sys

# getting the needed arguments to run the program

file_name = sys.argv[1]
ip, port = sys.argv[2], int(sys.argv[3])

# initializing the buffer size

buff = 1024

# connecting to the server machine

s = socket.socket()
s.connect((ip, port))
print("Connected to {}:{}".format(ip, port))

file = open(file_name, "rb")

# sending name of the file to server
# and waiting for a reply as an acknowledgement that 
# file name is recieved

s.send(file_name.encode())    
ack = s.recv(buff)

# if we recieve an acknowledgement then we can start
# running a progress bar and transer the file

if ack.decode() == file_name:
    
    file_size = Path(file_name).stat().st_size
    
    with alive_bar(file_size) as bar:
        
        # reding data of file and sending it as messages
        # until we send the last bit of the file

        msg = file.read(buff)
        while msg:
            s.send(msg)
            msg = file.read(buff)
            
            # moving the bar 
            
            for i in range(buff): bar()
                
# cleaning everything up after file has been transfered
    
print("Sent file {} successfully".format(file_name))
file.close()
s.close()
