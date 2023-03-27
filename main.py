from tkinter import *
# import the Pillow package to your IDE
from PIL import Image, ImageTk
from demographics import demo_graph
from database_window import database_win

root = Tk()
root.resizable(False, False)
root.minsize(500, 500)
root.config(padx=15, pady=15, bg="green")
root.iconimage = PhotoImage(file="images/icon_img.png")
root.iconphoto(False, root.iconimage)
root.title("Sculpture Survey")


canvas = Canvas(root, width=282, height=185, cursor="circle", bg="black", highlightthickness=0)
filename = ImageTk.PhotoImage(Image.open("images/sculpture_img.jpg"))
canvas.create_image(148, 95, image=filename)
canvas.pack()

Label(root, text="WELCOME TO UKULELE SCULPTURE", relief=RIDGE, font=("Calibri", "15", "bold")).pack()
Label(root, text="\nWe are glad you are here!", bg="green", fg="white", font=("Times", "12", "bold")).pack()
Label(root, text="Will you like to share your experience?\n", bg="green", fg="white", font=("Times", "12", "bold")).pack()
Label(root, text="Take the 60 seconds survey by clicking the button below", bg="green", fg="white", font=("Times", "13", "bold")).pack()

survey_btn = Button(root, text="TAKE SURVEY", bd=5, fg="white", bg="red", relief=GROOVE, font="Times", command=demo_graph)
survey_btn.pack()

labelframe = LabelFrame(root, text="Are you an admin? If yes, click the login button below:", bg="black", fg="white", labelanchor=N)
labelframe.pack(expand=True)

Label(labelframe, text="Password:", font=("Calibri", "12", "bold"), bg="black", fg="white").pack(side=LEFT)
password = Entry(labelframe, width=30, justify=CENTER)
password.pack(side=LEFT, expand=True)
Label(labelframe, text=" ", bg="black").pack(side=LEFT)
admin_btn = Button(labelframe, text="ADMIN LOGIN", bd=5, fg="white", bg="black", command=database_win)
admin_btn.pack(side=BOTTOM)


root.mainloop()
