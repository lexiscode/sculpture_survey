from tkinter import *
from tkinter import ttk
import sqlite3


def database_win():
    base_win = Tk()
    base_win.resizable(False, False)
    base_win.maxsize(1355, 690)
    base_win.config(padx=15, pady=15, bg="green")
    base_win.title("Admin Panel")

    # Using treeview widget
    treev = ttk.Treeview(base_win, selectmode='browse')

    # Calling pack method w.r.to treeview
    treev.pack(side=RIGHT)

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(base_win, orient="vertical", command=treev.yview)

    # Calling pack method w.r.to vertical scrollbar
    verscrlbar.pack(side=RIGHT, fill=BOTH)

    # Configuring treeview
    treev.configure(xscrollcommand=verscrlbar.set)

    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to the respective columns
    treev.column("1", width=45, anchor=CENTER)
    treev.column("2", width=90, anchor=CENTER)
    treev.column("3", width=90, anchor=CENTER)
    treev.column("4", width=90, anchor=CENTER)
    treev.column("5", width=90, anchor=CENTER)
    treev.column("6", width=90, anchor=CENTER)
    treev.column("7", width=100, anchor=CENTER)
    treev.column("8", width=120, anchor=CENTER)
    treev.column("9", width=90, anchor=CENTER)
    treev.column("10", width=90, anchor=CENTER)
    treev.column("11", width=90, anchor=CENTER)
    treev.column("12", width=90, anchor=CENTER)
    treev.column("13", width=90, anchor=CENTER)
    treev.column("14", width=45, anchor=CENTER)
    treev.column("15", width=45, anchor=CENTER)
    treev.column("16", width=45, anchor=CENTER)

    # Assigning the heading names to the respective columns
    treev.heading("1", text="#ID")
    treev.heading("2", text="FIRST NAME")
    treev.heading("3", text="LAST NAME")
    treev.heading("4", text="MIDDLE NAME")
    treev.heading("5", text="D.O.B")
    treev.heading("6", text="GENDER")
    treev.heading("7", text="MARITAL STATUS")
    treev.heading("8", text="ADDRESS")
    treev.heading("9", text="CITY")
    treev.heading("10", text="STATE")
    treev.heading("11", text="PHONE NO.")
    treev.heading("12", text="JOB STATUS")
    treev.heading("13", text="RELIGION")
    treev.heading("14", text="#Q1")
    treev.heading("15", text="#Q2")
    treev.heading("16", text="#Q3")

    # connect to the database
    query_conn = sqlite3.connect("survey_record.db")
    query_c = query_conn.cursor()
    # query the database
    query_c.execute("SELECT *, oid FROM form_details")
    records = query_c.fetchall()

    x = 0
    for record in records:
        x = x + 1
        treev.insert("", 'end', text=f"L{x}",
                     values=(str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4]),
                             str(record[5]), str(record[6]), str(record[7]), str(record[8]), str(record[9]),
                             str(record[10]), str(record[11]), str(record[12]), str(record[13]), str(record[14]),
                             str(record[15])))

    '''
    # syntax below
    # Inserting the items and their features to the columns built
    treev.insert("", 'end', text="L1", values=("1", "Alex", "Nwokorie", "Vincent", "14/06/2020", "Male", "Single",
                                               "2 Oremeji Street", "Akoka", "Lagos", "09023959933", "Employed",
                                               "Christian", "2", "4", "1"))

    '''

    # commit changes
    query_conn.commit()
    # close connection
    query_conn.close()
