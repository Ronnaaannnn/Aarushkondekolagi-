from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

from menu import MainMenu
from registration_form import Register
from database import get_db_connection

def main():
    root = Tk()
    app= MainWindow(root)
    root.mainloop()
#MAIN WINDOW FOR LOG IN
class MainWindow:
    # constructor
    def __init__(self,master):
        # public data mambers
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="white")
        self.frame = Frame(self.master,bg="white")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame,text = "HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold",bg="white",fg="red")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=40)
        #======================
        self.LoginFrame1 = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame1.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="white",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #======LABEL AND ENTRY=========
        self.lblUsername = Label(self.LoginFrame1,text="Username",font="Helvetica 14 bold",bg="white",fg="red",bd=22)
        self.lblUsername.grid(row=0,column=0)
        self.lblUsername = Entry(self.LoginFrame1,font="Helvetica 14 bold",textvariable= self.Username,bd=2)
        self.lblUsername.grid(row=0,column=1)
        self.lblPassword = Label(self.LoginFrame1,text="Password ",font="Helvetica 14 bold",bg="white",fg="red",bd=22)
        self.lblPassword .grid(row=1,column=0)
        self.lblPassword  = Entry(self.LoginFrame1,font="Helvetica 14 bold",show="*",textvariable= self.Password,bd=2)
        self.lblPassword .grid(row=1,column=1)
        #===========BUTTONS====
        self.btnLogin = Button(self.LoginFrame2,text = "Login" ,font="Helvetica 10 bold", width =10 ,bg="blue",fg="white",command = self.Login_system)
        self.btnLogin.grid(row=3,column=0)
        self.btnExit = Button(self.LoginFrame2,text = "Exit" ,font="Helvetica 10 bold", width =10 ,bg="blue",fg="white",command = self.Exit)
        self.btnExit.grid(row=3,column=1)

        self.btnRegister = Button(self.LoginFrame2, text="Register", font="Helvetica 10 bold", width=10, bg="blue",fg="white", command=self.open_registration)
        self.btnRegister.grid(row=3, column=2)

    def open_registration(self):
        self.newWindow = Toplevel(self.master)
        self.app = Register(self.newWindow)

    # public member function
    #Function for LOGIN
    def Login_system(self):
        S1=(self.Username.get())
        S2=(self.Password.get())

        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD=?", (S1, S2))
        result = c.fetchone()
        conn.close()

        if result:
            self.newWindow = Toplevel(self.master)
            self.app = MainMenu(self.newWindow)
        else:
            tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM" , "PLEASE ENTER VALID USERNAME AND PASSWORD")
    #Function for Exit
    def Exit(self):
        self.master.destroy()




if __name__ == "__main__":
    main()
