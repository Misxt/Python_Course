from tkinter import *
window = Tk()
window.title("Asa's Caculator")
window.geometry('550x400')
#Title
xspace = 3
yspace = 3
lbl = Label(window, text="Answer:")
lbl.grid(column=0, row=0, padx=xspace, pady=yspace)
lbl = Label(window, text="First Number: ")
lbl.grid(column=0, row=1, padx=xspace, pady=yspace)
ResultLbl = Label(window, text="")
ResultLbl.grid(column=1, row=0, padx=xspace, pady=yspace)
#Number Inputs
FirstNumber = StringVar()
entry = Entry(textvariable=FirstNumber)
entry.grid(column=1, row=1, padx=xspace, pady=yspace)
lbl = Label(window, text="Second Number: ")
lbl.grid(column=0, row=2, padx=xspace, pady=yspace)
SecondNumber = StringVar()
entry = Entry(textvariable=SecondNumber)
entry.grid(column=1, row=2, padx=xspace, pady=yspace)
#Operation Inputs
def labelchange(x):
    x = str(x)
    ResultLbl.config(text=x)
def addition():
    global FirstNumber
    global SecondNumber
    x = int(FirstNumber.get())
    y = int(SecondNumber.get())
    answer = x+y
    labelchange(answer)
def subtraction():
    global FirstNumber
    global SecondNumber
    x = int(FirstNumber.get())
    y = int(SecondNumber.get())
    answer = x-y
    labelchange(answer)
def multiplication():
    global FirstNumber
    global SecondNumber
    x = int(FirstNumber.get())
    y = int(SecondNumber.get())
    answer = x*y
    labelchange(answer)
def division():
    global FirstNumber
    global SecondNumber
    x = int(FirstNumber.get())
    y = int(SecondNumber.get())
    answer = x/y
    labelchange(answer)
btn = Button(window, text = "Addition", command = addition)
btn.grid(column=0, row=3, padx=xspace, pady=yspace)
btn = Button(window, text = "Subtraction", command = subtraction)
btn.grid(column=1, row=3, padx=xspace, pady=yspace)
btn = Button(window, text = "Multiplication", command = multiplication)
btn.grid(column=0, row=4, padx=xspace, pady=yspace)
btn = Button(window, text = "Division", command = division)
btn.grid(column=1, row=4, padx=xspace, pady=yspace)
#Display the result into a label instead of a terminal
#Make everything prettier
#"Modify label when button is pressed tkinter"

#Test
window.mainloop()