from tkinter import *
from datetime import  date


window = Tk()
window.title("Age Calculator")
window.geometry("500x330")
window.resizable(width=False, height=False)
window.config(bg="light grey")
window.config(padx=15, pady=20)

def age_cal():
    today = date.today()
    birthdate = date(int(year_input.get()), int(month_input.get()), int(month_input.get()))
    age = today.year - birthdate.year - ((today.month, today.day) <
                                         (birthdate.month, birthdate.day))
    try:
        int(day_entry.get())
        # int(month_entry.get())
        # int(year_entry.get())
        ans = Label(text=f"hi {name_entry.get()}! Your Age is {age}", font=("Arial", 15, "bold"),
                    background="light grey")
        ans.grid(column=1, row=9, pady=10)
    except ValueError:
        ans = Label(text=f"It is not validate", font=("Arial", 15, "bold"),
                    background="light grey")


name_person = Label(text="Name", background="light grey", font=("Arial", 12, "bold"),)
name_person.grid(column=0, row=4, pady=10,padx=100 )
day = Label(text="Day", background="light grey", font=("Arial", 12, "bold"), )
day.grid(column=0, row=5, pady=10,padx=100)
month = Label(text="Month", background="light grey", font=("Arial", 12, "bold"), )
month.grid(column=0, row=6, pady=10,padx=100)
year = Label(text="Year", background="light grey", font=("Arial", 12, "bold"), )
year.grid(column=0, row=7, pady=10,padx=100)

name_input= StringVar()
day_input = StringVar()
month_input= StringVar()
year_input = StringVar()

name_entry = Entry(window, textvariable=name_input, font=("Arial", 10),)
name_entry.grid(column=1, row=4, pady=10)
day_entry = Entry(window, textvariable=day_input, font=("Arial", 10),)
day_entry.grid(column=1, row=5, pady=10)
month_entry = Entry(window, textvariable=month_input, font=("Arial", 10),)
month_entry.grid(column=1, row=6, pady=10)
year_entry = Entry(window, textvariable=year_input, font=("Arial", 10),)
year_entry.grid(column=1, row=7, pady=10)

calculate_buttton = Button(text = "Calculate", command=age_cal, font=("arial", 15, "bold"),
                           fg="white", bg="black")
calculate_buttton.grid(column=1, row=8)
window.mainloop()
