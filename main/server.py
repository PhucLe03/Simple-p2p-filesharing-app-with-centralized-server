from tkinter import *
import socket
from tkinter import filedialog 
from tkinter import messagebox 
from tkinter import scrolledtext
import os
import threading
import time
import select
import _thread
from functools import partial

FILESIZE = 40960000
WINDOWSIZESTRING = "450x560+500+200"

root = Tk()
root.title("FILE TRANSFER SERVER")
root.geometry(WINDOWSIZESTRING)
root.configure(bg= "#f4fdfe")
root.resizable(False,False)


image_icon=PhotoImage(file="Image/app_icon.png")
root.iconphoto(False,image_icon)

Label(root, text="Server",font = ('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
Frame(root, width=400,height=2,bg="#f3f5f6").place(x=20,y=200)

box=scrolledtext.ScrolledText(root,width=49,height=16)
box.place(x=20, y=200)


IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
SIZE = 40960000
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"


connlist = []
addrlist = []
# filelist = []

def handle_client(conn, addr):
    connlist.append((conn,[])) # add socket to client's list
    addrlist.append(addr) # add address to client's list
    # filelist.append(['f'])
    # print(filelist)
    res = f"[NEW CONNECTION] {addr} connected.\n"

    conn.send("OK@Welcome to the File Server!".encode(FORMAT))
    print(res)
    
    box.insert(INSERT, res)
    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]
        
        if cmd == "MESSAGE":
            message = f"[MESSAGE] {conn.getpeername()} {data[1]}"
            box.insert(INSERT, message)
            print(message)
        elif cmd == "PUBLISH":
            # ip = conn.getpeername()[0]
            # port = conn.getpeername()[1]
            filename = data[1]
            if (filename==""):
                continue
            for c in connlist:
                if (c[0]==conn):
                    c[1].append(filename)
        elif cmd == "DOWNLOAD":
            msg = data[1]
            peer = conn.getpeername()[0]
            port = conn.getpeername()[1]
            # send request to other clients
            filename = msg
            for c in connlist:
                if (c[0]!=conn):
                    # c.send("OK@He wants to download".encode(FORMAT))
                    send_msg = f"DOWNLOAD@{filename};{peer};{port}"
                    print(send_msg)
                    c[0].send(send_msg.encode(FORMAT))

        elif cmd == "LOGOUT":
            connlist.remove(conn)
            addrlist.remove(addr)
            break

    print(f"[DISCONNECTED] {addr} disconnected")
    
    conn.close()

def printList(list, show):
    for elem in list:
        show.insert(END, "Client:" , f"{elem[0]}:{elem[1]}")


def is_valid_input(input):
    try:
        ip, port = input.split(":")
        return True
    except:
        return False

def Ping(ip_var):
    # for c in connlist:
    #     print(c.getpeername())
    input = ip_var.get()
    
    if input == "":
        messagebox.showinfo("Warning", "Fields cannot be empty")
        # print("Fields cannot be empty")    
    else:
        if is_valid_input(input):
            ip, port = input.split(':')
            result = False
            for addr in addrlist:
                if ip == addr[0] and port == str(addr[1]):
                    result = True
                    print("Address is valid")
                    messagebox.showinfo("ACTIVED", "This client is currently connected")
                    return
            if (result==False):
                messagebox.showinfo("Warning", "Address is not valid")
                    # print("Address is not valid")
                        
        else:
            messagebox.showerror("ERROR", "Syntax error")
            
            

def ClientList():
    window=Toplevel(root)
    window.title("CLIENT STATUS")
    window.geometry(WINDOWSIZESTRING)
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)
    
    Label(window, text="The connected clients\' list",font = ('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
    Frame(window, width=400,height=2,bg="#f3f5f6").place(x=20,y=200)
    
    show_clientList = Listbox(window,width=100,height=50)
    show_clientList.place(x = 0, y = 210)
    
    printList(addrlist,show_clientList)
    
    dis_ip_var = StringVar()
    ping_ip_var = StringVar()
    
    discover_label=Label(window,text="Enter IP:PORT to discover").place(x=210, y = 100)
    discover_ip=Entry(window,textvariable=dis_ip_var, width=30, bd=4).place(x=210, y=120)
    discover=Button(window,text="Discover",font=('Acumin Variable Concept',17,'bold') ,bg="#f4fdfe", width=10, height=1, command=lambda: Discover(dis_ip_var))
    discover.place(x=50,y=100)
    
    ping_label=Label(window,text="Enter IP:PORT to ping").place(x=210, y = 150)
    ping_ip=Entry(window,textvariable=ping_ip_var, width=30, bd=4).place(x=210, y=170)
    ping=Button(window,text="Ping",font=('Acumin Variable Concept',17,'bold') ,bg="#f4fdfe", width=10, height=1, command=lambda: Ping(ping_ip_var))
    ping.place(x=50,y=150)
    
    
    def Discover(ip_var): #input var
        input = ip_var.get()
        
        if input == "":
            messagebox.showinfo("Warning", "Fields cannot be empty")
            # print("Fields cannot be empty")    
        else:
            if is_valid_input(input):
                ip, port = input.split(':')
                result = False
                # for addr in addrlist:
                for c in connlist:
                    pe = c[0].getpeername()[0]
                    po = c[0].getpeername()[1]
                    if ip == pe and port == str(po):
                        result = True
                        
                        wd=Toplevel(window)
                        wd.title("DISCOVER")
                        wd.geometry(WINDOWSIZESTRING)
                        wd.configure(bg="#f4fdfe")
                        wd.resizable(False,False)
                    
                        Label(wd, text="List of sharing files",font = ('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
                        # Frame(wd, width=400,height=2,bg="#f3f5f6").place(x=20,y=200)
                        
                        show_fileList = Listbox(wd,width=100,height=50)
                        show_fileList.place(x = 0, y = 100)
                        for f in c[1]:
                            show_fileList.insert(END, f)
                        # printList(fileList, show_fileList)
                        
                        
                        
                        wd.mainloop()
                        return
                    # else:
                if (result==False):
                    messagebox.showinfo("Warning", "Address is not valid")
                    print("Address is not valid")
                            
            else:
                messagebox.showerror("ERROR", "Syntax error")
    
    
    
    window.mainloop()


def Server():
    res = f"[STARTING] Server is starting"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    res = res + f"\n[LISTENING] Server is listening on {IP}:{PORT}.\n" + "Waiting for connection...\n"
    # print(res)
    box.insert(INSERT, res)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        msg = f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}\n"
        box.insert(INSERT, msg)
        print(msg)
    
    
# thread = threading.Thread(target=Server)
def ServerThread():
    _thread.start_new_thread(Server, ())

def Stop():
    # run = False
    # running = False
    exit()

root.protocol("WM_DELETE_WINDOW", Stop)


def startClientList():
    _thread.start_new_thread(ClientList, ())

start=Button(root,text="Start Server",font=('Acumin Variable Concept',17,'bold') ,bg="#f4fdfe", command=ServerThread)
start.place(x=50,y=100)

clist=Button(root,text="Client List",font=('Acumin Variable Concept',17,'bold') ,bg="#f4fdfe", command=startClientList)
clist.place(x=250,y=100)

# background=PhotoImage(file="Image/background.png")



root.mainloop()