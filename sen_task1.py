import socket,time
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)		     

#Asking client for choice of program execution
intro="\nHey! Send a message to server"
print(intro)
msg=input('Enter your message:')
message = msg.encode('utf-8')

#Sending the message to server
c.sendto(message,('localhost',9999))

print("\nMessage sent, wait for reply\n")
time.sleep(1)
rec_reply,addrs= c.recvfrom(100)
data=rec_reply.decode('utf-8')
print(data)
