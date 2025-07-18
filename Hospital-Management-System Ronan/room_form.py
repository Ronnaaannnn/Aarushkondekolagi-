from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
from database import get_db_connection

#Class for ROOM ALLOCATION    
class Room:
    
    def __init__(self,master):

        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="white")
        self.frame = Frame(self.master,bg="white")
        self.frame.pack()

        #=============ATTRIBUTES===========
        self.P_id=StringVar()
        self.room_t=StringVar()
        self.room_no=StringVar()
        self.rate=StringVar()
        self.da=StringVar()
        self.dd=StringVar()
      
        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "ROOM ALLOCATION FORM", font="Helvetica 20 bold",bg="white", fg="red")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.P_id)
        self.lblpatid.grid(row=0,column=1)
        self.room_t1= Label(self.LoginFrame,text="ROOM TYPE\nSINGLE ROOM: Rs 4500\nTWIN SHARING : Rs2500\nTRIPLE SHARING: Rs2000\n",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
        self.room_t1.grid(row=1,column=0)
        self.room_t1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.room_t)
        self.room_t1.grid(row=1,column=1)
        
        self.room_no1=Label(self.LoginFrame,text="ROOM NUMBER ",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
        self.room_no1.grid(row=2,column=0)

        self.room_no1 = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.room_no)
        self.room_no1.grid(row=2,column=1)
        self.lblrate=Label(self.LoginFrame,text="ROOM CHARGES",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
        self.lblrate.grid(row=0,column=2)
        self.lblrate=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.rate)
        self.lblrate.grid(row=0,column=3)
        self.lblda=Label(self.LoginFrame,text="DATE ADMITTED",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
        self.lblda.grid(row=1,column=2)
        self.lblda=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.da)
        self.lblda.grid(row=1,column=3)
        self.lbldd=Label(self.LoginFrame,text="DATE DISCHARGED",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
        self.lbldd.grid(row=2,column=2)
        self.lbldd=Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.dd)
        self.lbldd.grid(row=2,column=3)
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SUBMIT",width =10,font="Helvetica 14 bold",bg="blue", fg="white",command=self.INSERT_ROOM)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="UPDATE",width =10,font="Helvetica 14 bold",bg="blue", fg="white",command=self.UPDATE_ROOM)
        self.button3.grid(row=3,column=2)
        
        self.button5 = Button(self.LoginFrame2, text="ROOM DETAILS",width =15,font="Helvetica 14 bold",bg="blue", fg="white",command=self.SEARCH_ROOM)
        self.button5.grid(row=3,column=4)
        
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="blue", fg="white",command = self.Exit)
        self.button6.grid(row=3,column=5)
        
    #FUNCTION TO INSERT DATA IN ROOM ALLOCATION FORM
    def INSERT_ROOM(self):
        try:
            p_id = int(self.P_id.get())
            rate = int(self.rate.get())
        except (ValueError, TclError):
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "Please enter valid numbers for Patient ID and Room Charges.")
            return

        conn = get_db_connection()
        c = conn.cursor()
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = list(c.execute("SELECT * FROM ROOM WHERE ROOM_NO=?",(r3,)))
        x=len(p)
        if x!=0:
             tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","ROOM_NO IS CURRENTLY OCCUPIED")
        else:
            c.execute('INSERT INTO ROOM VALUES(?,?,?,?,?,?)',(p_id,r3, r2, rate, r5, r6,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM ALLOCATED")
        conn.commit()
        conn.close()
            
    #FUNCTION TO OPEN SEARCH MENU IN ROOM ALLOCATION FORM
    def SEARCH_ROOM(self):
        self.newWindow= Toplevel(self.master)
        self.app = S_Room(self.newWindow)
        
    #FUNCTION TO EXIT ROOM ALLOCATION FORM
    def Exit(self):            
        self.master.destroy()   

    #FUNCTION TO UPDATE DATA IN ROOM ALLOCATION FORM       
    def UPDATE_ROOM(self):
        try:
            p_id = int(self.P_id.get())
            rate = int(self.rate.get())
        except (ValueError, TclError):
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "Please enter valid numbers for Patient ID and Room Charges.")
            return

        conn = get_db_connection()
        c = conn.cursor()
        r2=(self.room_t.get())
        r3=(self.room_no.get())
        r5=(self.da.get())
        r6=(self.dd.get())
        p = list(c.execute("Select * from ROOM where PATIENT_ID=? AND ROOM_NO=?",(p_id,r3,)))
        if len(p) == 0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "PATIENT IS NOT ALLOCATED THIS ROOM")
        else:
            c.execute('UPDATE ROOM SET ROOM_TYPE=?,RATE=?,DATE_ADMITTED=?,DATE_DISCHARGED=? where PATIENT_ID=?',(r2, rate, r5, r6, p_id,))
            tkinter.messagebox.showinfo("HOSPITAL DATABSE SYSTEM", "ROOM DETAILS UPDATED")
        conn.commit()
        conn.close()

#CLASS FOR DISPLAY MENU FOR SEARCH ROOM
class S_Room:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="white")
        self.frame = Frame(self.master,bg="white")
        self.frame.pack()
        self.Pr_id=StringVar()
        self.lblTitle = Label(self.frame,text = "SEARCH PATIENT DETAILS", font="Helvetica 20 bold",bg="white", fg="red")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER PATIENT ID TO SEARCH",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.Pr_id)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="blue", fg="white",command = self.ROOM_DISPLAY)
        self.SearchB.grid(row=0,column=1)    

    #FUNCTION TO SEARCH DATA IN ROOM ALLOCATION FORM
    def ROOM_DISPLAY(self):
        try:
            pat_rm = int(self.Pr_id.get())
        except (ValueError, TclError):
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "Please enter a valid Patient ID.")
            return

        conn = get_db_connection()
        c = conn.cursor()
        p=list(c.execute('select * from  ROOM  where PATIENT_ID=?',(pat_rm,)))
        if (len(p)==0):
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM","PATIENT NOT ALLOCATED ROOM")
        else:
            t=c.execute('SELECT PATIENT_ID,NAME,ROOM_NO,ROOM_TYPE FROM ROOM NATURAL JOIN PATIENT where PATIENT_ID=?',(pat_rm,));
            for i in t:
            
                self.l1 = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
                self.l1.grid(row=1,column=0)
                self.dis1= Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="white", fg="red",text=i[0])
                self.dis1.grid(row=1,column=1)
                        
                self.l2 = Label(self.LoginFrame,text="PATIENT NAME",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
                self.l2.grid(row=2,column=0)
                self.dis2=Label(self.LoginFrame,font="Helvetica 14 bold",bd=2,bg="white", fg="red",text=i[1])
                self.dis2.grid(row=2,column=1)

                self.l3 = Label(self.LoginFrame,text="ROOM NO",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
                self.l3.grid(row=1,column=2)
                self.dis3= Label(self.LoginFrame,font="Helvetica 14 bold",bg="white", fg="red",bd=2,text=i[2])
                self.dis3.grid(row=1,column=3)

                self.l4 = Label(self.LoginFrame,text="ROOM TYPE",font="Helvetica 14 bold",bg="white", fg="red",bd=22)
                self.l4.grid(row=2,column=2)
                self.dis4= Label(self.LoginFrame,font="Helvetica 14 bold",bg="white", fg="red",bd=2,text=i[3])
                self.dis4.grid(row=2,column=3)                 
                       

  
