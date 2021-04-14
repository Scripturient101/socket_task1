import socket,time,random
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('Socket Created')

reply_list=['Hey to you too','How can I help you?','What?','Do not bother me','Hey Buddy','You again?','You talking to me?']

s.bind(('localhost',9999))
print('Waiting for input')

#Accepting the msg from client
while True:
    rec_msg= s.recvfrom(100)
    msg=rec_msg[0].decode('utf-8')
    print("\nMessage sent from user: ",msg)


    ran = random.choice(reply_list)
    data=ran.encode('utf-8')
    print("\nSending this message to client:",ran)
    s.sendto(data,('localhost',9999))
    s.close()
