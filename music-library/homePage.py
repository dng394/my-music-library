# Name: Donna Ng
# Description: This is the home page of the music library.

from tkinter import *
from genres import listGenre
from addSong import addSong
from downloadSong import downloadSong
from deleteSong import deleteSong
from randomSongGen import randomSong


def exitPage():
    root = Tk()
    root.title("Exit")
    root.geometry("400x280")

    prompt = Label(root, text="Do you wish to exit this page?",
                   font=('times new roman', 24), anchor=CENTER)
    prompt.grid(row=0, column=0, columnspan=2, padx=45, pady=20)

    yes = Button(root, text="Yes", command=exit, font=('times new roman', 18))
    yes.grid(row=1, column=0, pady=10, ipadx=25, ipady=10)

    no = Button(root, text="No", command=root.destroy,
                font=('times new roman', 18))
    no.grid(row=1, column=1, pady=10, ipadx=25, ipady=10)

    root.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title("My Music Library")
    root.geometry("960x700")

    message = Label(root, text="My Music Library",
                    font=('times new roman', 70), anchor=CENTER)
    message.grid(row=0, column=0, columnspan=2, padx=45, pady=20)

    display = Button(root, text="Music Genres", command=listGenre,
                     font=('times new roman', 30))
    display.grid(row=1, column=0, columnspan=2,
                 padx=300, pady=10, ipadx=65, ipady=20)

    add = Button(root, text="Add Song", command=addSong,
                 font=('times new roman', 30))
    add.grid(row=2, column=0, pady=10,
             ipadx=130, ipady=20)

    delete = Button(root, text="Delete Song", command=deleteSong,
                    font=('times new roman', 30))
    delete.grid(row=2, column=1, pady=10,
                ipadx=126, ipady=20)

    download = Button(root, text="Download Song", command=downloadSong,
                      font=('times new roman', 30))
    download.grid(row=3, column=0, pady=10,
                  ipadx=93, ipady=20)

    random = Button(root, text="Recommend Song", command=randomSong,
                    font=('times new roman', 30))
    random.grid(row=3, column=1, pady=10,
                ipadx=90, ipady=20)

    close = Button(root, text="Exit", command=exitPage,
                   font=('times new roman', 30))
    close.grid(row=4, column=0, columnspan=2, padx=300,
               pady=50, ipadx=120, ipady=20)

    root.mainloop()
