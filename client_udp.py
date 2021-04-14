import socket,time
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host = socket.gethostname()		
udp_port = 12345			     

#Asking client for choice of program execution
menu ="\nEnter 1 to google \nEnter 2 to open notepad \nEnter 3 to exit"
print(menu)
choice=input('\nEnter your option:')
b_choice = choice.encode('utf-8')
print("choice in bytes:",b_choice)

#Sending the choice to server
c.sendto((b_choice),(udp_host,udp_port))
