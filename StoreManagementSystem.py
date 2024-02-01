
###importing all necessary modules
import pkg_resources.py2_warn
from win32api import GetSystemMetrics as gm
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Treeview
from tkinter import ttk 
from PIL import Image, ImageTk
from database import * #self made module
from datetime import datetime
from qrc import * #self made module
from tkinter import messagebox as ms
from classes import * #self made module
import random
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import pyttsx3




#=================================GUI CONFIGURATION============================




global h,w
h = gm(1)-50
w = gm(0)
root = Tk()
root.title(f"STORE MANAGEMENT SYSTEM")
root.iconbitmap("mainicon1.ico")
root.geometry(f"{w}x{h}")
root.state('zoomed')
root.minsize(w,h)
root.maxsize(w,h)



#====================functions==========================



def CloseBt(screen,x,y,desScreen):
    Button(screen,text = "Close",bd = 2,command = desScreen.destroy,relief = GROOVE,font = "timesewroman 12 bold",bg = "red",fg = "yellow",activebackground = "#3B3131",  padx = 8 ).place(relx = x, rely = y)

def speak(audio):
    #setting voice
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()



"""ADMIN PAGE FUNCTIONS"""

#menuBar functions



def makeadmin():

    #frame
    fr = Frame(admin, bg = "black" )
    fr.place(height = h , width = w , relx = 0, rely = 0)
    fr3 = LabelFrame(fr, text = "Add Admin", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,foreground = "yellow",bg = "#151b54", highlightbackground = "silver")
    fr4 = LabelFrame(fr, text = "Select And Update", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    fr5 = LabelFrame(fr, text = "Remove Admin", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    
    Label(fr, text = "STORE MANAGEMENT SYSTEM : MANAGE ADMIN ",padx = 40,pady =5, font = "CooperBlack 20 bold",bd = 8, relief = GROOVE,  fg = 'black', bg = "#d3d3d3").pack(fill = BOTH)

    fr3.place(height =355 , width =530 ,relx = 0.006,rely =0.539)
    fr4.place(height =355 ,width =530 ,relx =0.338 ,rely =0.539 )
    fr5.place(height =355 ,width =530 ,relx =0.669 ,rely =0.539 )

    #treeview  
    #treeframe
    treeframe = Frame(fr,bd = 5, relief = GROOVE)
    treeframe.place(height = 380,width = w-18,relx = 0.005,rely = 0.078) 
    atree = Treeview(treeframe, height = 20)
    atree['columns'] = ("User Id",'Password','Name','Phone','Email Id')

    #format
    atree.column("#0",width = 0,stretch = NO)
    atree.column("User Id",width =120,anchor = CENTER) 
    atree.column("Password",width = 120,anchor = CENTER)
    atree.column("Name",width = 120, anchor = CENTER)
    atree.column("Phone",width = 120,anchor = CENTER)
    atree.column("Email Id",width = 120,anchor = CENTER)

    #heading
    atree.heading("#0", text = "",anchor = W)
    atree.heading("User Id", text = "UserId", anchor = CENTER)
    atree.heading("Password", text = "Password", anchor = CENTER)    
    atree.heading("Name", text = "Name", anchor = CENTER)
    atree.heading("Phone", text = "Phone", anchor = CENTER)
    atree.heading("Email Id", text = "Email Id", anchor = CENTER)
    atree.place(height = 400,width = w-12)
    #EntryInTable
    
    counter1 = 0
    for i in sqlAccess(cur.execute("select * from ADMIN;")):
        atree.insert(parent = '',index = END, iid= counter1, values = i)
        counter1+=1
  
    #scroll bar
    treescroll = Scrollbar(treeframe)
    treescroll.pack(side = RIGHT, fill = Y)
    atree.config(yscrollcommand = treescroll.set)
    treescroll.config(command = atree.yview)

    #entry boxes 1
    Name = StringVar()
    Password = StringVar()
    Mail = StringVar()
    Phone = StringVar()
    UserId = StringVar()


    #class calling in function 
    def cl_addadmin():

        AddAdmin = Administrator(Name.get(),UserId.get(),Password.get(),Mail.get(),Phone.get())
        AddAdmin.add_admin()
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from ADMIN;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1
            


    e1 = Entry(fr3,textvariable =Name,font = "timesnewroman 12", width = 20, bd = 4)
    l1 = Label(fr3, text = "Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e2 = Entry(fr3,textvariable =UserId,font = "timesnewroman 12", width = 20, bd = 4)
    l2 = Label(fr3, text = "User Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e3 = Entry(fr3,textvariable =Password,font = "timesnewroman 12", width = 20, bd = 4)
    l3 = Label(fr3, text = "Password :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e4 = Entry(fr3,textvariable =Phone,font = "timesnewroman 12", width = 20, bd = 4)
    l4 = Label(fr3, text = "Phone No :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e5 = Entry(fr3,textvariable =Mail,font = "timesnewroman 12", width = 20, bd = 4)
    l5 = Label(fr3, text = "Email Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")

    e1.place(relx =0.5 ,rely =0.075 )
    e2.place(relx =0.5 ,rely =0.23 )
    e3.place(relx =0.5 ,rely =0.38)
    e4.place(relx =0.5 ,rely =0.52 )
    e5.place(relx =0.5 ,rely =0.66 )

    l1.place(relx =0.1 ,rely =0.075 )
    l2.place(relx =0.1 ,rely =0.23 )
    l3.place(relx =0.1 ,rely =0.38)
    l4.place(relx =0.1 ,rely =0.52 )
    l5.place(relx =0.1 ,rely =0.66 )


    #Entry Boxes 2
    Name1 = StringVar()
    Password1 = StringVar()
    Mail1 = StringVar()
    Phone1 = StringVar()
    UserId1 = StringVar()

    
    e6 = Entry(fr4,textvariable =Name1,font = "timesnewroman 12", width = 20, bd = 4)
    l6 = Label(fr4, text = "Update Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e7 = Entry(fr4,state = DISABLED,textvariable =UserId1,font = "timesnewroman 12",background = "#2c3539",fg = "white", width = 20, bd = 4)
    l7 = Label(fr4, text = "User Id* :", font = "timesnewroman 14 bold" ,  fg = 'RED', bg = "#151b54")
    e8 = Entry(fr4,textvariable =Password1,font = "timesnewroman 12", width = 20, bd = 4)
    l8 = Label(fr4, text = "Change Password :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e9 = Entry(fr4,textvariable =Phone1,font = "timesnewroman 12", width = 20, bd = 4)
    l9 = Label(fr4, text = "Update Phone No :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e10 = Entry(fr4,textvariable =Mail1,font = "timesnewroman 12", width = 20, bd = 4)
    l10 = Label(fr4, text = "Update Email Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e6.place(relx =0.5 ,rely =0.075 )
    e7.place(relx =0.5 ,rely =0.23 )
    e8.place(relx =0.5 ,rely =0.38 )
    e9.place(relx =0.5 ,rely =0.52 )
    e10.place(relx =0.5 ,rely =0.66 )

    l6.place(relx =0.1 ,rely =0.075 )
    l7.place(relx =0.1 ,rely =0.23 )
    l8.place(relx =0.1 ,rely =0.38)
    l9.place(relx =0.1 ,rely =0.52 )
    l10.place(relx =0.1 ,rely =0.66 )
    
    #Delete Selected
    delt = StringVar()
    l11 = Label(fr5, text = "REMOVE ADMIN by  User Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    l11.place(relx =0.25,rely = 0.19)
    e11 = Entry(fr5,state = DISABLED,textvariable =delt,background = "#2c3539",fg = "white",font = "timesnewroman 16", width = 20, bd = 4)
    e11.place(relx =0.27 ,rely =0.32 )




    #================FUNCTIONS IN EMPLOYEE===================


    
    def clicked1(event):
        global value3
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        selected3 = atree.focus()
        value3 = atree.item(selected3,'values') 
        e6.insert(0,value3[2])
        UserId1.set(value3[0])
        e8.insert(0,value3[1])
        e9.insert(0,value3[3])
        e10.insert(0,value3[4])
        delt.set(value3[0])  

    def cl_updtadmin():

        UpdateAdmin = Administrator(Name1.get(),UserId1.get(),Password1.get(),Mail1.get(),Phone1.get())
        UpdateAdmin.update_admin()    
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from ADMIN;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1 

        
    def cl_removeadmin():
        if len(sqlAccess(cur.execute("SELECT * FROM ADMIN;"))) >=2:
            try:    
                sqlInsert(cur.execute("DELETE FROM ADMIN WHERE ID = ?",(delt.get(),)))
                ms.showinfo("Successful","Data deleted successfully")
            except Exception as e:
                ms.showinfo("Failed",e)
            atree.delete(*atree.get_children())
            counter1 = 0
            for i in sqlAccess(cur.execute("select * from ADMIN;")):
                atree.insert(parent = '',index = END, iid= counter1, values = i)
                counter1+=1
        else:
            ms.showinfo("CANNOT REMOVE","YOU CANNOT REMOVE THE LAST ADMIN!")


    atree.bind("<Double-1>",clicked1)







    #buttons
    c3 = Button(fr3,text = "Add Admin",bd = 2,command = cl_addadmin,relief =GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
    c4 = Button(fr4,text = "Update Admin",bd = 2,command = cl_updtadmin,relief = GROOVE,font = "timesewroman 14 bold",bg = "white", activebackground = "#3B3131",  padx = 10 )
    c5 = Button(fr5,text = "Remove Admin",bd = 2,command =cl_removeadmin,relief = GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )    
    c6 = Button(fr5,text = "Close",bd = 2,command = fr.destroy,relief = GROOVE,font = "timesewroman 14 bold",bg = "red",fg = "yellow",activebackground = "#3B3131",  padx = 10 )    
    c3.place(relx = 0.3,  rely = 0.85)
    c4.place(relx = 0.3 ,rely =0.85)
    c5.place(relx = 0.34,rely =0.65 )
    c6.place(relx = 0.42,rely =0.85 )    
   
def supplier():

    #frame
    fr = Frame(admin, bg = "black" )
    fr.place(height = h , width = w , relx = 0, rely = 0)
    fr3 = LabelFrame(fr, text = "Add Supplier", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,foreground = "yellow",bg = "#151b54", highlightbackground = "silver")
    fr4 = LabelFrame(fr, text = "Select And Update", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    fr5 = LabelFrame(fr, text = "Remove Supplier", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    
    Label(fr, text = "STORE MANAGEMENT SYSTEM : MANAGE SUPPLIER ",padx = 40,pady =5, font = "CooperBlack 20 bold",bd = 8, relief = GROOVE,  fg = 'black', bg = "#d3d3d3").pack(fill = BOTH)

    fr3.place(height =355 , width =530 ,relx = 0.006,rely =0.539)
    fr4.place(height =355 ,width =530 ,relx =0.338 ,rely =0.539 )
    fr5.place(height =355 ,width =530 ,relx =0.669 ,rely =0.539 )



    #treeview  
    #treeframe
    treeframe = Frame(fr,bd = 5, relief = GROOVE)
    treeframe.place(height = 380,width = w-18,relx = 0.005,rely = 0.078) 
    atree = Treeview(treeframe, height = 20)
    atree['columns'] = ('Name', 'Supplier of', 'Address','Phone',"Email Id","Default Supplier")

    #format
    atree.column("#0",width = 0,stretch = NO)
    atree.column("Name",width = 120, anchor = CENTER)
    atree.column("Supplier of",width = 70,anchor = CENTER)
    atree.column("Address",width = 120,anchor = CENTER)
    atree.column("Phone",width =60,anchor = CENTER) 
    atree.column("Email Id",width = 120,anchor = CENTER)
    atree.column("Default Supplier",width = 20,anchor = CENTER)

    #heading
    atree.heading("#0", text = "",anchor = W)
    atree.heading("Name", text = "Name", anchor = CENTER)
    atree.heading("Supplier of", text = "Supplier of", anchor = CENTER)
    atree.heading("Address", text = "Address", anchor = CENTER)
    atree.heading("Phone", text = "Phone", anchor = CENTER)
    atree.heading("Email Id", text = "Email Id", anchor = CENTER)
    atree.heading("Default Supplier", text = "Default Supplier(Y/N)", anchor = CENTER)
    atree.place(height = 400,width = w-12)
    #EntryInTable
    
    counter1 = 0
    for i in sqlAccess(cur.execute("select * from SUPPLIER;")):
        atree.insert(parent = '',index = END, iid= counter1, values = i)
        counter1+=1
  
    #scroll bar
    treescroll = Scrollbar(treeframe)
    treescroll.pack(side = RIGHT, fill = Y)
    atree.config(yscrollcommand = treescroll.set)
    treescroll.config(command = atree.yview)

    #entry boxes 1
    Name2 = StringVar()
    Address2 = StringVar()
    Mail2 = StringVar()
    Phone2 = StringVar()
    Supp2 = StringVar()
    Defau2 = StringVar()

    def cl_addsupp():
        AddSupplier = Supplier(Name2.get(),Supp2.get(),Address2.get(),Phone2.get(),Mail2.get(),Defau2.get())
        AddSupplier.add_supplier()
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from SUPPLIER;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1      

    e1 = Entry(fr3,textvariable =Name2,font = "timesnewroman 12", width = 20, bd = 4)
    l1 = Label(fr3, text = "Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e2 = Entry(fr3,textvariable =Supp2,font = "timesnewroman 12", width = 20, bd = 4)
    l2 = Label(fr3, text = "Supplier of:", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e3 = Entry(fr3,textvariable =Address2,font = "timesnewroman 12", width = 20, bd = 4)
    l3 = Label(fr3, text = "Address :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e4 = Entry(fr3,textvariable =Phone2,font = "timesnewroman 12", width = 20, bd = 4)
    l4 = Label(fr3, text = "Phone No :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e5 = Entry(fr3,textvariable =Mail2,font = "timesnewroman 12", width = 20, bd = 4)
    l5 = Label(fr3, text = "Email Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e11 = Entry(fr3,textvariable =Defau2,font = "timesnewroman 12", width = 20, bd = 4)
    l11 = Label(fr3, text = "Default Supplier(Y/N):", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")

    e1.place(relx =0.5 ,rely =0.07 )
    e2.place(relx =0.5 ,rely =0.225 )
    e3.place(relx =0.5 ,rely =0.375)
    e4.place(relx =0.5 ,rely =0.515 )
    e5.place(relx =0.5 ,rely =0.655 )
    e11.place(relx =0.5 ,rely =0.795 )

    l1.place(relx =0.1 ,rely =0.07 )
    l2.place(relx =0.1 ,rely =0.225 )
    l3.place(relx =0.1 ,rely =0.375)
    l4.place(relx =0.1 ,rely =0.515 )
    l5.place(relx =0.1 ,rely =0.655 )
    l11.place(relx =0.1 ,rely =0.795 )

    #Entry Boxes 2
    Name3 = StringVar()
    Address3 = StringVar()
    Mail3 = StringVar()
    Phone3 = StringVar()
    Supp3 = StringVar()
    Defau3 = StringVar()



    e6 = Entry(fr4,textvariable =Name3,state = DISABLED,background = "#2c3539",fg = "white",font = "timesnewroman 12", width = 20, bd = 4)
    l6 = Label(fr4, text = "Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e7 = Entry(fr4,textvariable =Supp3,font = "timesnewroman 12", width = 20, bd = 4)
    l7 = Label(fr4, text = "Change Supplier of :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e8 = Entry(fr4,textvariable =Address3,font = "timesnewroman 12", width = 20, bd = 4)
    l8 = Label(fr4, text = "Change Address :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e9 = Entry(fr4,textvariable =Phone3,font = "timesnewroman 12", width = 20, bd = 4)
    l9 = Label(fr4, text = "Update Phone No :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e10 = Entry(fr4,textvariable =Mail3,font = "timesnewroman 12", width = 20, bd = 4)
    l10 = Label(fr4, text = "Update Email Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e12 = Entry(fr4,textvariable =Defau3,font = "timesnewroman 12", width = 20, bd = 4)
    l12 = Label(fr4, text = "Default Supplier(Y/N):", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")

    e6.place(relx =0.5 ,rely =0.07 )
    e7.place(relx =0.5 ,rely =0.225 )
    e8.place(relx =0.5 ,rely =0.375)
    e9.place(relx =0.5 ,rely =0.515 )
    e10.place(relx =0.5 ,rely =0.655 )
    e12.place(relx =0.5 ,rely =0.795 )

    l6.place(relx =0.1 ,rely =0.07 )
    l7.place(relx =0.1 ,rely =0.225 )
    l8.place(relx =0.1 ,rely =0.375)
    l9.place(relx =0.1 ,rely =0.515 )
    l10.place(relx =0.1 ,rely =0.655 )
    l12.place(relx =0.1 ,rely =0.795 )

    #Delete Selected
    delt1 = StringVar()
    l11 = Label(fr5, text = "REMOVE Supplier By Selecting:", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    l11.place(relx =0.23,rely = 0.19)
    e11 = Entry(fr5,state = DISABLED,textvariable =delt1,background = "#2c3539",fg = "white",font = "timesnewroman 16 bold", width = 20, bd = 4)
    e11.place(relx =0.29 ,rely =0.32 )





    #================FUNCTIONS IN EMPLOYEE===================


    
    def clicked1(event):
        global value2
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e12.delete(0,END)
        e11.delete(0,END)
        selected2 = atree.focus()
        value2 = atree.item(selected2,'values') 
        Name3.set(value2[0])
        e7.insert(0,value2[1])
        e8.insert(0,value2[2])
        e9.insert(0,value2[3])
        e10.insert(0,value2[4])
        e12.insert(0,value2[5])
        delt1.set(value2[0])  

    def cl_updtsupp():
        UpdateSupplier = Supplier(value2[0],Supp3.get(),Address3.get(),Phone3.get(),Mail3.get(),Defau3.get())
        UpdateSupplier.update_supplier() 
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from SUPPLIER;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1 

        
    def cl_removesupp():
        sqlInsert(cur.execute("DELETE FROM SUPPLIER WHERE NAME = ?",(value2[0],)))
        ms.showinfo("Removed","Supplier Removed!")
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from SUPPLIER;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1 

    atree.bind("<Double-1>",clicked1)



    #buttons
    c3 = Button(fr3,text = "Add Supplier",bd = 2,command = cl_addsupp,relief =GROOVE,font = "timesewroman 13 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
    c4 = Button(fr4,text = "Update Supplier",bd = 2,command = cl_updtsupp,relief = GROOVE,font = "timesewroman 13 bold",bg = "white", activebackground = "#3B3131",  padx = 10 )
    c5 = Button(fr5,text = "Remove Supplier",bd = 2,command = cl_removesupp,relief = GROOVE,font = "timesewroman 13 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )    
    c6 = Button(fr5,text = "Close",bd = 2,command = fr.destroy,relief = GROOVE,font = "timesewroman 13 bold",bg = "red",fg = "yellow",activebackground = "#3B3131",  padx = 10 )    
    c3.place(relx = 0.3,  rely = 0.89)
    c4.place(relx = 0.3 ,rely =0.89)
    c5.place(relx = 0.34,rely =0.65 )
    c6.place(relx = 0.42,rely =0.85 )

def editemployee():

    #frame
    fr = Frame(admin, bg = "black" )
    fr.place(height = h , width = w , relx = 0, rely = 0)
    fr3 = LabelFrame(fr, text = "Add Employee", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,foreground = "yellow",bg = "#151b54", highlightbackground = "silver")
    fr4 = LabelFrame(fr, text = "Select And Update/Remove", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    fr5 = LabelFrame(fr, text = "Generate ID CARD", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    
    Label(fr, text = "STORE MANAGEMENT SYSTEM : MANAGE EMPLOYEE ",padx = 40,pady =5, font = "CooperBlack 20 bold",bd = 8, relief = GROOVE,  fg = 'black', bg = "#d3d3d3").pack(fill = BOTH)

    fr3.place(height =355 , width =530 ,relx = 0.006,rely =0.539)
    fr4.place(height =355 ,width =530 ,relx =0.338 ,rely =0.539 )
    fr5.place(height =355 ,width =530 ,relx =0.669 ,rely =0.539 )



    #treeview  
    #treeframe
    treeframe = Frame(fr,bd = 5, relief = GROOVE)
    treeframe.place(height = 380,width = w-18,relx = 0.005,rely = 0.078) 
    atree = Treeview(treeframe, height = 20)
    atree['columns'] = ('User Id','Password', 'Name','Phone','Email Id','Employee Id')

    #format
    atree.column("#0",width = 0,stretch = NO)
    atree.column("User Id",width =120,anchor = CENTER)
    atree.column("Password",width = 120,anchor = CENTER)
    atree.column("Name",width = 120, anchor = CENTER)
    atree.column("Phone",width = 120,anchor = CENTER)
    atree.column("Email Id",width = 120,anchor = CENTER)
    atree.column("Employee Id",width = 120,anchor = CENTER)

    #heading
    atree.heading("#0", text = "",anchor = W)
    atree.heading("User Id", text = "UserId", anchor = CENTER)   
    atree.heading("Password", text = "Password", anchor = CENTER)
    atree.heading("Name", text = "Name", anchor = CENTER)
    atree.heading("Phone", text = "Phone", anchor = CENTER)
    atree.heading("Email Id", text = "Email Id", anchor = CENTER)
    atree.heading("Employee Id", text = "Employee Id", anchor = CENTER)
    atree.place(height = 400,width = w-12)
    
    #EntryInTable
    counter1 = 0
    for i in sqlAccess(cur.execute("select * from EMP;")):
        atree.insert(parent = '',index = END, iid= counter1, values = i)
        counter1+=1
  
    #scroll bar
    treescroll = Scrollbar(treeframe)
    treescroll.pack(side = RIGHT, fill = Y)
    atree.config(yscrollcommand = treescroll.set)
    treescroll.config(command = atree.yview)

    #entry boxes 1
    Name4 = StringVar()
    Password4 = StringVar()
    Mail4 = StringVar()
    Phone4 = StringVar()
    UserId4 = StringVar()
    empid4 = StringVar()

    def cl_addemp():
        addemp = Employee(Name4.get(),empid4.get(),UserId4.get(),Password4.get(),Mail4.get(),Phone4.get())
        addemp.add_employee()
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from EMP;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1

    e1 = Entry(fr3,textvariable =Name4,font = "timesnewroman 12", width = 20, bd = 4)
    l1 = Label(fr3, text = "Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e2 = Entry(fr3,textvariable =UserId4,font = "timesnewroman 12", width = 20, bd = 4)
    l2 = Label(fr3, text = "User Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e3 = Entry(fr3,textvariable =Password4,font = "timesnewroman 12", width = 20, bd = 4)
    l3 = Label(fr3, text = "Password :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e4 = Entry(fr3,textvariable =Phone4,font = "timesnewroman 12", width = 20, bd = 4)
    l4 = Label(fr3, text = "Phone No :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e5 = Entry(fr3,textvariable =Mail4,font = "timesnewroman 12", width = 20, bd = 4)
    l5 = Label(fr3, text = "Email Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e6 = Entry(fr3,textvariable =empid4,font = "timesnewroman 12", width = 20, bd = 4)
    l6 = Label(fr3, text = "Employee Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")

    e1.place(relx =0.5 ,rely =0.070 )
    e2.place(relx =0.5 ,rely =0.20 )
    e3.place(relx =0.5 ,rely =0.35)
    e4.place(relx =0.5 ,rely =0.49 )
    e5.place(relx =0.5 ,rely =0.63 )
    e6.place(relx =0.5 ,rely =0.76 )

    l1.place(relx =0.1 ,rely =0.070 )
    l2.place(relx =0.1 ,rely =0.20 )
    l3.place(relx =0.1 ,rely =0.35)
    l4.place(relx =0.1 ,rely =0.49 )
    l5.place(relx =0.1 ,rely =0.63 )
    l6.place(relx =0.1 ,rely =0.76 )

    #Entry Boxes 2
    Name5 = StringVar()
    Password5 = StringVar()
    Mail5 = StringVar()
    Phone5 = StringVar()
    UserId5 = StringVar()

    e6 = Entry(fr4,textvariable =Name5,font = "timesnewroman 12", width = 20, bd = 4)
    l6 = Label(fr4, text = "Update Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e7 = Entry(fr4,textvariable =UserId5,font = "timesnewroman 12", width = 20, bd = 4)
    l7 = Label(fr4, text = "Change User Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e8 = Entry(fr4,textvariable =Password5,font = "timesnewroman 12", width = 20, bd = 4)
    l8 = Label(fr4, text = "Change Password :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e9 = Entry(fr4,textvariable =Phone5,font = "timesnewroman 12", width = 20, bd = 4)
    l9 = Label(fr4, text = "Update Phone No :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e10 = Entry(fr4,textvariable =Mail5,font = "timesnewroman 12", width = 20, bd = 4)
    l10 = Label(fr4, text = "Update Email Id :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")


    e6.place(relx =0.5 ,rely =0.075 )
    e7.place(relx =0.5 ,rely =0.23 )
    e8.place(relx =0.5 ,rely =0.38 )
    e9.place(relx =0.5 ,rely =0.52 )
    e10.place(relx =0.5 ,rely =0.66 )

    l6.place(relx =0.1 ,rely =0.075 )
    l7.place(relx =0.1 ,rely =0.23 )
    l8.place(relx =0.1 ,rely =0.38)
    l9.place(relx =0.1 ,rely =0.52 )
    l10.place(relx =0.1 ,rely =0.66 )

    

    #================FUNCTIONS IN EMPLOYEE===================


    
    def clicked(event):
        global value1
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        selected1 = atree.focus()
        value1 = atree.item(selected1,'values')   
        e6.insert(0,value1[2])
        e7.insert(0,value1[0])
        e8.insert(0,value1[1])
        e9.insert(0,value1[3])
        e10.insert(0,value1[4])
     
        
    def cl_genid():
        data = value1               
        genQR(data[5],data[2])
        ms.showinfo("Saved","Id Card generated and saved in folder id_gen.")
        
    def cl_remove():
        sqlInsert(cur.execute("DELETE FROM EMP WHERE EMPID = ?",(value1[5],)))
        ms.showinfo("Removed","Employee Removed!")
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from EMP;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1       
        
        
    def cl_updtemp():
        upemp = Employee(Name5.get(),value1[5],UserId5.get(),Password5.get(),Mail5.get(),Phone5.get())
        upemp.update_employee()  
        atree.delete(*atree.get_children())
        counter1 = 0
        for i in sqlAccess(cur.execute("select * from EMP;")):
            atree.insert(parent = '',index = END, iid= counter1, values = i)
            counter1+=1      

    atree.bind("<Double-1>",clicked)


        #buttons
    c3 = Button(fr3,text = "Add Employee",bd = 2,command = cl_addemp,relief =GROOVE,font = "timesewroman 12 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
    c4 = Button(fr4,text = "Update Employee",bd = 2,command = cl_updtemp,relief = GROOVE,font = "timesewroman 12 bold",bg = "white", activebackground = "#3B3131",  padx = 7)
    c5 = Button(fr4,text = "Remove Employee",bd = 2,command = cl_remove,relief = GROOVE,font = "timesewroman 12 bold",bg = "white",activebackground = "#3B3131",  padx = 7 )    
    c7 = Button(fr5,text = "Generate ID",compound = TOP,image = x13,bd = 2,command = cl_genid,relief = GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )    
    c6 = Button(fr4,text = "Close",bd = 2,command = fr.destroy,relief = GROOVE,font = "timesewroman 12 bold",bg = "red",fg = "yellow",activebackground = "#3B3131",  padx = 8 )    
    c3.place(relx = 0.3,  rely = 0.9)
    c4.place(relx = 0.4 ,rely =0.85)
    c5.place(relx = 0.01,rely =0.85 )
    c6.place(relx = 0.82,rely =0.85 )
    c7.place(relx = 0.25, rely = 0.15)

def contactus():
    ms.showinfo("Contact Us","If you have any query regarding this application.Feel free to reach us at atulk1844@gmail.com or call us at XXXXXXXX45. We will reply as soon as possible. Regards!")
    speak("HELLO SIR !!THIS STORE, MANAGEMENT SYSTEM IS MADE, FOR CBSE PROJECT WORK 2020-2021, BY ATUL KUMAR SINGH , CLASS 12 SCIENCE, ROLL NUMBER 3. THANKYOU FOR USING MY SOFTWARE")




#internal functions of ADMIN PAGE

    
def itemEntryadmin():
    #frame
    fr = Frame(admin, bg = "black" )
    fr.place(height = h , width = w , relx = 0, rely = 0)
    fr3 = LabelFrame(fr, text = "Add Item", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,foreground = "yellow",bg = "#151b54", highlightbackground = "silver")
    fr4 = LabelFrame(fr, text = "Select And Update Item", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    fr5 = LabelFrame(fr, text = "Remove Item", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")   
    
    Label(fr, text = "STORE MANAGEMENT SYSTEM : ADD ITEM ",padx = 40,pady =5, font = "CooperBlack 20 bold",bd = 8, relief = GROOVE,  fg = 'black', bg = "#d3d3d3").pack(fill = BOTH)

    fr3.place(height =450 , width =530 ,relx = 0.006,rely =0.419)
    fr4.place(height =450 ,width =530 ,relx =0.338 ,rely =0.419 )
    fr5.place(height =450 ,width =530 ,relx =0.669 ,rely =0.419 )

    #treeview  
    #treeframe
    treeframe = Frame(fr,bd = 5, relief = GROOVE)
    treeframe.place(height = 280,width = w-18,relx = 0.005,rely = 0.078) 
    atree = Treeview(treeframe, height = 12)
    atree['columns'] = ('Product Code','Product Name','Product Category','Selling Price','Quantity Available')

    #format
    atree.column("#0",width = 0,stretch = NO)
    atree.column("Product Code",width = 20, anchor = CENTER)
    atree.column("Product Name",width = 100,anchor = CENTER)
    atree.column("Product Category",width =50,anchor = CENTER) 
    atree.column("Selling Price",width = 50,anchor = CENTER)
    atree.column("Quantity Available",width = 50,anchor = CENTER)

    #heading
    atree.heading("#0", text = "",anchor = W)
    atree.heading("Product Code", text = "Product Code", anchor = CENTER)
    atree.heading("Product Name", text = "Product Name", anchor = CENTER)
    atree.heading("Product Category",text = "Product Category", anchor = CENTER)
    atree.heading("Selling Price", text = "Selling Price", anchor = CENTER)
    atree.heading("Quantity Available", text = "Quantity Available", anchor = CENTER)
    atree.place(height = 400,width = w-12)
    
    #EntryInTable
    counter3 = 0
    for i in sqlAccess(cur.execute("SELECT * FROM INVENTORY;")):
        atree.insert(parent = '',index = END, iid= counter3, values = i)
        counter3+=1
  
    #scroll bar
    treescroll = Scrollbar(treeframe)
    treescroll.pack(side = RIGHT, fill = Y)
    atree.config(yscrollcommand = treescroll.set)
    treescroll.config(command = atree.yview)

    #entry boxes 1
    Name6 = StringVar()
    Pcode6 = StringVar()
    Quan6 = StringVar()
    Price6 = StringVar()
    Pcat6 = StringVar()

    def cl_additem():

        AddItem = ItemEntry(Name6.get(),Pcat6.get(),Pcode6.get(),Price6.get(),Quan6.get())
        AddItem.add_item()        
        ms.showinfo("Successful","Item Added!")
        atree.delete(*atree.get_children())
        counter3 = 0
        for i in sqlAccess(cur.execute("SELECT * FROM INVENTORY;")):
            atree.insert(parent = '',index = END, iid= counter3, values = i)
            counter3+=1



    e1 = Entry(fr3,textvariable =Name6,font = "timesnewroman 12", width = 20, bd = 4)
    l1 = Label(fr3, text = "Product Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e2 = Entry(fr3,textvariable =Pcat6,font = "timesnewroman 12", width = 20, bd = 4)
    l2 = Label(fr3, text = "Product Category:", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e3 = Entry(fr3,textvariable =Pcode6,font = "timesnewroman 12", width = 20, bd = 4)
    l3 = Label(fr3, text = "Product Code :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e4 = Entry(fr3,textvariable =Price6,font = "timesnewroman 12", width = 20, bd = 4)
    l4 = Label(fr3, text = "Selling Price :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e5 = Entry(fr3,textvariable =Quan6,font = "timesnewroman 12", width = 20, bd = 4)
    l5 = Label(fr3, text = "Quantity :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")

    e1.place(relx =0.5 ,rely =0.075 )
    e2.place(relx =0.5 ,rely =0.23 )
    e3.place(relx =0.5 ,rely =0.38)
    e4.place(relx =0.5 ,rely =0.52 )
    e5.place(relx =0.5 ,rely =0.66 )

    l1.place(relx =0.1 ,rely =0.075 )
    l2.place(relx =0.1 ,rely =0.23 )
    l3.place(relx =0.1 ,rely =0.38)
    l4.place(relx =0.1 ,rely =0.52 )
    l5.place(relx =0.1 ,rely =0.66 )

    #Entry Boxes 2
    Name7 = StringVar()
    Pcode7 = StringVar()
    Quan7 = StringVar()
    Price7 = StringVar()
    Pcat7 = StringVar()

    e6 = Entry(fr4,textvariable =Name7,font = "timesnewroman 12", width = 20, bd = 4)
    l6 = Label(fr4, text = "Product Name :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e7 = Entry(fr4,textvariable =Pcat7,font = "timesnewroman 12", width = 20, bd = 4)
    l7 = Label(fr4, text = "Product Category:", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e8 = Entry(fr4,textvariable =Pcode7,font = "timesnewroman 12",state = DISABLED, width = 20, bd = 4)
    l8 = Label(fr4, text = "Product Code* :", font = "timesnewroman 14 bold" ,  fg = 'red', bg = "#151b54")
    e9 = Entry(fr4,textvariable =Price7,font = "timesnewroman 12", width = 20, bd = 4)
    l9 = Label(fr4, text = "Selling Price :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e10 = Entry(fr4,textvariable =Quan7,font = "timesnewroman 12", width = 20, bd = 4)
    l10 = Label(fr4, text = "Quantity :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    e6.place(relx =0.5 ,rely =0.075 )
    e7.place(relx =0.5 ,rely =0.23 )
    e8.place(relx =0.5 ,rely =0.38 )
    e9.place(relx =0.5 ,rely =0.52 )
    e10.place(relx =0.5 ,rely =0.66 )

    l6.place(relx =0.1 ,rely =0.075 )
    l7.place(relx =0.1 ,rely =0.23 )
    l8.place(relx =0.1 ,rely =0.38)
    l9.place(relx =0.1 ,rely =0.52 )
    l10.place(relx =0.1 ,rely =0.66 )

    #Delete Selected
    delt4 = StringVar()
    l11 = Label(fr5, text = "REMOVE Item By Selecting (Code):", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
    l11.place(relx =0.23,rely = 0.19)
    e11 = Entry(fr5,state = DISABLED,textvariable =delt4,font = "timesnewroman 16 bold", width = 20, bd = 4)
    e11.place(relx =0.29 ,rely =0.32 )




    #================FUNCTIONS===================


    
    def clicked2(event):
        global value4
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        selected4 = atree.focus()
        value4 = atree.item(selected4,'values') 
        e6.insert(0,value4[1])
        e7.insert(0,value4[2])
        Pcode7.set(value4[0])
        e9.insert(0,value4[3])
        e10.insert(0,value4[4])
        delt4.set(value4[0])  
 
    def cl_Updtitem():

        UpItem = ItemEntry(Name7.get(),Pcat7.get(),value4[0],Price7.get(),Quan7.get())
        UpItem.update_item()
        atree.delete(*atree.get_children())
        counter3 = 0
        for i in sqlAccess(cur.execute("SELECT * FROM INVENTORY;")):
            atree.insert(parent = '',index = END, iid= counter3, values = i)
            counter3+=1        

    def cl_removeitem():
        sqlInsert(cur.execute("DELETE FROM INVENTORY WHERE PCODE = ?",(value4[0],)))
        ms.showinfo("Removed","Item Removed!")
        atree.delete(*atree.get_children())
        counter3 = 0
        for i in sqlAccess(cur.execute("SELECT * FROM INVENTORY;")):
            atree.insert(parent = '',index = END, iid= counter3, values = i)
            counter3+=1        

    def gen_bar_code_additem():
        genBar(Pcode6.get(),Name6.get())
        ms.showinfo("Done",f"BARCODE for product code {Pcode6.get()} has been generated in BARCODES folder!")

    def gen_bar_code():
        pdtname = sqlAccess(cur.execute("SELECT PNAME FROM INVENTORY WHERE PCODE = ?",(delt4.get(),)))[0][0]
        genBar(delt4.get(),pdtname)
        ms.showinfo("Done",f"BARCODE for product code {delt4.get()} has been generated in BARCODES folder!")
         
    atree.bind("<Double-1>",clicked2)


    #buttons
    c3 = Button(fr3,text = "Add Item",bd = 2,command = cl_additem,relief =GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
    c7 = Button(fr3,text = "Gen Bar Code*",bd = 2,command =gen_bar_code_additem,relief =GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
    c8 = Button(fr5,text = "Gen Bar Code*",bd = 2,command =gen_bar_code,relief =GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
    c4 = Button(fr4,text = "Update Item",bd = 2,command = cl_Updtitem,relief = GROOVE,font = "timesewroman 14 bold",bg = "white", activebackground = "#3B3131",  padx = 10 )
    c5 = Button(fr5,text = "Remove Item",bd = 2,command = cl_removeitem,relief = GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )    
    c6 = Button(fr5,text = "Close",bd = 2,command = fr.destroy,relief = GROOVE,font = "timesewroman 14 bold",bg = "red",fg = "yellow",activebackground = "#3B3131",  padx = 10 )    
    c3.place(relx = 0.1,  rely = 0.85)
    c7.place(relx = 0.5,  rely = 0.85)
    c4.place(relx = 0.3 ,rely =0.85)
    c5.place(relx = 0.34,rely =0.55 )
    c6.place(relx = 0.41,rely =0.75 )
    c8.place(relx = 0.32,rely =0.65 )

def inventory():
    #frame
    fr = Frame(admin, bg = "black" )
    fr.place(height = h , width = w , relx = 0, rely = 0)

    lf = LabelFrame(fr, text = "INVENTORY DATABASE", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,foreground = "yellow",bg = "#151b54", highlightbackground = "silver")
    lf.place(height = 700,width = w-12)

    #search option
    lookvar = StringVar()
    def searchInventory():
        s = lookvar.get()
        data = sqlAccess(cur.execute("SELECT * FROM INVENTORY WHERE PNAME LIKE ?",(f"%{s}%",)))
        atree.delete(*atree.get_children())
        counter = 0
        for i in data:
            atree.insert(parent = '',index = END, iid= counter, values = i)
            counter+=1

    def clearsearch():
        atree.delete(*atree.get_children())
        look.delete(0,END)
        counter = 0
        for i in sqlAccess(cur.execute("SELECT * FROM INVENTORY;")):
            atree.insert(parent = '',index = END, iid= counter, values = i)
            counter+=1
        
    Label(fr, text = "Search by Name :",bg = "black", fg = "white" ,font = "timesnewroman 14 bold").place(relx = 0.32, rely = 0.85)
    look = Entry(fr,textvariable =lookvar,font = "timesnewroman 12", width = 20, bd = 4)
    look.place(relx = 0.45,rely =0.85 )
    Button(fr, text = "Search",command = searchInventory,relief = SUNKEN,font = "timesewroman 12 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 ).place(relx = 0.386,rely =0.89 )
    Button(fr, text = "Clear",command = clearsearch,relief = SUNKEN,font = "timesewroman 12 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 ).place(relx = 0.506,rely =0.89 )
    CloseBt(fr,0.6,0.89,fr)

    #treeview  
    #treeframe
    treeframe = Frame(lf,bd = 5, relief = GROOVE)
    treeframe.place(height =700 ,width = w-18,relx = 0,rely = 0) 
    atree = Treeview(lf)
    atree['columns'] = ('Product Code','Product Name',"Product Category","Selling Price","Quantity Available")

    #format
    atree.column("#0",width = 0,stretch = NO)
    atree.column("Product Code",width = 20, anchor = CENTER)
    atree.column("Product Name",width =50,anchor = CENTER) 
    atree.column("Product Category",width = 120,anchor = CENTER)
    atree.column("Selling Price",width = 50,anchor = CENTER)
    atree.column("Quantity Available",width = 50,anchor = CENTER)

    #heading
    atree.heading("#0", text = "",anchor = W)
    atree.heading("Product Code", text = "Product Code", anchor = CENTER)
    atree.heading("Product Name", text = "Product Category", anchor = CENTER)
    atree.heading("Product Category", text = "Product Name", anchor = CENTER)
    atree.heading("Selling Price", text = "Selling Price", anchor = CENTER)
    atree.heading("Quantity Available", text = "Quantity Available", anchor = CENTER)
    atree.place(height = 750,width = w-18)
    #EntryInTable
    counter = 0
    for i in sqlAccess(cur.execute("SELECT * FROM INVENTORY;")):
        atree.insert(parent = '',index = END, iid= counter, values = i)
        counter+=1
    #scroll bar
    treescroll = Scrollbar(lf)
    treescroll.pack(side = RIGHT, fill = Y)
    atree.config(yscrollcommand = treescroll.set)
    treescroll.config(command = atree.yview)
        
def todaySelling():
    #frame
    frame = Frame(admin)
    frame.place(height = 200,width = 700,relx = 0.3, rely = 0.25)

    fr = LabelFrame(frame, text = "TODAY'S SALE",foreground = "yellow", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", highlightbackground = "silver" )
    fr.place( height = 200,width = 700)

    CloseBt(fr,0.45,0.8,frame)

    sold = StringVar()
    current_date = datetime.now().strftime("%Y-%m-%d")
    amount = sqlAccess(cur.execute("SELECT AMOUNT FROM SALE WHERE DATE = ?",(current_date,)))[0][0] 
    Label(fr, text = "******* Today you Sold Items Of Total *******",bg = "#151b54", fg = "white" ,font = "timesnewroman 14 bold").place(relx = 0.25, rely = 0.1)
    sell = Entry(fr,state = DISABLED,textvariable =sold,font = "timesnewroman 12", width = 20, bd = 4)
    sell.place(relx = 0.37, rely = 0.4)
    sold.set(f"Rs. {amount}")

def stats():
    dates = []
    earning = []
    for i in sqlAccess(cur.execute("SELECT DATE FROM SALE")):
        dates.append(i[0])

    for j in sqlAccess(cur.execute("SELECT AMOUNT FROM SALE")):
        earning.append(j[0])

    plt.style.use("dark_background")
    ypos = np.arange(len(dates))
    plt.xticks(ypos,dates)
    width = 0.35
    plt.bar(ypos,earning,color = (1,1,0,0.8))
    plt.xlabel("DATES")
    plt.ylabel("TOTAL SELLING AMOUNT (Rs)")
    plt.title("YOUR DAILY SELLING DETAILS")
    plt.show()

def importing():
    #frame
    fr = Frame(admin, bg = "black" )
    fr.place(height = h , width = w , relx = 0, rely = 0)

    Label(fr, text = "STORE MANAGEMENT SYSTEM : IMPORT ",padx = 40,pady = 12, font = "CooperBlack 30 bold",bd = 8, relief = GROOVE,  fg = 'black', bg = "#d3d3d3").pack(fill = BOTH)
    fr1 = LabelFrame(fr, text = "Import From Supplier", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")
    fr1.place(height =615 ,width =595 ,relx =0.02 ,rely =0.15 )
    textframe = Frame(fr1)
    textframe.place(height = 170,width = 515,relx = 0.07, rely = 0.58)

    #Importing Details
    name8= StringVar()
    phn8 = StringVar()
    categ8 = StringVar()
    quan8 = IntVar()

    l5 = Label(fr1, text = "Supplier Name -", font = "timesnewroman 14 bold",   fg = 'white', bg = "#151b54")
    l6 = Label(fr1, text = "Phone -", font = "timesnewroman 14 bold",  fg = 'white', bg = "#151b54")
    l7 = Label(fr1, text = "Supplier Of -", font = "timesnewroman 14 bold",  fg = 'white', bg = "#151b54")
    l8 = Label(fr1, text = "Quantity -", font = "timesnewroman 14 bold",   fg = 'white', bg = "#151b54")
    l9 = Label(fr1,text = "Please Describe Your Order-", font = "timesnewroman 10 bold",   fg = 'white', bg = "#151b54")
    e5 = Entry(fr1,textvariable =name8,font = "timesnewroman 14", width = 20, bd = 4)
    e6 = Entry(fr1,textvariable =phn8,font = "timesnewroman 14", width = 20, bd = 4)
    e7 = Entry(fr1,textvariable =categ8,font = "timesnewroman 14", width = 20, bd = 4)
    e8 = Entry(fr1,textvariable =quan8,font = "timesnewroman 14", width = 20, bd = 4)
    t9 = Text(fr1,font = "Timesnewroman 15")
    CloseBt(fr1,0.28,0.905,fr)


    #text scroll
    scroll = Scrollbar(textframe)
    scroll.pack(side = RIGHT, fill = Y)
    t9.config(yscrollcommand = scroll.set)
    scroll.config(command = t9.yview)

    l5.place(relx = 0.1,rely = 0.04)
    l6.place(relx =0.1 ,rely = 0.16)
    l7.place(relx =0.1 ,rely = 0.28 )
    l8.place(relx = 0.1,rely = 0.40 )
    l9.place(relx = 0.04, rely = 0.54)
    e5.place(relx = 0.5,rely = 0.04)
    e6.place(relx = 0.5,rely = 0.16)
    e7.place(relx = 0.5,rely = 0.28)
    e8.place(relx = 0.5,rely = 0.40)
    t9.place(height = 170,width = 500,relx = 0.07, rely = 0.58)


    def cl_order():
        OrderItem = ImportGoods(name8.get(),phn8.get(),categ8.get(),quan8.get(), t9.get(1.0,END))
        OrderItem.set_order()
        atree.delete(*atree.get_children())
        counter = 0
        for i in sqlAccess(cur.execute("SELECT NAME,PHONE,SUPP_OF,DEF FROM SUPPLIER;")):
            atree.insert(parent = '',index = END, iid= counter, values = i)
            counter+=1

    #treeview  
    #treeframe
    treeframe = LabelFrame(fr,text = "Available Suppliers",font = "Timesnewroman 14",bd = 5, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")
    treeframe.place(height = 380,width = 800,relx = 0.46,rely = 0.15) 
    atree = Treeview(treeframe, height = 20)
    atree['columns'] = ('Name', 'Phone', 'Supplier of',"Default Supplier")

    #format
    atree.column("#0",width = 0,stretch = NO)
    atree.column("Name",width = 90, anchor = CENTER)
    atree.column("Phone",width =60,anchor = CENTER) 
    atree.column("Supplier of",width = 40,anchor = CENTER)
    atree.column("Default Supplier",width = 10,anchor = CENTER)

    #heading
    atree.heading("#0", text = "",anchor = W)
    atree.heading("Name", text = "Name", anchor = CENTER)
    atree.heading("Phone", text = "Phone", anchor = CENTER)
    atree.heading("Supplier of", text = "Supplier of", anchor = CENTER)
    atree.heading("Default Supplier", text = "Default Supplier(Y/N)", anchor = CENTER)
    atree.place(height = 380,width = 780)

    #INSERTING
    counter = 0
    for i in sqlAccess(cur.execute("SELECT NAME,PHONE,SUPP_OF,DEF FROM SUPPLIER;")):
        atree.insert(parent = '',index = END, iid= counter, values = i)
        counter+=1
  
    #scroll bar
    treescroll = Scrollbar(treeframe)
    treescroll.pack(side = RIGHT, fill = Y)
    atree.config(yscrollcommand = treescroll.set)
    treescroll.config(command = atree.yview)


    #===========================treeview2=========================

    
    #treeframe
    treeframe1 = LabelFrame(fr,text = "Current Orders",font = "Timesnewroman 14",bd = 5, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")
    treeframe1.place(height = 200,width = 800,relx = 0.46,rely = 0.65) 
    atree1 = Treeview(treeframe1, height = 20)
    atree1['columns'] = ('Name', 'Phone', 'Supplier of',"Quantity")

    #format
    atree1.column("#0",width = 0,stretch = NO)
    atree1.column("Name",width = 90, anchor = CENTER)
    atree.column("Phone",width =60,anchor = CENTER) 
    atree1.column("Supplier of",width = 40,anchor = CENTER)
    atree1.column("Quantity",width = 10,anchor = CENTER)

    #heading
    atree1.heading("#0", text = "",anchor = W)
    atree1.heading("Name", text = "Name", anchor = CENTER)
    atree1.heading("Phone", text = "Phone", anchor = CENTER)
    atree1.heading("Supplier of", text = "Supplier of", anchor = CENTER)
    atree1.heading("Quantity", text = "Quantity Ordered", anchor = CENTER)
    atree1.place(height = 200,width = 780)

    #INSERTING
    counter = 0
    if  sqlAccess(cur.execute("SELECT * FROM IMPORTING")) == []:
        pass
    else:    
        for i in sqlAccess(cur.execute("SELECT * FROM IMPORTING")):
            atree1.insert(parent = '',index = END, iid= counter, values = i)
            counter+=1
    
    #scroll bar
    treescroll1 = Scrollbar(treeframe1)
    treescroll1.pack(side = RIGHT, fill = Y)
    atree1.config(yscrollcommand = treescroll1.set)
    treescroll1.config(command = atree1.yview)

    #================FUNCTIONS===================

    
    def clicked3(event):
        global value5 
        selected5 = atree1.focus()
        value5 = atree1.item(selected5,'values') 

    def cl_removeimpt():
        sqlInsert(cur.execute("DELETE FROM IMPORTING WHERE NAME = ?",(value5[0],)))
        ms.showinfo("Removed", "Details are removed from database but will be in you email history!")
        atree1.delete(*atree1.get_children())
        counter = 0
        for i in sqlAccess(cur.execute("SELECT * FROM IMPORTING")):
            atree1.insert(parent = '',index = END, iid= counter, values = i)
            counter+=1      
 
    atree1.bind("<Double-1>",clicked3)


    c8 = Button(fr1,text = "Order",command =cl_order,relief = SUNKEN,font = "timesewroman 14 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 )
    c8.place(relx = 0.442 ,rely = 0.9)

    c9 = Button(fr1,text = "Delete",command =cl_removeimpt,relief = SUNKEN,font = "timesewroman 14 bold",bg = "SKY BLUE", pady= 1,activebackground = "#3B3131",  padx = 5 )
    c9.place(relx = 0.62 ,rely = 0.9) 
    Label(fr1, text = "*Select From Importing Tabel And Press Delete To Remove From Tabel!*", font = "timesnewroman 10 bold",   fg = 'RED', bg = "#151b54").place(relx = 0.02, rely = 0.97)

def discount():
    #frame
    fr = LabelFrame(admin, text = "Discount Declaration",foreground = "yellow", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", highlightbackground = "silver"  )
    fr.place(height = 450 , width = 700 ,relx = 0.28, rely = 0.15)

    gift = StringVar()
    DisPer = IntVar()
    shopabove = IntVar()

    def Apply():
        sqlInsert(cur.execute("DELETE FROM DISCOUNT"))
        sqlInsert(cur.execute("INSERT INTO DISCOUNT VALUES(?,?,?)",(DisPer.get(),gift.get(),shopabove.get())))
        ms.showinfo("Done","Conditions Applied!")



    Label(fr, text = "**Discounts will be fixed, change daily to update!!**",bg = "#151b54", fg = "Red" ,font = "timesnewroman 11 bold").place(relx = 0.02, rely = 0.1)
    
    e1 = Entry(fr,textvariable =DisPer,font = "timesnewroman 15", width = 20, bd = 4)
    l1 = Label(fr, text = "Discount % :", font = "timesnewroman 15 bold" ,  fg = 'White', bg = "#151b54")
    l2 = Label(fr, text = "GIFT FOR SHOPPING :", font = "timesnewroman 14 bold",   fg = 'white', bg = "#151b54")
    l3 = Label(fr, text = "SHOP ABOVE :", font = "timesnewroman 14 bold",   fg = 'white', bg = "#151b54")
    e2 = Entry(fr,textvariable =gift,font = "timesnewroman 12", width = 20, bd = 4)
    e3 = Entry(fr,textvariable =shopabove,font = "timesnewroman 12", width = 20, bd = 4)
    Label(fr, text = "Applies on All Products!!",bg = "#151b54", fg = "RED" ,font = "timesnewroman 10 bold").place(relx = 0.44, rely = 0.35)

    e1.place(relx = 0.44,rely = 0.27)
    e2.place(relx = 0.44,rely = 0.45)
    e3.place(relx = 0.44,rely = 0.65)
    l1.place(relx =0.02 ,rely =0.27 )
    l2.place(relx =0.02 ,rely = 0.45 )
    l3.place(relx =0.02 ,rely = 0.65 )


    Button(fr,text = "Apply",command = Apply,relief = SUNKEN,font = "timesewroman 12 bold",bg = "sky blue", pady= 1,activebackground = "#3B3131",  padx = 5).place(relx = 0.453,rely =0.75 )
    CloseBt(fr,0.45,0.82,fr)

def settings():

    #frame
    frame = Frame(admin, bg = "black" )
    frame.place(height = 200 , width = 600 , relx = 0.35, rely = 0.3)
    fr = LabelFrame(frame, text = "RESET SOFTWARE",foreground = "yellow", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", highlightbackground = "silver" )
    fr.place( height = 200,width = 600)
    CloseBt(fr,0.4,0.7,frame)
    
    Label(fr, text = "Clear Database(Factory Reset) - ",foreground = "White", font = "timesnewroman 15 bold",bg = "#151b54").place(relx = 0.03, rely = 0.25)
   
    def cl_reset():
        res = ms.askokcancel("Warning","Do you really want wo clear your database?  (This cannot be Undone!)")
        if res == True:
            import time
            ms.showwarning("Clearing","The app will close in 5 secs! Press Ok to proceed--")            
            timeout = Label(admin, text ="",bg = "black",fg = "red", font = "helvetica 150 bold")
            timeout.place(height = h,width = w)
            def st():
                for k in range(5,-1,-1):
                    timeout.config(text = f"0{k}:00")
                    timeout.update()
                    time.sleep(1)
            st()
            sqlInsert(cur.execute("DELETE FROM ADMIN;"))
            sqlInsert(cur.execute("DELETE FROM EMP;"))
            sqlInsert(cur.execute("DELETE FROM INVENTORY;"))
            sqlInsert(cur.execute("DELETE FROM SUPPLIER"))
            sqlInsert(cur.execute("DELETE FROM SALE"))
            sqlInsert(cur.execute("DELETE FROM IMPORTING"))
            admin.destroy()
        else:
            pass

    
    Button(fr,text = "Reset",bd = 2,command = cl_reset,relief = GROOVE,font = "timesewroman 12 bold",bg = "Grey",fg = "white",activebackground = "#3B3131",  padx =11 ).place(relx = 0.57,  rely = 0.25)

"""EMPLOYEE PAGE FUNCTIONS"""
def selling():
    
    flag = 0
    if len(sqlAccess(cur.execute("SELECT * FROM EMP;"))) >=  2:
        logid = sqlAccess(cur.execute("SELECT ID FROM EMP;"))
        logpass = sqlAccess(cur.execute("SELECT PASSWORD FROM EMP;"))
        loginid = []
        loginpass = []
        for i in range(0,len(logid)):
            loginid.append(logid[i][0])
            loginpass.append(logpass[i][0])

        if userid1.get() in loginid and password1.get() in loginpass:
            flag = 1

    elif userid1.get() in sqlAccess(cur.execute("SELECT ID FROM EMP;"))[0][0] and password1.get() in sqlAccess(cur.execute("SELECT PASSWORD FROM EMP;"))[0][0]:
        flag = 2

    if flag == 1 or flag == 2:     

        #progressbar
        p = Progressbar(root,orient = HORIZONTAL, length = 500,maximum = 200, mode = "determinate")
        p.place(relx = 0.35,rely = 0.13)
        label100 = Label(root,text = "Loading....", font = "timesnewroman 14 bold", bg = "blue",fg = "white")
        label100.place(relx = 0.47,rely = 0.16)
        import time
        for x in range(4):
            p['value'] +=50 
            root.update_idletasks()
            time.sleep(1)
        p.destroy()
        label100.destroy()
        userentry1.delete(0,END)
        userpassword1.delete(0,END)   

        #tracing
        def checking(*args):
            x1 =  cusname.get()
            y1 = cusphone.get()
            z1 = cusmail.get()

            if len(x1)>0 and len(y1)>0:
                c2.config(state = NORMAL)     

            else:
                c2.config(state = DISABLED) 

        #inserting new date
        tdydate = datetime.now().strftime("%Y-%m-%d")
        datecheck = sqlAccess(cur.execute("SELECT DATE FROM SALE WHERE DATE = ?",(tdydate,)))
        if datecheck == []:
            sqlInsert(cur.execute("INSERT INTO SALE VALUES(?,?)",(tdydate,0)))
        else:
            pass
        
        #window
        emp = Toplevel()
        emp.grab_set()
        emp.title("******STORE MANAGEMENT WINDOW : EMPLOYEE******")
        emp.iconbitmap("icons/mainicon.ico")
        emp.focus_set()
        emp.geometry(f"{w}x{h}")
        emp.state("zoomed")
        emp.minsize(w,h)
        emp.maxsize(w,h)

        #frame
        fr = Frame(emp, bg = "black")
        fr.place(height = h , width = w , relx = 0, rely = 0)
        
        headtime = Label(fr, text = "",padx = 40,pady = 20, font = "CooperBlack 30 bold",bd = 8, relief = GROOVE,  fg = 'black', bg = "#d3d3d3")
        headtime.pack(fill = BOTH)
        def ht():
            samay = datetime.now().strftime("%I:%M:%S %p")
            heading = f"****STORE MANAGEMENT SYSTEM : SELL**** [Time: {samay}]"
            headtime.config(text = heading)
            headtime.after(1000,ht)
        ht()

        fr1 = LabelFrame(fr, text = "Previous Purchases",foreground = "yellow", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", highlightbackground = "silver")
        fr2 = LabelFrame(fr, text = "Customer Details", font = "timesnewroman 12 bold",foreground = "yellow", bd = 8, relief = GROOVE,bg = "#151b54", highlightbackground = "silver")
        fr3 = LabelFrame(fr, text = "Options", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,foreground = "yellow",bg = "#151b54", highlightbackground = "silver")
        fr4 = LabelFrame(fr, text = "Purchase", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE,bg = "#151b54", foreground = "yellow",highlightbackground = "silver")
        fr5 = LabelFrame(fr, text = "BILL", font = "timesnewroman 12 bold", bd = 8, relief = GROOVE, bg = "#151b54",highlightbackground = "silver",foreground = "yellow")
            
        fr1.place(height =170,width =445,relx =0.01 ,rely = 0.16 )
        fr2.place(height =387,width = 445 ,relx =0.01 ,rely = 0.39)
        fr3.place(height = 80, width = w-30,relx = 0.01,rely =0.868)
        fr4.place(height =615 ,width =595 ,relx =0.298 ,rely =0.133 )
        fr5.place(height =615 ,width = 500 ,relx =0.68 ,rely =0.133 )

        #datatype
        billno = IntVar()
        cusname = StringVar()
        cusphone = StringVar()
        cusmail = StringVar()
        pname = StringVar()
        pcode = StringVar()
        pcategory = StringVar()
        pquantity = IntVar()
        totalamt = IntVar()

        #entry
        if sqlAccess(cur.execute("SELECT * FROM DISCOUNT")) == []:
            pass
        else:
            offer = list(sqlAccess(cur.execute("SELECT * FROM DISCOUNT"))[0])
            text_ = f"{offer[0]}% on all purchases\nShop above Rs. {offer[2]} to get gift of the day!" 
            l9 = Label(fr4, text = f"Today's Deal: {text_}", font = "timesnewroman 13 bold",   fg = 'YELLOW', bg = "#151b54")
            l9.place(relx = 0.22,rely = 0.88)

        entry1 = Entry(fr1,textvariable =billno,font = "timesnewroman 12", width = 20, bd = 4)
        l1 = Label(fr1, text = "Bill Number :", font = "timesnewroman 14 bold" ,  fg = 'White', bg = "#151b54")
        l2 = Label(fr2, text = "Customer Name :", font = "timesnewroman 14 bold",   fg = 'white', bg = "#151b54")
        l3 = Label(fr2, text = "Customer Phone :", font = "timesnewroman 14 bold", fg = 'white', bg = "#151b54")
        l4 = Label(fr2, text = "Customer Email :", font = "timesnewroman 14 bold",  fg = 'white', bg = "#151b54")
        l9 = Label(fr2, text = "Fill customer's details and press enter to continue!", font = "timesnewroman 12 bold",  fg = 'green', bg = "#151b54")
        l5 = Label(fr4, text = "Product Name -", font = "timesnewroman 14 bold",   fg = 'white', bg = "#151b54")
        l6 = Label(fr4, text = "Product Code -", font = "timesnewroman 14 bold",  fg = 'white', bg = "#151b54")
        l7 = Label(fr4, text = "Product Category -", font = "timesnewroman 14 bold",  fg = 'white', bg = "#151b54")
        l8 = Label(fr4, text = "Product Quantity -", font = "timesnewroman 14 bold",   fg = 'white', bg = "#151b54")
        entry2 = Entry(fr2,textvariable =cusname,font = "timesnewroman 12", width = 20, bd = 4)
        entry3 = Entry(fr2,textvariable =cusphone,font = "timesnewroman 12", width = 20, bd = 4)
        entry4 = Entry(fr2,textvariable =cusmail,font = "timesnewroman 12", width = 20, bd = 4)
        entry5 = Entry(fr4,textvariable =pname,font = "timesnewroman 14", width = 20, bd = 4)
        entry6 = Entry(fr4,textvariable =pcode,font = "timesnewroman 14", width = 20, bd = 4)
        entry7 = Entry(fr4,textvariable =pcategory,font = "timesnewroman 14", width = 20, bd = 4)
        entry8 = Entry(fr4,textvariable =pquantity,font = "timesnewroman 14", width = 20, bd = 4)
        entry9 = Entry(fr4,state = DISABLED,textvariable =totalamt,font = "timesnewroman 14", width = 30, bd = 4)

        Label(fr4, text = "THANKS FOR SHOPPING WITH US!", font = "Timesnewroman 20 bold", fg = "hot pink", bg = "#151b54", relief = GROOVE, bd = 2 ).place(relx = 0.1,rely = 0.05)
        Label(fr5, text = "Bill Area", font = "Timesnewroman 16 bold", fg = "white", bg = "grey", relief = GROOVE, bd = 2 ).pack(fill = BOTH)
        entry1.place(relx = 0.42,rely = 0.17)
        entry2.place(relx = 0.44,rely = 0.18)
        entry3.place(relx = 0.44,rely = 0.38)
        entry4.place(relx = 0.44,rely = 0.58)
        entry5.place(relx = 0.47,rely = 0.15)
        entry6.place(relx = 0.47,rely = 0.27)
        entry7.place(relx = 0.47,rely = 0.39)
        entry8.place(relx = 0.47,rely = 0.51)
        entry9.place(relx = 0.22,rely = 0.8)

        l1.place(relx =0.05 ,rely =0.17 )
        l2.place(relx =0.02 ,rely = 0.18 )
        l3.place(relx =0.02 ,rely = 0.38)
        l4.place(relx = 0.02,rely = 0.58 )
        l5.place(relx = 0.1,rely = 0.15)
        l6.place(relx =0.1 ,rely = 0.27)
        l7.place(relx =0.1 ,rely = 0.39 )
        l8.place(relx = 0.1,rely = 0.51 )   
        l9.place(relx =0.02 ,rely = 0.1 )   
    
        #bill space
        t1 = Text(fr5,font = 'courier 13')
        t1.pack(fill = BOTH,expand = 1)
        date = datetime.now().strftime("%d/ %m/ %Y")
        tim = datetime.now().strftime("%H:%M:%S")
        t1.insert(END,"\t      ****APNA BAZAAR****\n")
        t1.insert(END,"\t   Thanks for shoppng with us\n")
        t1.insert(END,f"DT: {date}\n")
        t1.insert(END,f"Time: {tim}\n")
        t1.insert(END,f"Bill No: \n")
        t1.insert(END,"------------------------------------------------\n")
        t1.insert(END,f"Cus.-\t\t\t")
        t1.insert(END,f"Phone-\n")
        t1.insert(END,f"Mail-id-\n")
        t1.insert(END,"------------------------------------------------\n")
        t1.insert(END,"[Item]\t\t     [Qty]\t\t[Price]\n")
        t1.insert(END,"------------------------------------------------\n")

        billdata = t1.get(1.0,END) 
        total_price = []

        #scroll bar
        scroll = Scrollbar(t1)
        scroll.pack(side = RIGHT, fill = Y)
        scroll.config(command = t1.yview)
        t1.config(yscrollcommand = scroll.set)

        
    #===============================================SELLING FUNCTIONS====================================================


        def Search_bill():
            oldBill = prePurchase(billno.get())
            t1.delete(1.0,END)
            t1.insert(END,oldBill)

        def Gen_Bill():
            file = open(f"bill_gen/{genBillNo}.txt","w")
            file.write(t1.get(1.0,END))
            file.close()
            date = datetime.now().strftime("%d/ %m/ %Y")
            tim = datetime.now().strftime("%H:%M:%S")
            t1.insert(END,"\t      ****APNA BAZAAR****\n")
            t1.insert(END,"\t   Thanks for shoppng with us\n")
            t1.insert(END,f"DT: {date}\n")
            t1.insert(END,f"Time: {tim}\n")
            t1.insert(END,f"Bill No: \n")
            t1.insert(END,"------------------------------------------------\n")
            t1.insert(END,f"Cus.-\t\t\t")
            t1.insert(END,f"Phone-\n")
            t1.insert(END,f"Mail-id-\n")
            t1.insert(END,"------------------------------------------------\n")
            t1.insert(END,"[Item]\t\t     [Qty]\t\t[Price]\n")
            t1.insert(END,"------------------------------------------------\n")
            ms.showinfo("Bill Generated","Bill has been generated!")

        def Enter():
            global genBillNo
            #BILL NO GENERATE
            billNo = random.randint(10000000,99999999)
            genBillNo = billNo
            
            t1.delete(1.0,END)
            t1.insert(END,"\t      ****APNA BAZAAR****\n")
            t1.insert(END,"\t   Thanks for shoppng with us\n")
            t1.insert(END,f"DT: {date}\n")
            t1.insert(END,f"Time: {tim}\n")
            t1.insert(END,f"Bill No: {genBillNo} \n")
            t1.insert(END,"------------------------------------------------\n")
            t1.insert(END,f"Cus.- {cusname.get()}")
            t1.insert(END,f"\t\t\tPhone- {cusphone.get()}\n")
            t1.insert(END,f"Mail-id- {cusmail.get()}\n")
            t1.insert(END,"------------------------------------------------\n")
            t1.insert(END,"[Item]\t\t     [Qty]\t\t[Price]\n")
            t1.insert(END,"------------------------------------------------\n")
            c8.config(state = NORMAL)
            c3.config(state = NORMAL)
            c4.config(state = NORMAL)
            c5.config(state = NORMAL)
            c9.config(state = NORMAL)
            c6.config(state = NORMAL)
            c10.config(state = NORMAL)
            c11.config(state = NORMAL)

        def Total_amt():
            cmpt_price = tuple(total_price)
            cost = int(sum(cmpt_price))

            if sqlAccess(cur.execute("SELECT * FROM DISCOUNT")) == []:
                pass
                dis_cost = 0
            else:
                shopamt = sqlAccess(cur.execute("SELECT ABOVE FROM DISCOUNT"))[0][0]
                gifttogive = sqlAccess(cur.execute("SELECT GIFT FROM DISCOUNT"))[0][0]
                dis_cost = sqlAccess(cur.execute("SELECT DISCOUNT FROM DISCOUNT"))[0][0]

            
            final_cost = cost-(cost*dis_cost)/100
            
            prvamt = (sqlAccess(cur.execute("SELECT AMOUNT FROM SALE WHERE DATE = ?",(tdydate,))))[0][0]
            newamt = final_cost+prvamt
            sqlInsert(cur.execute("UPDATE SALE SET AMOUNT = ? WHERE DATE = ?",(newamt,tdydate)))
            totalamt.set(final_cost)
            t1.insert(END,"\n------------------------------------------------\n")   

            t1.insert(END,f"Total Amoount(with GST) :{cost}\n")   
            t1.insert(END,f"Total Discount :{cost*dis_cost/100}\n")
            t1.insert(END,f"Net Price :Rs. {final_cost}\n")
            t1.insert(END,"------------------------------------------------\n")
            if final_cost>=shopamt:
                t1.insert(END,f"You got : {gifttogive}, as your shopping surprise!")
            else:
                pass
            c3.config(state = NORMAL)
            c4.config(state = NORMAL)
            c5.config(state = NORMAL)
        
        def clear_ent():
            entry5.delete(0,END)
            entry6.delete(0,END)
            entry7.delete(0,END)
            entry8.delete(0,END)

        def printbill():
                file = filedialog.askopenfile(filetypes = (('All Files',"*"),("Template files", "*.type")))
                if file:
                    print("printing")
                else:
                    pass
        
        def cl_mailbill():
            sell = Retail(genBillNo,cusname.get(),cusphone.get(),cusmail.get(),t1.get(1.0,END))
            sell.mailbill()

        def cl_whatsappbill():
            whts = Retail(billno.get(),cusname.get(),cusphone.get(),cusmail.get(),billdata)
            whts.whatsapp_bill()

        def scan_Bar():
            barcode_taken = scanBar()
            output = sqlAccess(cur.execute("SELECT PNAME,PCATEGORY FROM INVENTORY WHERE PCODE = ?",(barcode_taken,)))[0]
            pcode.set(barcode_taken)
            pname.set(output[0])
            pcategory.set(output[1])

        def Add_to_cart():
            p = pname.get()
            q = pcategory.get()
            r = pcode.get()
            s = pquantity.get()
            price = int(sqlAccess(cur.execute("SELECT PSELL FROM INVENTORY WHERE PCODE = ?",(r,)))[0][0])*s
            
            if int(sqlAccess(cur.execute("SELECT PQUANTITY FROM INVENTORY WHERE PCODE = ?",(r,)))[0][0])<=s:
                ms.showinfo("Empty","SORRY! NOT IN STOCK!")
            else:    
                updtquantity =  int(sqlAccess(cur.execute("SELECT PQUANTITY FROM INVENTORY WHERE PCODE = ?",(r,)))[0][0])-s
                sqlInsert(cur.execute("UPDATE INVENTORY SET PQUANTITY = ? WHERE PCODE = ?",(updtquantity,r)))
                t1.insert(END,f"{p}\t\t\t{s}\t   {price}\n")
                total_price.append(price)

        def code_search():
            code = pcode.get()
            detail = list(sqlAccess(cur.execute("SELECT * FROM INVENTORY WHERE PCODE = ?",(code,)))[0])
            pname.set(detail[1])
            pcategory.set(detail[2])

        def clearall():
            entry1.delete(0,END)
            entry2.delete(0,END)
            entry3.delete(0,END)
            entry4.delete(0,END)
            c8.config(state = DISABLED)
            c9.config(state = DISABLED)
            c6.config(state = DISABLED)
            t1.delete(1.0,END)
            date = datetime.now().strftime("%d/ %m/ %Y")
            tim = datetime.now().strftime("%H:%M:%S")
            t1.insert(END,"\t      ****APNA BAZAAR****\n")
            t1.insert(END,"\t   Thanks for shoppng with us\n")
            t1.insert(END,f"DT: {date}\n")
            t1.insert(END,f"Time: {tim}\n")
            t1.insert(END,f"Bill No: \n")
            t1.insert(END,"------------------------------------------------\n")
            t1.insert(END,f"Cus.-\t\t\t")
            t1.insert(END,f"Phone-\n")
            t1.insert(END,f"Mail-id-\n")
            t1.insert(END,"------------------------------------------------\n")
            t1.insert(END,"[Item]\t\t     [Qty]\t\t[Price]\n")
            t1.insert(END,"------------------------------------------------\n")


        #buttons
        c1 = Button(fr1,text = "Search",command =Search_bill,relief = SUNKEN,font = "timesewroman 12 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 )
        c2 = Button(fr2,text = "Enter",state = DISABLED,command = Enter,relief = SUNKEN,font = "timesewroman 14 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 )
        c3 = Button(fr3,text = "Generate Bill",state = DISABLED,image = x11,compound = LEFT,bd = 2,command = Gen_Bill,relief =GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
        c4 = Button(fr3,text = "Email Bill",image = x10,compound = LEFT,state = DISABLED,bd = 2,command = cl_mailbill,relief = GROOVE,font = "timesewroman 14 bold",bg = "white", activebackground = "#3B3131",  padx = 10 )
        c5 = Button(fr3,text = "Whatsapp Bill",image = x9,compound = LEFT,bd = 2,state = DISABLED,command = cl_whatsappbill,relief = GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
        c6 = Button(fr4,text = "Total",command = Total_amt,state = DISABLED,relief = SUNKEN,font = "timesewroman 14 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 )
        c7 = Button(fr3,text = "Close Session",bd = 2,command = emp.destroy,relief = GROOVE,font = "timesewroman 14 bold",bg = "red",fg = "White", pady= 5,activebackground = "#3B3131",  padx = 10 )
        c8 = Button(fr4,text = "Add to Cart",state = DISABLED,command =Add_to_cart,relief = SUNKEN,font = "timesewroman 14 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 )
        c9 = Button(fr4,text = "Clear",command = clear_ent,relief = SUNKEN,state = DISABLED,font = "timesewroman 14 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 )
        c10 = Button(fr3,state = DISABLED,text = "Scan Bar",image = x12,bd = 2,compound = LEFT,command = scan_Bar,relief = GROOVE,font = "timesewroman 14 bold",bg = "white",activebackground = "#3B3131",  padx = 10 )
        c11 = Button(fr3,text = "Print Bill",bd = 2,command = printbill,state = DISABLED,relief = GROOVE,font = "timesewroman 14 bold",bg = "sky blue",fg = "red", pady= 5,activebackground = "#3B3131",  padx = 10 )
        c12 = Button(fr4,text = "Search",bd = 2,command = code_search,relief = GROOVE,font = "timesewroman 10 bold",bg = "white",fg = "black", pady= 3,activebackground = "#3B3131")
        c13 = Button(fr2,text = "Clear All",bd = 2,command = clearall,relief = GROOVE,font = "timesewroman 14 bold",bg = "white", pady= 1,activebackground = "#3B3131",  padx = 5 )


        c1.place(relx =0.35 ,rely =0.5 )
        c2.place(relx =0.20 ,rely =0.8 )
        c3.place(relx = 0.06,  rely = 0.05 )
        c4.place(relx = 0.23 ,rely =0.05)
        c5.place(relx = 0.385,rely =0.05 )
        c6.place(relx =0.48 ,rely =0.65 )
        c7.place(relx = 0.83,rely =0.05 )
        c8.place(relx =0.1 ,rely =0.65 )
        c9.place(relx =0.75 ,rely =0.65 )
        c10.place(relx = 0.69 ,rely =0.05 )
        c11.place(relx = 0.57 ,rely =0.05 )
        c12.place(relx = 0.88 ,rely =0.27 )
        c13.place(relx =0.54 ,rely =0.8 )
        cusname.trace("w",checking)
        cusphone.trace("w",checking)
        cusmail.trace("w",checking)
        emp.mainloop()
    else:
        ms.showerror("Wrong Credentials", "ID/PASSWORD entered is wrong.")
 
'''========================FRONT PAGE FUNCTIONS============================'''

def adm():


    flag = 0
    if len(sqlAccess(cur.execute("SELECT * FROM ADMIN;"))) >=  2:
        logid = sqlAccess(cur.execute("SELECT ID FROM ADMIN;"))
        logpass = sqlAccess(cur.execute("SELECT PASSWORD FROM ADMIN;"))
        loginid = []
        loginpass = []
        for i in range(0,len(logid)):
            loginid.append(logid[i][0])
            loginpass.append(logpass[i][0])

        if userid.get() in loginid and password.get() in loginpass:
            flag = 1

    elif userid.get() in sqlAccess(cur.execute("SELECT ID FROM ADMIN;"))[0][0] and password.get() in sqlAccess(cur.execute("SELECT PASSWORD FROM ADMIN;"))[0][0]:
        flag = 2

    if flag == 1 or flag == 2: 
        global admin

        #progressbar
        p = Progressbar(root,orient = HORIZONTAL, length = 500,maximum = 200, mode = "determinate")
        p.place(relx = 0.35,rely = 0.13)
        label100 = Label(root,text = "Loading....", font = "timesnewroman 14 bold", bg = "blue",fg = "white")
        label100.place(relx = 0.47,rely = 0.16)
        import time
        for x in range(4):
            p['value'] +=50 
            root.update_idletasks()
            time.sleep(1)
        p.destroy()
        label100.destroy()
        userentry.delete(0,END)
        userpassword.delete(0,END)   

    
        #admin window=======
        #admin config
        
        admin = Toplevel()
        admin.grab_set()
        admin.title("******STORE MANAGEMENT WINDOW : ADMIN******")
        admin.iconbitmap("icons/mainicon.ico")
        admin.focus_set()
        admin.geometry(f"{w}x{h}")
        admin.state("zoomed")
        admin.minsize(w,h)
        admin.maxsize(w,h)
        photo = ImageTk.PhotoImage(Image.open("mainimage1.jpg"))
        cvs = Canvas(admin,width =w,  height = h)
        cvs.pack(side = 'top')
        cvs.create_image(0,0,image = photo, anchor = 'nw')


        
        #============layout=================

        
        '''BUTTONS'''
        but1 = Button(admin,compound = TOP, text = "Inventory",command = inventory,image = x1, relief = SUNKEN,font = "timesewroman 15 bold",activebackground = "#3B3131", pady= 1, padx = 11 )
        but2 = Button(admin,compound = TOP, text = "Items Add",command = itemEntryadmin,image = x2, relief = SUNKEN,font = "timesewroman 15 bold", pady= 1, activebackground = "#3B3131", padx = 11 )
        but3 = Button(admin,compound = TOP, text = "Import Stock",command = importing,image = x3, relief = SUNKEN,font = "timesewroman 15 bold", pady= 1, activebackground = "#3B3131", padx = 11 )
        but4 = Button(admin,compound = TOP, text = "Statistics",command = stats,image = x4, relief = SUNKEN,font = "timesewroman 15 bold", pady= 1,activebackground = "#3B3131",  padx = 11 )
        but5 = Button(admin,compound = TOP, text = "Today's Sale",command = todaySelling,image = x5, relief = SUNKEN,font = "timesewroman 15 bold", pady= 1,activebackground = "#3B3131",  padx = 11 )
        but6 = Button(admin,compound = TOP, text = "On Sale Item",command = discount,image = x6, relief = SUNKEN,font = "timesewroman 15 bold", pady= 1, activebackground = "#3B3131", padx = 11 )
        but7 = Button(admin,text = "Logout",compound = TOP,command = admin.destroy,image = x7, relief = SUNKEN,font = "timesewroman 8 bold",bg = "cyan", pady= 1,activebackground = "#3B3131",  padx = 5 )
        but8 = Button(admin,text = "Reset",compound = TOP,command = settings,image = x8, relief = SUNKEN,font = "timesewroman 8 bold",bg = "pink", pady= 1,activebackground = "#3B3131",  padx = 5 )
        but1.place(relx = 0.01, rely = 0.26)
        but2.place(relx = 0.01, rely = 0.50)
        but3.place(relx = 0.01, rely = 0.75)
        but4.place(relx = 0.88, rely = 0.26)
        but5.place(relx = 0.88, rely = 0.50)
        but6.place(relx = 0.88, rely = 0.75)
        but7.place(relx = 0.92, rely = 0.01)
        but8.place(relx = 0.92, rely = 0.1)

        notify = sqlAccess(cur.execute("SELECT PCATEGORY FROM INVENTORY WHERE PQUANTITY <= 5"))
        if notify != []:
            low_items = []
            for items in notify:
                low_items.append(items[0])
            ms.showinfo("Low On Stock",f"Items of category: {low_items} are very low on Quantity. Please Import!\nCHECK INVENTORY FOR MORE DETAILS!")
        else:
            pass

        '''MENU'''
        mymenu = Menu(admin)
        m3 = Menu(mymenu, tearoff = 0)
        m3.add_command(label = "Add/Remove/Update ADMIN",  command = makeadmin)
        mymenu.add_cascade(label = "MANAGE ADMIN",menu = m3)

        m4 = Menu(mymenu,tearoff = 0)
        m4.add_command(label = "Add/Remove/Update EMPLOYEE", command = editemployee)
        mymenu.add_cascade(label = "MANAGE EMPLOYEE",menu = m4)

        m5 = Menu(mymenu,tearoff = 0)
        m5.add_command(label = "Add/Remove/Update SUPPLIER", command = supplier)
        mymenu.add_cascade(label = "MANAGE SUPPLIER", menu = m5)

        m6 = Menu(mymenu,tearoff = 0)
        m6.add_command(label = "Contact Us", command = contactus)
        mymenu.add_cascade(label = "HELP",menu = m6)

        admin.config(menu = mymenu)    
        admin.mainloop()

    else:
        ms.showerror("Wrong Credentials", "ID/PASSWORD entered is wrong.")

def searchadmin():
        try:    
            #email sequence
            import smtplib
            by_Password = sqlAccess(cur.execute("SELECT PASSWORD FROM ADMIN WHERE MAIL = ?",(forgotmail.get(),)))[0][0]
            by_Id = sqlAccess(cur.execute("SELECT ID FROM ADMIN WHERE MAIL = ?",(forgotmail.get(),)))[0][0]
            to = forgotmail.get()
            content = f"***ID PASSWORD RECOVERY FOR ADMIN***\n\nWe recieved your request for ID PASSWORD recovery. Here are your Id and Password;\n\nUser Id: {by_Id}\nPassword: {by_Password}\n\nIf not done by you, contact the Owner soon.\n\nRegards!"
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('apnaBazaarpvtltd@gmail.com', 'apnabazaar@')
            server.sendmail('apnaBazaarpvtltd@gmail.com',to, content)
            server.close()
            ms.showinfo("Successful","A mail has been sent to your registered mail-id.")
        except Exception as e:
            ms.showinfo("Failed",e)
    
def searchemp():
        try:    
            #email sequence
            import smtplib
            by_Password = sqlAccess(cur.execute("SELECT PASSWORD FROM EMP WHERE MAIL = ?",(forgotmail1.get(),)))[0][0]
            by_Id = sqlAccess(cur.execute("SELECT ID FROM EMP WHERE MAIL = ?",(forgotmail1.get(),)))[0][0]
            to = forgotmail1.get()
            content = f"***ID PASSWORD RECOVERY FOR EMPLOYEE***\n\nWe recieved your request for ID PASSWORD recovery. Here are your Id and Password;\n\nUser Id: {by_Id}\nPassword: {by_Password}\n\nIf not done by you, contact the admin soon.\n\nRegards!"
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('apnaBazaarpvtltd@gmail.com', 'apnabazaar@')
            server.sendmail('apnaBazaarpvtltd@gmail.com',to, content)
            server.close()
            ms.showinfo("Successful","A mail has been sent to your registered mail-id.")
        except Exception as e:
            ms.showinfo("Failed",e)

def signup():

    global name9,ids9,passwd9,mail9,phone9,window
    #trace function
    def check(*args):
        x =  name9.get()
        y = ids9.get()
        z = phone9.get()
        c = mail9.get()
        a = cnfpass9.get()
        v = passwd9.get()
        if len(x)>0 and len(y)>0 and len(z)>0 and len(a)>0 and len(v)>0 and len(c)>0:
            if v == a:
                button['state'] = NORMAL
            else:
                p12 = Label(window,text = "**Passwords are not same!**",bg = "#FFFFFF",fg = "red",font = "Timesnewroman 10 bold")
                p12.place(relx = 0.40,rely = 0.91)
        else:
            button['state'] = DISABLED


    window = Toplevel()
    window.grab_set()
    window.title("****Sign-Up****")
    window.iconbitmap("icons/mainicon.ico")
    window.focus_set()
    window.geometry("800x500")
    window.minsize(800,500)
    window.maxsize(800,500)
    photo = ImageTk.PhotoImage(Image.open("login2.png"))
    cvs = Canvas(window, width = 800, height = 500)
    cvs.pack(side = 'top')
    cvs.create_image(0,0,image = photo, anchor = 'nw')


    #=====var======

    
    name9 = StringVar()
    ids9 = StringVar()
    passwd9= StringVar()
    cnfpass9 = StringVar()
    mail9 = StringVar()
    phone9 = StringVar()
    
    Label(window,text = "SIGN UP", font = "gothic 24 bold", bd = 5, bg = "#0c090a", fg = "white").place(relx = 0.38,rely = 0.03,width = 200)
    Label(window,text = "Full Name :", font = "timesnewroman 14 bold", bd = 5, bg = "#254117", fg = "white").place(relx = 0.2,rely = 0.17)
    Entry(window,textvariable =name9,font = "timesnewroman 15", width = 20, bd = 4).place(relx = 0.5,rely = 0.17)
    
    Label(window,text = "User ID :", font = "timesnewroman 14 bold", bd = 5, bg = "#254117", fg = "white").place(relx = 0.2,rely = 0.27)
    Entry(window,textvariable = ids9,font = "timesnewroman 15", width = 20, bd = 4).place(relx = 0.5,rely = 0.27)
    
    Label(window,text = "Password :", font = "timesnewroman 14 bold", bd = 5, bg = "#254117", fg = "white").place(relx = 0.2,rely = 0.37)
    Entry(window,show = '*',textvariable = passwd9,font = "timesnewroman 15", width = 20, bd = 4).place(relx = 0.5,rely =0.37 )
    
    Label(window,text = "Confirm Password :", font = "timesnewroman 14 bold", bd = 5, bg = "#254117", fg = "white").place(relx = 0.2,rely = 0.47)
    Entry(window,show = "*",textvariable = cnfpass9,font = "timesnewroman 15", width = 20, bd = 4).place(relx =0.5 ,rely = 0.47)
    
    Label(window,text = "Email ID :", font = "timesnewroman 14 bold", bd = 5, bg = "#254117", fg = "white").place(relx = 0.2,rely = 0.57)
    Entry(window,textvariable = mail9,font = "timesnewroman 15", width = 20, bd = 4).place(relx = 0.5,rely = 0.57)
    
    Label(window,text = "Phone :", font = "timesnewroman 14 bold", bd = 5, bg = "#254117", fg = "white").place(relx = 0.2,rely = 0.67)
    Entry(window,textvariable = phone9,font = "timesnewroman 15", width = 20, bd = 4).place(relx =0.5 ,rely = 0.67)
    
    button = Button(window,text = "Register", bd = 5,state = DISABLED, relief = SUNKEN,font = "timesewroman 16 bold",bg = "#2B1B17",fg = "white", command = register, activebackground = "#3B3131", pady= 2, padx = 15  )
    button.place(relx = 0.42,rely = 0.80)
    Label(window,text = "All fields are mandatory!",bg = "#2B1B17",fg = "white",font = "timesnewroman 10 bold").place(relx = 0.4, rely = 0.74)
    p12 = Label(window,text = "**Password are not same!**",bg = "#FFFFFF",fg = "red",font = "Timesnewroman 8 bold")
    name9.trace('w',check)
    passwd9.trace('w',check) 
    cnfpass9.trace('w',check)
    mail9.trace('w',check)
    phone9.trace('w',check)
    ids9.trace('w',check)
    window.mainloop()

def retriveAdmin():
    window1 = Toplevel()
    window1.grab_set()
    window1.title("****RETRIVE ID/PASS****")
    window1.iconbitmap("icons/mainicon.ico")
    window1.focus_set()
    window1.geometry("520x400")
    window1.minsize(520,400)
    window1.maxsize(520,400)
    photo = ImageTk.PhotoImage(Image.open("login2.png"))
    cvs = Canvas(window1, width = 520, height = 400)
    cvs.pack(side = 'top')
    cvs.create_image(0,0,image = photo, anchor = 'nw')
    
    #====working======
    
    global forgotmail
    forgotmail = StringVar()
    
    Label(window1,text = "RETRIVING WINDOW", font = "gothic 16 bold", bd = 5, bg = "#0c090a", fg = "white").place(relx = 0.34,rely = 0.03,width = 200)
    Label(window1,text = "Enter Registered Email-Id", font = "timesnewroman 12 bold", bd = 5, bg = "#0c090a", fg = "yellow").place(relx = 0.34,rely = 0.2)
    

    Entry(window1,textvariable = forgotmail,font = "timesnewroman 12", width = 20, bd = 4).place(relx = 0.355,rely = 0.4)
    Button(window1, text = "Search", command = searchadmin,bd = 3,relief = SUNKEN, font = "timesnewromman 12 bold",bg = "white",fg = "red", activebackground = "#3B3131", pady= 2, padx = 10).place(relx = 0.44,rely = 0.6)
    window1.mainloop()

def retriveEmp():
    window2 = Toplevel()
    window2.grab_set()
    window2.title("****RETRIVE ID/PASS****")
    window2.iconbitmap("icons/mainicon.ico")
    window2.focus_set()
    window2.geometry("520x400")
    window2.minsize(520,400)
    window2.maxsize(520,400)
    photo = ImageTk.PhotoImage(Image.open("login2.png"))
    cvs = Canvas(window2, width = 520, height = 400)
    cvs.pack(side = 'top')
    cvs.create_image(0,0,image = photo, anchor = 'nw')
    
    #====working======
    
    global forgotmail1
    forgotmail1 = StringVar()
    
    Label(window2,text = "RETRIVING WINDOW", font = "gothic 16 bold", bd = 5, bg = "#0c090a", fg = "white").place(relx = 0.34,rely = 0.03,width = 200)
    Label(window2,text = "Enter Registered Email-Id", font = "timesnewroman 12 bold", bd = 5, bg = "#0c090a", fg = "yellow").place(relx = 0.34,rely = 0.2)
    

    Entry(window2,textvariable = forgotmail1,font = "timesnewroman 12", width = 20, bd = 4).place(relx = 0.355,rely = 0.4)
    Button(window2, text = "Search", command = searchemp,bd = 3,relief = SUNKEN, font = "timesnewromman 12 bold",bg = "white",fg = "red", activebackground = "#3B3131", pady= 2, padx = 10).place(relx = 0.44,rely = 0.6)
    window2.mainloop()

def register():
    a = name9.get()
    b = passwd9.get()
    c = ids9.get()
    d = phone9.get()
    f = mail9.get()

    try:
        sqlInsert(cur.execute("INSERT INTO ADMIN VALUES(?,?,?,?,?)",(c,b,a,d,f)))
        ms.showinfo("Registered", "Admin has been registered successfully!")
        window.destroy()
    except Exception as e:
        ms.showerror("Error", e)

#====================================image bg===================================== 

photo = ImageTk.PhotoImage(Image.open("loginmod.jpg"))
cvs = Canvas(root,width =w,  height = h)
cvs.pack(side = 'top')
cvs.create_image(0,0,image = photo, anchor = 'nw')

#=================================ICONS FOR BUTTONS AND LABLES============================================

icon1 = PhotoImage(file = "icons/admin.png")
icon2 = PhotoImage(file = "icons/employee.png")
icon3 = PhotoImage(file  = "icons/user.png")
icon4 = PhotoImage(file = "icons/password.png")
icon5 = PhotoImage(file = "icons/qrcode.png")

x1 = PhotoImage(file = "icons/inventory.png")
x2 = PhotoImage(file = "icons/addproduct.png")
x3 = PhotoImage(file = "icons/import.png")
x4 = PhotoImage(file = "icons/stats.png")
x5 = PhotoImage(file = "icons/sell.png")
x6 = PhotoImage(file = "icons/discount.png")
x7 = PhotoImage(file = "icons/logout.png")
x8 = PhotoImage(file = "icons/settings.png")

x9 = PhotoImage(file = "icons/whatsapp.png")
x10 = PhotoImage(file = "icons/mail.png")
x11 = PhotoImage(file = "icons/bill.png")
x12 = PhotoImage(file = "icons/barcode.png")
x13 = PhotoImage(file = "icons/id.png")

#===============================LOGIN PAGE======================================

def click(event): 
     
    global userentry,userentry1,userpassword,userpassword1,userid,password,userid1,password1  
    val = c1.get()
    userid = StringVar()
    password = StringVar()
    userid1 = StringVar()
    password1 = StringVar()


    
    
    #admin
    if val == "Admin":
            #trace function
        def check(*args):
            x =  userid.get()
            y = password.get()
            if len(x)>0 and len(y)>0 :
                b2['state'] = NORMAL           
            else:
               b2['state'] = DISABLED

        userentry = Entry(root,textvariable = userid,font = "timesnewroman 15", width = 20, bd = 4)
        userentry.place(relx = 0.50, rely = 0.56)
        userpassword = Entry(root,show = "*",textvariable = password,font = "timesnewroman 15", width = 20, bd = 4)
        userpassword.place(relx = 0.50, rely = 0.66)
        l3 = Label(root, image = icon1 , bg = "#151B54")
        l3.place(relx = 0.468, rely = 0.28)
        
        l4 = Label(root, text = "LOGIN AS ADMIN",padx = 40, font = "timesnewroman 20 bold",bd = 2, relief = GROOVE,  fg = 'black', bg = "grey")
        l4.place(relx = 0.418, rely =0.46 )  

        b2 = Button(root,state = DISABLED, text = "Login",bd = 5, relief = SUNKEN,font = "timesewroman 16 bold",bg = "#2B1B17",fg = "white", command = adm, activebackground = "#3B3131", pady= 5, padx = 15 )
        b2.place(relx = 0.48, rely = 0.76)
    
        l5 = Label(root, text = "USER ID",padx = 20,image = icon3,compound = LEFT, font = "timesnewroman 14 bold",fg = 'black', bg = "#d1d0ce")
        l5.place(relx = 0.37, rely =0.56)

        l6 = Label(root, text = "PASSWORD",padx = 8,image = icon4,compound = LEFT, font = "timesnewroman 14 bold",fg = 'black', bg = "#d1d0ce")
        l6.place(relx = 0.37, rely =0.66) 

        userid.trace("w",check)
        password.trace("w",check)

        if len(sqlAccess(cur.execute("select * from admin;"))) == 0:
            b4 = Button(root, text = "First User!",bd = 5,command = signup, relief = SUNKEN,font = "timesewroman 8 bold",bg = "#3B3131",fg = "white", pady= 1, padx = 38 )
            b4.place(relx = 0.468, rely = 0.84)
        else:
            b4 = Button(root, text = "Forgot ID/Password!",bd = 5,command = retriveAdmin, relief = SUNKEN,font = "timesewroman 8 bold",bg = "#3B3131",fg = "white", pady= 1, padx = 11 )
            b4.place(relx = 0.468, rely = 0.84)             
    
    
    #employee    
    elif val == "Employee":

        infolabel = Label(root, text = "If you are a new Employee, ask your owner for your registeration!",padx = 20,font = "timesnewroman 14 bold",fg = 'black', bg = "pink")
        infolabel.place(relx = 0.295,rely = 0.9)
          #trace function
        def checkbutton(*args):
            x1 =  userid1.get()
            y1 = password1.get()

            if len(x1)>0 and len(y1)>0:
                b1.config(state = NORMAL)     

            else:
                b1.config(state = DISABLED)

        l1 = Label(root, image = icon2 , bg = "#151B54")
        l1.place(relx = 0.468, rely = 0.28)
        
        l2 = Label(root, text = "LOGIN AS EMPLOYEE",padx = 10, font = "timesnewroman 20 bold",bd = 2, relief = GROOVE,  fg = 'black', bg = "grey")
        l2.place(relx = 0.418, rely =0.46 )  
        
        l5 = Label(root, text = "USER ID",padx = 20,image = icon3,compound = LEFT, font = "timesnewroman 14 bold",fg = 'black', bg = "#d1d0ce")
        l5.place(relx = 0.37, rely =0.56)

        l6 = Label(root, text = "PASSWORD",padx = 8,image = icon4,compound = LEFT, font = "timesnewroman 14 bold",fg = 'black', bg = "#d1d0ce")
        l6.place(relx = 0.37, rely =0.66) 
        
        b1 = Button(root, text = "Login",state = DISABLED,bd = 5, relief = SUNKEN,font = "timesewroman 16 bold",bg = "#2B1B17",fg = "white", command = selling, activebackground = "#3B3131", pady= 5, padx = 15 )
        b1.place(relx = 0.48, rely = 0.76)
                
        userentry1 = Entry(root,textvariable = userid1,font = "timesnewroman 15", width = 20, bd = 4)
        userentry1.place(relx = 0.50, rely = 0.56)
        
        userpassword1 = Entry(root,show = "*",textvariable = password1,font = "timesnewroman 15", width = 20, bd = 4)
        userpassword1.place(relx = 0.50, rely = 0.66)
        
        b5 = Button(root, text = "Forgot ID/Password!",command = retriveEmp,bd = 5, relief = SUNKEN,font = "timesewroman 8 bold",bg = "#3B3131",fg = "white", pady= 1, padx = 11 )
        b5.place(relx = 0.468, rely = 0.84)
        
        userid1.trace("w",checkbutton)
        password1.trace("w",checkbutton)

c1 = ttk.Combobox(root,height = 50,width = 20, state  = "readonly", font = "timesnewroman 16 ")
c1['values'] = ('Admin', 'Employee') 
c1.set("Select")
c1.bind("<<ComboboxSelected>>", click)
c1.place(relx = 0.43, rely =0.2 ) 

#===============ATTENDANCE BUTTON==================================

ab3 = Button(root, compound = TOP, image = icon5, text = "TAKE ATTENDANCE",bd = 5, relief = SUNKEN,font = "timesewroman 18 bold",bg = "#addfff",fg = "black", command = scanQR, activebackground = "#3B3131" )
ab3.place(relx = 0.1, rely = 0.3)
if sqlAccess(cur.execute("SELECT * FROM EMP")) == []:
    ab3.config(state = DISABLED)
else:
    pass

#=========================================================================================
root.mainloop()
