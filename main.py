from tkinter import *
window = Tk()
window.title("Welcome to Asa's App")
window.geometry('550x400')
x = False
lbl = Label(window, text=":)")
lbl.grid(column=1, row=1)
lbl = Label(window, text="Hello",font = ("Arial Bold", 50))
lbl.grid(column=0, row=0)
text = StringVar()
entry = Entry(textvariable=text)
entry.grid(column=2, row=1)
def clicked():
    global x
    global text
    print(text.get())
    text.set("")
    if x == False:
        lbl.configure(text="olleH")
        x = True
    elif x == True:
        lbl.configure(text="Hello")
        x = False
    print("Button was clicked")
btn = Button(window, text = "Click Me", command = clicked)
btn.grid(column=1, row=0)
#Read the webpage and continue with project



window.mainloop()