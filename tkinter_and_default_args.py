from tkinter import *

def button_clicked():
    my_label["text"] = "I got clicked!"
    my_text = input.get()
    my_label.config(text=my_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial", 10, "bold"))
my_label["text"] = "New text"
my_label.config(text="New text")
my_label.config(text="Click the button!")
# my_label.pack() #side=left, botton, right, top #expand=True
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Click Me! 2", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=20)
# input.pack()
input.grid(column=3, row=2)




# import turtle
#
# tim = turtle.Turtle()
# tim.write("Some text", font=("Times New Roman", 80, "bold"), align="center")




window.mainloop()