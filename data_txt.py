from demographics import demo_graph
from tkinter import messagebox


dg_import = demo_graph()

def save():
    get_firstname = dg_import.first_name.get()
    get_lastname = dg_import.last_name.get()
    get_middle_name = dg_import.middle_name.get()
    get_home_address = dg_import.home_address.get()
    get_city = dg_import.city.get()
    get_state = dg_import.state.get()
    get_phone_no = dg_import.phone_no.get()

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

                '''
                This below has already been sorted out in the database.py file
                
                first_name.delete(0, END)
                last_name.delete(0, END)
                middle_name.delete(0, END)
                home_address.delete(0, END)
                city.delete(0, END)
                state.delete(0, END)
                phone_no.delete(0, END)
                '''
