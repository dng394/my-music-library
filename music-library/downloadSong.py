# Name: Donna Ng
# Description: This will download a song to the music library.


import json
from tkinter import *


def download(number):
    with open('songs.json', 'r') as infile:
        songs = json.load(infile)

    if number in songs['element']:
        if songs['element'][number]['status'] == 'DELETED':
            message = "\nThis song is no longer available.\n"
        else:
            songs['element'][number]['status'] = 'Song Downloaded'
            with open('songs.json', 'w') as outfile:
                json.dump(songs, outfile, indent=4)
            message = "\nSong downloaded successfully!\nStatus has been updated.\n"
    else:
        message = "\nInvalid!\nThis song number does not exist.\n"

    update = Tk()
    update.title("System Message")
    update.geometry("240x160")

    mess = Label(update, text=message, font=('times new roman', 15))
    mess.grid(row=0, column=0, padx=20)
    close = Button(update, text="Close this window",
                   command=update.destroy,
                   font=('times new roman', 18))
    close.grid(row=1, column=0, padx=20, pady=10,
               ipadx=25, ipady=10)
    update.mainloop()


def downloadSong():
    root = Tk()
    root.title("Download A Song")
    root.geometry("480x300")
    prompt = Label(root, text="Enter the song number: ",
                   font=('times new roman', 18), anchor=CENTER)
    prompt.grid(row=0, column=0, padx=40, pady=40)
    index = Entry(root, width=10)
    index.grid(row=0, column=1)

    submitB = Button(root, text="SUBMIT",
                     command=lambda: download(index.get()),
                     font=('times new roman', 18))
    submitB.grid(row=1, column=1,
                 pady=10, ipadx=20, ipady=10)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('times new roman', 24))
    terminate.grid(row=2, column=0, columnspan=2,
                   pady=10, ipadx=20, ipady=10)
    root.mainloop()
