from tkinter import *
from backend import backClick

def onClick():
    text1 = message.get()
    backClick(text1)
    print(text1)
    message_entry.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    root.title("My First App")
    root.geometry("200x100")

    message = StringVar()

    message_entry = Entry(textvariable=message)
    message_entry.place(relx=.5, rely=.1, anchor="c")

    message_button = Button(text="Отправить", command=onClick)
    message_button.place(relx=.5, rely=.5, anchor="c")

    root.mainloop()
