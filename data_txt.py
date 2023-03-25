from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox


def save():
    get_firstname = first_name.get()
    get_lastname = last_name.get()
    get_middle_name = middle_name.get()
    get_home_address = home_address.get()
    get_city = city.get()
    get_state = state.get()
    get_phone_no = phone_no.get()

    if len(get_firstname) == 0 or len(get_lastname) == 0 or len(get_middle_name) == 0 or len(
            get_home_address) == 0 or len(get_city) == 0 or len(get_state) == 0 or len(get_phone_no) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askquestion(title="Confirmation", message="Is it okay to save?")
        if is_ok:
            messagebox.showinfo(title="SUCCESS", message="Saved Successfully!\n\nThanks for your time.")
            with open("data.txt", "a") as data_file:
                data_file.write(
                    f"First Name: {get_firstname} | Last Name: {get_lastname} | Middle Name: {get_middle_name} | Home Address: {get_home_address} | City: {get_city} | State: {get_state} | Phone Number: {get_phone_no}\n")


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


