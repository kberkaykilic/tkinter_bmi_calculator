import tkinter as tk
from tkinter import messagebox as msg


def bmi_calculator():
    if entry1.get().isalpha() or entry2.get().isalpha():
        msg.showerror(title="Error", message="Please enter a NUMBER.")
        return
    cm = float(entry1.get())
    kg = float(entry2.get())
    bmi = kg / ((cm/100) ** 2)
    category = ""
    try:
        if bmi < 16:
            category = " Severely Underweight"
        elif (bmi >= 16) and (bmi < 18.5):
            category = "Underweight"
        elif (bmi >= 18.5) and (bmi < 25):
            category = "Healthy"
        elif (bmi >= 25) and (bmi < 30):
            category = "Overweight"
        elif bmi >= 30:
            category = "Severely Overweight"
        msg.showinfo(title="BMI", message=f"Your BMI is: {bmi:.2f} \n You are {category}.")
    except ValueError:
        msg.showerror(title="Error", message="Please enter valid numeric number.")


win = tk.Tk()
win.title("BMI Calculator")
win.iconbitmap("python.ico")  # if the code doesn't run, try your own path.

# setting up the font
bold_font = ("Times new roman", 22, "bold")

label1 = tk.Label(win, text="BMI Calculator", font=bold_font, bg="Black", fg="White")
label1.pack()
label2 = tk.Label(win, text="Enter height (cm):")
label2.pack(padx=5, pady=5)
entry1 = tk.Entry(win)
entry1.pack(padx=5, pady=5)
label3 = tk.Label(win, text="Enter weight (kg):")
label3.pack(padx=5, pady=5)
entry2 = tk.Entry(win)
entry2.pack(padx=5, pady=5)
button1 = tk.Button(win, text="Calculate", command=bmi_calculator)
button1.pack(padx=5, pady=5)

win.mainloop()
