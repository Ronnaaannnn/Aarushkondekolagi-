from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
from database import get_db_connection

class PatientInfo:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Information")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="white")
        self.frame = Frame(self.master, bg="white")
        self.frame.pack(fill=BOTH, expand=True)

        self.lblTitle = Label(self.frame, text="Search Patient", font="Helvetica 20 bold", bg="white", fg="red")
        self.lblTitle.pack(pady=5)

        search_frame = Frame(self.frame, bg="white")
        search_frame.pack(pady=10)

        self.search_label = Label(search_frame, text="Search by Patient ID or Name:", font="Helvetica 12 bold", bg="white", fg="red")
        self.search_label.grid(row=0, column=0, padx=5, pady=5)

        self.search_var = StringVar()
        self.search_entry = Entry(search_frame, textvariable=self.search_var, width=30, font="Helvetica 12")
        self.search_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = Button(search_frame, text="Search", command=self.search_patient, bg="blue", fg="white", font="Helvetica 12 bold")
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        tree_frame = Frame(self.frame)
        tree_frame.pack(pady=10, padx=10, fill=BOTH, expand=True)

        tree_scroll_y = Scrollbar(tree_frame)
        tree_scroll_y.pack(side=RIGHT, fill=Y)
        tree_scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)
        tree_scroll_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set, height=25)
        self.tree['columns'] = ("Patient ID", "Name", "Sex", "DOB", "Address", "Room No", "Room Type", "Date Admitted", "Date Discharged")

        tree_scroll_y.config(command=self.tree.yview)
        tree_scroll_x.config(command=self.tree.xview)

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Patient ID", anchor=W, width=80)
        self.tree.column("Name", anchor=W, width=150)
        self.tree.column("Sex", anchor=W, width=80)
        self.tree.column("DOB", anchor=W, width=100)
        self.tree.column("Address", anchor=W, width=200)
        self.tree.column("Room No", anchor=W, width=100)
        self.tree.column("Room Type", anchor=W, width=100)
        self.tree.column("Date Admitted", anchor=W, width=120)
        self.tree.column("Date Discharged", anchor=W, width=120)

        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Patient ID", text="Patient ID", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Sex", text="Sex", anchor=W)
        self.tree.heading("DOB", text="DOB", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Room No", text="Room No", anchor=W)
        self.tree.heading("Room Type", text="Room Type", anchor=W)
        self.tree.heading("Date Admitted", text="Date Admitted", anchor=W)
        self.tree.heading("Date Discharged", text="Date Discharged", anchor=W)

        self.tree.pack(fill=BOTH, expand=True)
        self.load_data()

    def search_patient(self):
        search_query = self.search_var.get()
        self.load_data(search_query)

    def load_data(self, search_query=None):
        conn = get_db_connection()
        c = conn.cursor()
        
        query = """
            SELECT
                p.PATIENT_ID, p.NAME, p.SEX, p.DOB, p.ADDRESS,
                r.ROOM_NO, r.ROOM_TYPE, r.DATE_ADMITTED, r.DATE_DISCHARGED
            FROM PATIENT p
            LEFT JOIN ROOM r ON p.PATIENT_ID = r.PATIENT_ID
        """

        if search_query:
            query += " WHERE p.PATIENT_ID LIKE ? OR p.NAME LIKE ?"
            params = ('%' + search_query + '%', '%' + search_query + '%')
            c.execute(query, params)
        else:
            c.execute(query)

        rows = c.fetchall()
        conn.close()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in rows:
            self.tree.insert(parent='', index='end', values=row)

if __name__ == '__main__':
    root = Tk()
    app = PatientInfo(root)
    root.mainloop() 