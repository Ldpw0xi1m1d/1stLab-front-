from tkinter import *
from backend import backClick
from backend import backGetData

def onClick():
    text1 = message.get()
    backClick(text1)
    print(text1)
    message_entry.delete(0, END)

def onClickGet():
    textFromFile = backGetData()
    lbl.config(text=textFromFile)


if __name__ == '__main__':
    root = Tk()
    root.title("My First App")
    root.geometry("300x150")

    message = StringVar()

    message_entry = Entry(textvariable=message)
    message_entry.place(relx=.5, rely=.1, anchor="c")

    message_button = Button(text="Отправить", command=onClick)
    message_button.place(relx=.5, rely=.5, anchor="c")

    data_button = Button(text="Получить", command=onClickGet)
    data_button.place(relx=.5, rely=.3, anchor="c")

    lbl = Label(root, text="Привет")
    lbl.place(relx=.13, rely=.13, anchor="c")

    root.mainloop()
