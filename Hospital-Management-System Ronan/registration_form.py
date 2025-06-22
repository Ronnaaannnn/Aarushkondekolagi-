from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
from database import get_db_connection

class Register:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="white")
        self.frame = Frame(self.master, bg="white")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text="REGISTRATION FORM", font="Helvetica 20 bold", bg="white", fg="red")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=400, height=80, relief="ridge", bg="white", bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="white", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblUsername = Label(self.LoginFrame1, text="Username", font="Helvetica 14 bold", bg="white", fg="red", bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.entryUsername = Entry(self.LoginFrame1, font="Helvetica 14 bold", textvariable=self.Username, bd=2)
        self.entryUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LoginFrame1, text="Password", font="Helvetica 14 bold", bg="white", fg="red", bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.entryPassword = Entry(self.LoginFrame1, font="Helvetica 14 bold", show="*", textvariable=self.Password, bd=2)
        self.entryPassword.grid(row=1, column=1)

        self.btnRegister = Button(self.LoginFrame2, text="Register", font="Helvetica 10 bold", width=10, bg="blue", fg="white", command=self.register_system)
        self.btnRegister.grid(row=3, column=0)
        self.btnExit = Button(self.LoginFrame2, text="Exit", font="Helvetica 10 bold", width=10, bg="blue", fg="white", command=self.exit)
        self.btnExit.grid(row=3, column=1)

    def register_system(self):
        username = self.Username.get()
        password = self.Password.get()

        if not username or not password:
            tkinter.messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", "Username and password cannot be empty.")
            return

        conn = get_db_connection()
        c = conn.cursor()

        c.execute("SELECT * FROM USERS WHERE USERNAME=?", (username,))
        if c.fetchone():
            tkinter.messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", "Username already exists.")
        else:
            c.execute("INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)", (username, password))
            conn.commit()
            tkinter.messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM", "Registration successful.")
            self.master.destroy()

        conn.close()

    def exit(self):
        self.master.destroy()

def main():
    root = Tk()
    app = Register(root)
    root.mainloop()

if __name__ == "__main__":
    main() 