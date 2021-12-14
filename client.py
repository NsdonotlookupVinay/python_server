from os import error
import socket
import subprocess
import time
subprocess.run('clear', shell= True)
print('''


 .o88b. db      d888888b d88888b d8b   db d888888b 
d8P  Y8 88        `88'   88'     888o  88 `~~88~~' 
8P      88         88    88ooooo 88V8o 88    88    
8b      88         88    88~~~~~ 88 V8o88    88    
Y8b  d8 88booo.   .88.   88.     88  V888    88    
 `Y88P' Y88888P Y888888P Y88888P VP   V8P    YP    
                                                ''')

print ("""
          | | | |  ___  __ _   __ _   ___ 
          | |_| | (_-< / _` | / _` | / -_)
           \___/  /__/ \__,_| \__, | \___|
                              |___/       """)
print("""FOR _
     EXIT                -->  (exit())
     COMMAND             --> (cmd)
          for example -> cmd
     TO CREATE FILE      --> (file)
          for example -> file
     TO TRANSFER FILE    --> ts""")
# HOST = input("[HOST] --> Host to connect > ")
HOST = "127.0.1.1"
PORT = 5050
ADDR = (HOST,PORT)
FORMAT = "utf-8"
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(ADDR)
while True:
     msg = input("[<-] : ")
     if msg == "exit()":
          s.close()
          exit()
     elif 'cmd' in msg:
          # msgc = msg.encode(FORMAT)
          # s.send(msgc)
          # recc = s.recv(1024).decode(FORMAT)
          # print(recc)
          print('[*] Usage --> exit() to exit cmd mode \n[*] You are in cmd mode now')
          while True:
               inputc = input('[<-] CMD ##> ')
               if "exit()" in inputc:
                    print("[*] CMD mode is now off ")
                    break
               else:
                    send = "cmd " + inputc
                    senda = send.encode(FORMAT)
                    s.send(senda)
                    # time.sleep(2)
                    try :
                         recvc = s.recv(1024).decode(FORMAT)
                         print(recvc)
                    except:
                         pass
     elif 'file' in msg :
          print('[*] Usage --> exit() to exit file mode \n[*] You are in file mode now')
          while True:
               inputf  = input('[<-] FILE NAME : ')
               if inputf == "exit()" :
                    print("[*] File mode is now off")
                    break
               inputco = input('[<-] CONTENT   : ')
               # msgf = inputf.encode(FORMAT)
               # msgco = inputco.encode(FORMAT)
               total  = "file " + inputf +" "+ inputco
               totals= total.encode(FORMAT)
               s.send(totals)
               recf = s.recv(1024).decode(FORMAT)
               print(recf)
     elif 'ts' in msg :
          print("[*] Usage --> Just enter file name \nYou are in transfer file mode ")
          while True:
               try:
                    content = ""
                    filen = input('[<-] Enter file name :')
                    if filen == "exit()" :
                         break
                    else:
                         with open(filen , "r") as b:
                              content  = b.read()
                         totals = "file " + filen + " " + content
                         totalse = totals.encode(FORMAT)
                         s.send(totalse)
                         recc = s.recv(1024).decode(FORMAT)
                         print(recc)
               except:
                    print("[*] File not found")
     else:
          print("[->] wrong option ")
