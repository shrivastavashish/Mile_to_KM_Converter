from tkinter import *

#Author: @Ashish Shrivastav

# Create a formula
def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = round(miles * 1.609)
        kilo_result_label.config(text=f"{km}")
    except ValueError:
        kilo_result_label.config(text="Invalid Input")

# Create a window
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=100)
window.config(padx=50, pady=50)
window.config(bg="light blue")


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.config(bg="black", fg="white")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.config(bg="black", fg="white")
is_equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.config(bg="black", fg="white")
kilo_result_label.grid(column=1, row=1)

kilo_output = Label(text="Km")
kilo_output.config(bg="black", fg="white")
kilo_output.grid(column=2, row=1)

calc_button = Button(text="Calculate", bg="red", command=miles_to_km)
calc_button.config(bg="red")
calc_button.grid(column=1, row=2)