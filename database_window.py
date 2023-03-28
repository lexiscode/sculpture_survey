from tkinter import *
from tkinter import ttk
import sqlite3
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def database_win():
    base_win = Tk()
    base_win.resizable(False, False)
    base_win.minsize(1356, 700)
    base_win.config(padx=15, pady=15, bg="white")
    base_win.title("Admin Panel")

    # SATISFACTORY SURVEY HEADING
    Label(base_win, text="DATABASE DASHBOARD", fg="green", bg="white", font=("Lucida", 20, "bold")).grid(row=0, column=0, columnspan=10)

    # PIE CHART - STATS
    my_dict = {'NAME': ['Excellent', 'Good', 'Poor', 'Very Poor'], '%': [30, 40, 50, 50]}
    df = pd.DataFrame(data=my_dict)
    lbl = ['Excellent', 'Good', 'Poor', 'Very Poor']
    fig1 = df.plot.pie(title="Stats Chart", y='%', figsize=(2.5, 2), labels=lbl).get_figure()

    plot1 = FigureCanvasTkAgg(fig1, base_win)
    plot1.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # QUERY LABELFRAME #
    labelframe1 = LabelFrame(base_win, text="Select the options you will like to view results for:")
    labelframe1.grid(row=1, column=2, columnspan=2, padx=5, pady=(10, 0))
    # AGE SUB-LABELFRAME
    age_labelframe = LabelFrame(labelframe1, text="AGE:")
    age_labelframe.grid(row=0, column=0, columnspan=2, padx=5, pady=(10, 0))

    var = StringVar(age_labelframe)
    R1 = Radiobutton(age_labelframe, text="Below 25", variable=var, value="1")
    R1.pack(side=LEFT)
    R2 = Radiobutton(age_labelframe, text="Between 25 and 45", variable=var, value="2")
    R2.pack(side=LEFT)
    R3 = Radiobutton(age_labelframe, text="Above 45", variable=var, value="3")
    R3.pack(side=LEFT)
    # GENDER SUB-LABELFRAME
    gender_labelframe = LabelFrame(labelframe1, text="GENDER:")
    gender_labelframe.grid(row=1, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    gender_list = ["Male", "Female"]
    gender_value_inside = StringVar(gender_labelframe)
    gender_value_inside.set("--Click to Select Gender--")
    gender_drop = OptionMenu(gender_labelframe, gender_value_inside, *gender_list)
    gender_drop.pack(side=LEFT, fill=X, expand=TRUE)
    # STATE SUB-LABELFRAME
    state_labelframe = LabelFrame(labelframe1, text="STATE:")
    state_labelframe.grid(row=2, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    state_list = ["Lagos", "Abuja", "Rivers", "Imo"]
    state_value_inside = StringVar(state_labelframe)
    state_value_inside.set("--Click to Select State--")
    state_drop = OptionMenu(state_labelframe, state_value_inside, *state_list)
    state_drop.pack(side=LEFT, fill=X, expand=TRUE)

    # SUBMIT BUTTON
    stats_btn = Button(labelframe1, text="Submit", bd=3, fg="white", bg="black", font="Times")
    stats_btn.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    # -- STATISTICS QUERY LABELFRAME 1 -- #
    labelframe3 = LabelFrame(base_win, text="Showing results for selected options:")
    labelframe3.grid(row=1, column=4, columnspan=2, padx=5, pady=(10, 0))
    # Total Number of Tourists SUB-LABELFRAME
    liked_stat_labelframe = LabelFrame(labelframe3, text="Total Number of Tourists:")
    liked_stat_labelframe.grid(row=0, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    Label(liked_stat_labelframe, text="50").pack(side=LEFT, fill=X, expand=TRUE)

    # Percentage of Selected Gender  SUB-LABELFRAME
    curious_stat_labelframe = LabelFrame(labelframe3, text="Percentage of Selected Gender:")
    curious_stat_labelframe.grid(row=1, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    Label(curious_stat_labelframe, text="50").pack(side=LEFT, fill=X, expand=TRUE)

    # Percentage of Selected State Residents SUB-LABELFRAME
    interested_stat_labelframe = LabelFrame(labelframe3, text="Percentage of Selected Sate Residents:")
    interested_stat_labelframe.grid(row=2, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    Label(interested_stat_labelframe, text="50").pack(side=LEFT, fill=X, expand=TRUE)

    # -- STATISTICS QUERY LABELFRAME 2 -- #
    labelframe3 = LabelFrame(base_win, text="Showing results for selected options:")
    labelframe3.grid(row=1, column=6, columnspan=2, padx=5, pady=(10, 0))
    # Avg No. who liked the sculpture SUB-LABELFRAME
    liked_stat_labelframe = LabelFrame(labelframe3, text="Avg No. of those who liked the sculpture:")
    liked_stat_labelframe.grid(row=0, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    Label(liked_stat_labelframe, text="1000").pack(side=LEFT, fill=X, expand=TRUE)

    # Avg people curious  SUB-LABELFRAME
    curious_stat_labelframe = LabelFrame(labelframe3, text="Avg No. of people curious as to how it worked:")
    curious_stat_labelframe.grid(row=1, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    Label(curious_stat_labelframe, text="50").pack(side=LEFT, fill=X, expand=TRUE)

    # Avg people interested in science SUB-LABELFRAME
    interested_stat_labelframe = LabelFrame(labelframe3, text="Avg No. of people interested about the science of acoustics:")
    interested_stat_labelframe.grid(row=2, column=0, columnspan=2, padx=5, pady=(10, 0), sticky='nwne')

    Label(interested_stat_labelframe, text="50").pack(side=LEFT, fill=X, expand=TRUE)



    # Using TREEVIEW widget
    treev = ttk.Treeview(base_win, selectmode='browse')
    # Calling pack method w.r.to treeview
    treev.grid(row=2, rowspan=2, columnspan=7, padx=10, pady=(10, 0))
    # Constructing vertical scrollbar with treeview
    verscrlbar = ttk.Scrollbar(base_win, orient="vertical", command=treev.yview)
    # Calling pack method w.r.to vertical scrollbar
    verscrlbar.grid(row=2, rowspan=2, column=8, sticky=NS, pady=(10, 0))
    # Configuring treeview
    treev.configure(yscrollcommand=verscrlbar.set)
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
    treev.insert("", 'end', text="L1", values=("#ID", "First Name", "Last Name", "Middle Name", "Date of Birth", "Gender", 
                "Marital Status", "Street Address", "City", "State", "Phone No.", "Employed", "Religion", "Q1", "Q2", "Q3"))

    '''

    # commit changes
    query_conn.commit()
    # close connection
    query_conn.close()

    # Tourist ID Number
    user_id = Entry(base_win, width=10, justify=CENTER)
    user_id.grid(row=4, column=0, columnspan=8, pady=(10, 0))
    user_id.insert(0, "Tourist #ID:")

    # EDIT/UPDATE BUTTON
    edit_btn = Button(base_win, text="EDIT RECORD", bd=5, fg="white", bg="red", relief=GROOVE, font="Times")
    edit_btn.grid(row=5, column=3, pady=(20, 0), sticky='nwne')

    # DELETE BUTTON
    delete_btn = Button(base_win, text="DELETE RECORD", bd=5, fg="white", bg="red", relief=GROOVE, font="Times")
    delete_btn.grid(row=5, column=4, pady=(20, 0), sticky='nwne')
