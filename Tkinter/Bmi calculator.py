from tkinter import *
def bmi_calci():
    weight = float(weight_input.get())
    height = float(height_input.get())
    res = round((weight/(height*height))*10000, 2)
    bmi_result_label.config(text=f"{res}")


window = Tk()
window.title("BMI Calculator")
window.minsize(width=150, height=150)
window.config(padx=15, pady=20)

weight = Label(text="Weight is")
weight.grid(column=0, row=0)
height = Label(text="Height is")
height.grid(column=0, row=2)
weight_input = Entry(width=20)
weight_input.grid(column=1, row=0)
height_input = Entry(width=20)
height_input.grid(column=1, row=2)

weight_label = Label(text="KG")
weight_label.grid(column=2, row=0)
height_label = Label(text="CM")
height_label.grid(column=2, row=2)

bmi_label = Label(text="Your BMI is ")
bmi_label.grid(column=0, row=8, padx=15, pady=15)
bmi_result_label = Label(text="0")
bmi_result_label.grid(column=1, row=8)
bmi_unit_label = Label(text="Kg/m^2")
bmi_unit_label.grid(column=2, row=8)

calculate_button = Button(text="Calculate", command = bmi_calci)
calculate_button.grid(column=1, row=5,padx=15, pady=15 )



window.mainloop()