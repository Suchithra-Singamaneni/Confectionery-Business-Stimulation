from tkinter import * 
from tkinter import ttk 
from socket import * 
import base64 
import os 
from stat import * 
from PIL import Image, ImageTk 
clientSocket = socket(AF_INET, SOCK_STREAM) 
flag = 0 
path = "C:\\jupyter\\"

def BClick(event):
    name = textfield1.get()
    email = textfield2.get()
    window.destroy()
    win=Tk()
    
    image2 = Image.open("C:\\jupyter\\model.png") 
    photo2 = ImageTk.PhotoImage(image2) 
    label2 = Label(win,image=photo2) 
    label2.image = photo2 
    label2.pack() 
    
    L4=Label(win, text=" Choco Rush! ", fg='navajo white', font=("Verdana", 23, "bold"),bg='brown4') 
    L4.place(x=335, y=90) 
    T = Text(win, height=12, width=30, bd=5, padx=50, fg='brown4', font=("Calibri", 13, "bold")) 
    T.place(x=290, y=220) 
 
    image3 = Image.open("C:\\jupyter\\logo.png")
    photo3 = ImageTk.PhotoImage(image3)
    BB=Button(win, image = photo3, height=170, width=170)
    BB.place(x=645, y=15) 
    textfield3=Entry(win, text="This is Entry Widget", width=30, bd=5) 
    textfield3.place(x=340, y=530)
    serverName = "127.0.0.1" 
    serverPort = 3001 
    clientSocket.connect((serverName, serverPort)) 
    print("Connected.") 
    T.insert(END,"\nHi "+name+"!") 
        
    def selected(var): #command to server sending function for all buttons 
        T.delete(1.0,END) 
        if(var==4): 
            temp="Money.txt" 
            fp=open("C:\\jupyter\\Orders\\"+temp,'w') 
            msg=textfield3.get() 
            fp.write(msg) 
            msg=str(var)+temp+">"+msg 
        elif(var==9): 
            msg=str(var)+email 
        elif(var==10): 
             msg="." 
        else: 
             msg=str(var)+textfield3.get() 
        msg_bytes = msg.encode('ascii') 
        base64_bytes = base64.b64encode(msg_bytes) 
        clientSocket.send(base64_bytes)
        
        response = clientSocket.recv(1024) 
        if(var==3): 
            temp="Bill.txt" 
            fp1=open("C:\\jupyter\\Orders\\"+temp,'w')
            fp1.write(str(response)) 
            T.insert(END, response)
            textfield3.delete(0,END) 
            global flag #flag stores the button number pressed or 0 
            flag=0

        #FOR MENU
        if(var==0):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag = 0
        if(var==1):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag = 0
        if(var==2):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag = 0
        if(var==4):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag = 0
        if(var==5):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag = 0
        if(var==6):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag = 0
        if(var==7):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag=0
        if(var==8):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag=0
        if(var==9):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag=0
        
        if(var==10):
            T.insert(END,response)
            textfield3.delete(0,END)
            flag=0

     
    def selected1(): 
        selected(1) 
    def selected2(): 
        T.delete(1.0,END) 
        T.insert(END, "\n\nPlease enter your order!") 
        global flag 
        flag=2
            
    def selected3(): 
        selected(3)
            
    def selected4(): 
        T.delete(1.0,END) 
        T.insert(END, "\n\nPlease enter the amount!") 
        global flag 
        flag=4

    def selected5(): 
        T.delete(1.0,END) 
        T.insert(END, "\n\nPlease enter the order to be cancelled!") 
        global flag 
        flag=5
            
    def selected6(): 
        T.delete(1.0,END) 
        T.insert(END, "\n\nPlease enter \"Old order>New order\"")
        global flag 
        flag=6
            
    def selected7(): 
        selected(7) 
            
    def selected8(): 
        selected(8) 

    def selected9(): 
        selected(9) 
 
    def selected10(): 
        T.delete(1.0,END) 
        T.insert(END, "\n\nPlease enter your house number(1/2/3/4)? :") 
        global flag 
        flag=10 
 
    def exit(): 
        win.destroy() 
        global path 
        os.chmod( path+"Orders\\Bill.txt", S_IWRITE ) 
        os.remove(path+"Orders\\Bill.txt")
                
    def okay(): 
        global flag 
        T.delete(1.0,END) 
        selected(flag)
            
        
    B1 = Button(win, text="Confectionery", command=selected1, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
        #list directories and files 
    B1.place(x=50,y=100)
        
    B2 = Button(win, text="Place Order ", command=selected2, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
        #make a directory 
    B2.place(x=50,y=150)
        
    B3 = Button(win, text="Bill ", command=selected3, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
        #download a file 
    B3.place(x=50,y=200)
     
    B4 = Button(win, text="Payment ", command=selected4, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
        #upload a file 
    B4.place(x=50,y=250)
        
    B5 = Button(win, text="Cancel order ", command=selected5, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
        #delete a directory 
    B5.place(x=50,y=300)
        
    B6 = Button(win, text="Edit order ", command=selected6, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
    #rename a directory 
    B6.place(x=50,y=350)
        
    B7 = Button(win, text="Order details", command=selected7, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
    #get modified time details #single slash 
    B7.place(x=50,y=400)
        
    B8 = Button(win, text="Order Status", command=selected8, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
        #check if a file is executable 
    B8.place(x=50,y=450)
        
    B9 = Button(win, text="Confirm Order", command=selected9, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
    #make a file read-only 
    B9.place(x=50,y=500) 
    
    B10 = Button(win, text="House no.", command=selected10, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
        #take address for LS algo routing 
    B10.place(x=50,y=550)
        
    B11 = Button(win, text="QUIT", command=exit, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
    #Close GUI and socket 
    B11.place(x=750,y=560)
        
    B12 = Button(win, text="OKAY", command=okay, fg='brown4', bg='navajo white', font=("Verdana", 13, "bold"), activebackground='brown4', activeforeground='navajo white') 
    #For entering details 
    B12.place(x=550,y=525) 
        
    win.title('Choco Rush') 
    win.geometry("850x620+10+20") 
    win.mainloop() 
        
     
window=Tk()

image1 = Image.open("C:\\jupyter\\model.png") 
photo1 = ImageTk.PhotoImage(image1) 
label1 = Label(window,image=photo1) 
label1.image = photo1 
label1.pack()
    
    
L1=Label(window, text="Welcome to Choco rush!", fg='white', font=("Verdana", 23, "bold"),bg='brown4') 
L1.place(x=220, y=70)
    
L2=Label(window, text="Username: ", fg='brown4', font=("Verdana", 10, "bold"), bg='navajo white') 
L2.place(x=280, y=340) 
    
L3=Label(window, text="Email: ", fg='brown4', font=("Verdana", 10, "bold"), bg='navajo white') 
L3.place(x=310, y=400)
    
btn=Button(window, text="Login", fg='black', font=("Verdana", 10, "bold"), height=1, width=10, bd=5) 
btn.place(x=410, y=460) 
btn.bind('<Button-1>', BClick) 
    
textfield1=Entry(window, text="Username", width=30, bd=5) 
textfield1.place(x=370, y=340) 
    
textfield2=Entry(window, text="Email", width=30, bd=5) 
textfield2.place(x=370, y=400)
    
window.title('Choco rush') 
window.geometry("850x620+10+20") 
window.mainloop() 
    
    
