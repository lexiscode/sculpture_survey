from tkinter import *
import sqlite3
from tkcalendar import DateEntry
from tkinter import ttk


# submit to database
def submit():
    # create a database or connect to one
    submit_conn = sqlite3.connect("survey_record.db")
    # create cursor
    submit_c = submit_conn.cursor()
    # insert into table
    submit_c.execute("INSERT INTO from_details VALUES "
                     "(:first_name, :last_name, :middle_name, :home_address, :date_of_birth, :gender_option, :marital_status, "
                     ":city, :state, :phone_no, :employment_status, :religion, :scale_1, :scale_2, scale_3)",
                     {
                         "first_name": first_name.get(),
                         "last_name": last_name.get(),
                         "middle_name": middle_name.get(),
                         "home_address": home_address.get(),
                         "date_of_birth": date_of_birth.get(),
                         "gender_option": gender_option.get(),
                         "marital_status": marital_status.get(),
                         "city": city.get(),
                         "state": state.get(),
                         "phone_no": phone_no.get(),
                         "employment_status": employment_status.get(),
                         "religion": religion.get(),
                         "scale_1": scale_1.get(),
                         "scale_2": scale_2.get(),
                         "scale_3": scale_3.get()
                     })
    # commit changes
    submit_conn.commit()
    # close connection
    submit_conn.close()
    # clear the textboxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    middle_name.delete(0, END)
    home_address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    phone_no.delete(0, END)


def connect_database():
    database = Tk()
    database.resizable(False, False)
    database.minsize(1000, 1000)
    database.config(padx=15, pady=15, bg="green")
    database.title("Database Information")

    # create a database or connect to one
    conn = sqlite3.connect("survey_record.db")
    # create cursor
    c = conn.cursor()
    # create table
    c.execute(""""CREATE TABLE form_details(
        first_name text, last_name text, middle_name text, home_address text, date_of_birth date,
        gender_option text, marital_status text, home_address text, city text, state text, phone_no integer, 
        employment_status text, religion text, scale_1 integer, scale_2 integer, scale_3 integer
        )""")


