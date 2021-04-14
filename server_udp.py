import socket, webbrowser, subprocess
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print('Socket Created')

udp_host = socket.gethostname()	
udp_port = 12345

s.bind((udp_host,udp_port))

print('Waiting for input')

#Accepting the choice from client
b_choice = s.recvfrom(100)
choice=b_choice[0].decode('utf-8')
print("choice : ",choice)

#Excecuting  the choice of program
while choice !=3:          
  if choice == 1:
    webbrowser.open('https://www.google.com/')

  elif choice == 2: 
    subprocess.Popen(["Notepad.exe","testing.txt"])
  s.close()


            
