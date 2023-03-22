from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk


def demo_graph():
    demo = Tk()
    demo.resizable(0, 0)
    demo.minsize(1000, 1000)
    # demo.geometry("1000x1000")
    demo.config(padx=15, pady=15, bg="green")
    demo.title("Form Fill")

    # Create firstname, lastname and middle name labels and entries
    Label(demo, text="First Name", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=0, column=0, pady=(10, 0))
    first_name = Entry(demo, width=30)
    first_name.grid(row=0, column=1, padx=20, pady=(10, 0))

    Label(demo, text="Last Name", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=0, column=2, pady=(10, 0))
    last_name = Entry(demo, width=30)
    last_name.grid(row=0, column=3, padx=20, pady=(10, 0))

    Label(demo, text="Middle Name", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=0, column=4, pady=(10, 0))
    middle_name = Entry(demo, width=30)
    middle_name.grid(row=0, column=5, padx=20, pady=(10, 0))

    # Create a Date setup calendar using DateEntry
    Label(demo, text="Date of Birth", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=1, column=0, pady=(10, 0))
    cal = DateEntry(demo, width=27)
    cal.grid(row=1, column=1, padx=10, pady=(10, 0))

    # Create a Gender option
    Label(demo, text="Gender", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=1, column=2, pady=(10, 0))
    n = StringVar()
    gender_option = ttk.Combobox(demo, width=27, textvariable=n)
    gender_option['values'] = ('Male', 'Female')
    gender_option.grid(row=1, column=3, padx=10, pady=(10, 0))
    gender_option.current(0)

    # Marital Status
    Label(demo, text="Marital Status", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=1, column=4, pady=(10, 0))
    n = StringVar()
    marital_status = ttk.Combobox(demo, width=27, textvariable=n)
    marital_status['values'] = ('Single', 'Married', 'Widowed', 'Divorced')
    marital_status.grid(row=1, column=5, padx=10, pady=(10, 0))
    marital_status.current(0)

    # Create home address fill
    Label(demo, text="Home Address", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=2, column=0, pady=(10, 0))
    home_address = Entry(demo, width=30)
    home_address.grid(row=2, column=1, padx=20, pady=(10, 0))
    # Create city fill
    Label(demo, text="City", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=2, column=2, pady=(10, 0))
    city = Entry(demo, width=30)
    city.grid(row=2, column=3, padx=20, pady=(10, 0))
    # Create state fill
    Label(demo, text="State", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=2, column=4, pady=(10, 0))
    state = Entry(demo, width=30)
    state.grid(row=2, column=5, padx=20, pady=(10, 0))

    # Create phone number fill
    Label(demo, text="Phone No.", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=3, column=0, pady=(10, 0))
    phone_no = Entry(demo, width=30)
    phone_no.grid(row=3, column=1, padx=20, pady=(10, 0))

    # Create employment status
    Label(demo, text="Employment Status", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=3, column=2, pady=(10, 0))
    employment_var = StringVar()
    employment_status = ttk.Combobox(demo, width=27, textvariable=employment_var)
    employment_status['values'] = ('Unemployed', 'Self-employed', 'Working Staff')
    employment_status.grid(row=3, column=3, padx=10, pady=(10, 0))
    employment_status.current(0)

    # Create state fill
    Label(demo, text="Religion", fg="white", bg="green", font=("Lucida", 10, "bold")).grid(row=3, column=4, pady=(10, 0))
    religion_var = StringVar()
    religion = ttk.Combobox(demo, width=27, textvariable=religion_var)
    religion['values'] = ('Christian', 'Muslim')
    religion.grid(row=3, column=5, padx=10, pady=(10, 0))
    religion.current(0)
