# Name: Donna Ng
# Description: This will delete a song from the music library.


import json
from tkinter import *


def deletePage(index):
    term = Tk()
    term.title("Delete?")
    term.geometry("360x160")

    prompt = Label(term, text="Are you sure you want to delete this?",
                   font=('times new roman', 24), anchor=CENTER)
    prompt.grid(row=0, column=0, columnspan=2, padx=45,
                pady=20)

    yes = Button(term, text="Yes",
                 command=lambda: delete(index),
                 font=('times new roman', 18))
    yes.grid(row=1, column=0, pady=10,
             ipadx=25, ipady=10)

    no = Button(term, text="No",
                command=term.destroy,
                font=('times new roman', 18))
    no.grid(row=1, column=1, pady=10,
            ipadx=25, ipady=10)
    term.mainloop()


def delete(number):
    with open('songs.json', 'r') as infile:
        songs = json.load(infile)

    if number in songs['element']:
        if songs['element'][number]['status'] == 'DELETED':
            message = "\nThis song has already been \ndeleted from the system.\n"
        else:
            songs['element'][number]['status'] = 'DELETED'
            with open('songs.json', 'w') as outfile:
                json.dump(songs, outfile, indent=4)
            message = "\nSong deleted successfully!\nStatus has been updated.\n"
    else:
        message = "\nInvalid!\nThe index number does not exist.\n"

    update = Tk()
    update.title("System Message")
    update.geometry("240x160")

    newMsg = Label(update, text=message, font=('times new roman', 15))
    newMsg.grid(row=0, column=0, padx=20)
    close = Button(update, text="Close Window",
                   command=update.destroy,
                   font=('times new roman', 18))
    close.grid(row=1, column=0, padx=20, pady=10,
               ipadx=25, ipady=10)
    update.mainloop()


def deleteSong():
    root = Tk()
    root.title("Delete A Song")
    root.geometry("480x300")
    prompt = Label(root, text="Enter the song number: ",
                   font=('times new roman', 18), anchor=CENTER)
    prompt.grid(row=0, column=0, padx=40, pady=40)
    number = Entry(root, width=10)
    number.grid(row=0, column=1)

    submit = Button(root, text="Submit",
                    command=lambda: delete(number.get()),
                    font=('times new roman', 18))
    submit.grid(row=1, column=1,
                pady=10, ipadx=20, ipady=10)

    close = Button(root, text="Close Window", command=root.destroy,
                   font=('times new roman', 24))
    close.grid(row=2, column=0, columnspan=2,
               pady=10, ipadx=20, ipady=10)
    root.mainloop()