def demo_graph():
    demo = Tk()
    demo.resizable(False, False)
    demo.minsize(1000, 530)
    # demo.geometry("1000x530")
    demo.config(padx=15, pady=15, bg="green")
    demo.title("Form Fill")

    # Create global scope for textbox entries
    # this helps define the variables below in order for them to be able to be used above
    global first_name, last_name, middle_name, date_of_birth, gender_option, marital_status, home_address, city, state, phone_no, \
        employment_status, religion, scale_1, scale_2, scale_3, satisfactory_btn

    # SATISFACTORY SURVEY HEADING
    Label(demo, text="SATISFACTORY SURVEY", fg="white", bg="green", font=("Lucida", 40, "bold")).grid(row=0, column=0,
                                                                                                      columnspan=5,
                                                                                                      pady=(10, 0))

    # APPRECIATION HEADING
    Label(demo, text="Thank you for taking the time to help us improve this platform!", fg="white", bg="green",
          font=("Lucida", 10, "bold")).grid(row=1, column=0, columnspan=5, pady=(10, 0))

    # SECTION 1 - DEMOGRAPHICS FORM #
    label_frame = LabelFrame(demo, text="FILL THE DEMOGRAPHICS FORM", bg="green", fg="white", bd=3, labelanchor=NW)
    label_frame.grid(row=2, column=0, columnspan=5, pady=(10, 0))

    # Create firstname, lastname and middle name labels and entries
    Label(label_frame, text="First Name", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=0, column=0,
                                                                                                    pady=(10, 0),
                                                                                                    padx=30)
    first_name = Entry(label_frame, width=30)
    first_name.grid(row=0, column=1, padx=20, pady=(10, 0))

    Label(label_frame, text="Last Name", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=0, column=2,
                                                                                                   pady=(10, 0))
    last_name = Entry(label_frame, width=30)
    last_name.grid(row=0, column=3, padx=20, pady=(10, 0))

    Label(label_frame, text="Middle Name", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=0, column=4,
                                                                                                     pady=(10, 0))
    middle_name = Entry(label_frame, width=30)
    middle_name.grid(row=0, column=5, padx=20, pady=(10, 0))

    # Create a Date setup calendar using DateEntry
    Label(label_frame, text="Date of Birth", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=1, column=0,
                                                                                                       pady=(10, 0))
    date_of_birth = DateEntry(label_frame, width=27)
    date_of_birth.grid(row=1, column=1, padx=10, pady=(10, 0))

    # Create a Gender option
    Label(label_frame, text="Gender", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=1, column=2,
                                                                                                pady=(10, 0))
    n = StringVar()
    gender_option = ttk.Combobox(label_frame, width=27, textvariable=n)
    gender_option['values'] = ('--Select Gender--', 'Male', 'Female')
    gender_option.grid(row=1, column=3, padx=10, pady=(10, 0))
    gender_option.current(0)

    # Marital Status
    Label(label_frame, text="Marital Status", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=1, column=4,
                                                                                                        pady=(10, 0))
    n = StringVar()
    marital_status = ttk.Combobox(label_frame, width=27, textvariable=n)
    marital_status['values'] = ('Single', 'Married', 'Widowed', 'Divorced')
    marital_status.grid(row=1, column=5, padx=10, pady=(10, 0))
    marital_status.current(0)

    # Create home address fill
    Label(label_frame, text="Home Address", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=2, column=0,
                                                                                                      pady=(10, 0))
    home_address = Entry(label_frame, width=30)
    home_address.grid(row=2, column=1, padx=20, pady=(10, 0))
    # Create city fill
    Label(label_frame, text="City", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=2, column=2,
                                                                                              pady=(10, 0))
    city = Entry(label_frame, width=30)
    city.grid(row=2, column=3, padx=20, pady=(10, 0))
    # Create state fill
    Label(label_frame, text="State", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=2, column=4,
                                                                                               pady=(10, 0))
    state = Entry(label_frame, width=30)
    state.grid(row=2, column=5, padx=20, pady=(10, 0))

    # Create phone number fill
    Label(label_frame, text="Phone No.", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=3, column=0,
                                                                                                   pady=(10, 0))
    phone_no = Entry(label_frame, width=30)
    phone_no.grid(row=3, column=1, padx=20, pady=(10, 0))

    # Create employment status
    Label(label_frame, text="Employment Status", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=3,
                                                                                                           column=2,
                                                                                                           pady=(10, 0))
    employment_var = StringVar()
    employment_status = ttk.Combobox(label_frame, width=27, textvariable=employment_var)
    employment_status['values'] = ('Unemployed', 'Self-employed', 'Working Staff')
    employment_status.grid(row=3, column=3, padx=10, pady=(10, 0))
    employment_status.current(0)

    # Create state fill
    Label(label_frame, text="Religion", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=3, column=4,
                                                                                                  pady=(10, 0))
    religion_var = StringVar()
    religion = ttk.Combobox(label_frame, width=27, textvariable=religion_var)
    religion['values'] = ('Christian', 'Muslim')
    religion.grid(row=3, column=5, padx=10, pady=(10, 0))
    religion.current(0)

    # SECTION 2 - PSYCHOLOGY FORM
    label_frame = LabelFrame(demo, text="FILL THE PSYCHOLOGY FORM", bg="green", fg="white", bd=3, labelanchor=NW,
                             width=1000)
    label_frame.grid(row=3, column=0, columnspan=5, pady=(10, 0))
    labeltext_inside = Label(label_frame,
                             text="This is the numerical representation in order to fill this section below:"
                                  " 1 Strongly Agree, 2 Agree, 3 Neither Agree, 4 Disagree and 5 Strongly Disagree")
    labeltext_inside.grid(row=0, column=0, columnspan=5, padx=50, pady=(10, 0))

    # First scale
    Label(label_frame, text="Do you enjoy the sculpture?", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(
        row=1, column=0, columnspan=2, pady=(10, 0))
    scale_1 = Scale(label_frame, from_=1, to=5, orient=HORIZONTAL, bg="black", fg="white", activebackground="green")
    scale_1.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky='NSEW')

    # Second scale
    Label(label_frame, text="Were you curious as to how it worked?", fg="white", bg="green",
          font=("Lucida", 10, "bold")).grid(
        row=1, column=2, columnspan=2, pady=(10, 0))
    scale_2 = Scale(label_frame, from_=1, to=5, orient=HORIZONTAL, bg="black", fg="white", activebackground="green")
    scale_2.grid(row=2, column=2, columnspan=2, pady=(10, 0), sticky='NSEW')

    # Third scale
    Label(label_frame, text="Want to know more about science as a result?", fg="white", bg="green",
          font=("Lucida", 10, "bold")).grid(
        row=1, column=4, columnspan=2, pady=(10, 0))
    scale_3 = Scale(label_frame, from_=1, to=5, orient=HORIZONTAL, bg="black", fg="white", activebackground="green")
    scale_3.grid(row=2, column=4, columnspan=2, pady=(10, 0), sticky='NSEW')

