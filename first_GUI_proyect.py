from tkinter import *

def do_math():
    miles = float(input.get())
    km = round(miles * 1.609)
    km_value.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
# Entry
input = Entry(width=7)
input.grid(column=1, row=0)

# Label
label = Label(text="Miles")
label.grid(column=2, row=0)

label1 = Label(text="is equal to:")
label1.grid(column=0, row=1)

km_value = Label(text="0")
km_value.grid(column=1, row=1)

km_result = Label(text="Km")
km_result.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=do_math)
calculate_button.grid(column=1, row=2)


window.mainloop()