import sqlite3
from demographics import *

dg_import = demo_graph()

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
                         "first_name": dg_import.first_name.get(),
                         "last_name": dg_import.last_name.get(),
                         "middle_name": dg_import.middle_name.get(),
                         "home_address": dg_import.home_address.get(),
                         "date_of_birth": dg_import.date_of_birth.get(),
                         "gender_option": dg_import.gender_option.get(),
                         "marital_status": dg_import.marital_status.get(),
                         "city": dg_import.city.get(),
                         "state": dg_import.state.get(),
                         "phone_no": dg_import.phone_no.get(),
                         "employment_status": dg_import.employment_status.get(),
                         "religion": dg_import.religion.get(),
                         "scale_1": dg_import.scale_1.get(),
                         "scale_2": dg_import.scale_2.get(),
                         "scale_3": dg_import.scale_3.get()
                     })
    # commit changes
    submit_conn.commit()
    # close connection
    submit_conn.close()
    # clear the textboxes
    dg_import.first_name.delete(0, END)
    dg_import.last_name.delete(0, END)
    dg_import.middle_name.delete(0, END)
    dg_import.home_address.delete(0, END)
    dg_import.city.delete(0, END)
    dg_import.state.delete(0, END)
    dg_import.phone_no.delete(0, END)


def connect_database():
    database = Tk()
    database.resizable(0, 0)
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
