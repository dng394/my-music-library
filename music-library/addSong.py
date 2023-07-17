# Name: Donna Ng
# Description: This will add a song to the music library.

import json
from tkinter import *


def submitBtn(title, artist, genre, availability):
    with open('songs.json', 'r') as infile:
        songs = json.load(infile)
    status = availability
    songs['number'] += 1
    index = songs['number']
    songs['element'][index] = {'title': title,
                               'artist': artist,
                               'genre': genre,
                               'status': status
                               }
    with open('songs.json', 'w') as outfile:
        json.dump(songs, outfile, indent=4)

    message = Tk()
    message.title("New System Message")
    message.geometry("300x250")

    update = "\nMusic library successfully updated!\nSong: " + \
        title + "\nby: " + artist + "\nwith No. " + \
        str(index) + " has been been added.\n"
    newMsg = Label(message, text=update, font=('times new roman', 16))
    newMsg.grid(row=0, column=0, padx=20)
    close = Button(message, text="Close Window",
                   command=message.destroy, font=('times new roman', 18))
    close.grid(row=1, column=0, padx=20, pady=10,)
    message.mainloop()


def addSong():
    root = Tk()
    root.title("Add A Song")
    root.geometry("800x650")
    genre = ["Pop", "Rock", "RnB", "EDM",
             "Ambient", "Trance", "New Age", "Country"]
    music_genre = StringVar(root)
    music_genre.set("Select one from the following")

    title = Label(root, text="My Music Library", font=(
        'times new roman', 80), anchor=CENTER)
    title.grid(row=0, column=0, columnspan=2, padx=45, pady=20)

    title_field = Label(root, text="Enter a song title: ",
                        font=('times new roman', 18))
    title_field.grid(row=1, column=0, pady=20)

    artist_field = Label(root, text="Enter the artist name: ",
                         font=('times new roman', 18))
    artist_field.grid(row=2, column=0, pady=20)

    genre_field = Label(root, text="Select the music genre: ",
                        font=('times new roman', 18))
    genre_field.grid(row=3, column=0, pady=20)

    status_field = Label(root, text="Enter the status:",
                         font=('times new roman', 18))
    status_field.grid(row=4, column=0, pady=20)

    title = Entry(root, width=40)
    title.grid(row=1, column=1)

    artist = Entry(root, width=40)
    artist.grid(row=2, column=1)

    genre_list = OptionMenu(root, music_genre, *genre)
    genre_list.grid(row=3, column=1)

    status = Entry(root, width=40)
    status.grid(row=4, column=1)

    submit = Button(root, text="Submit", command=lambda: submitBtn(
        title.get(), artist.get(), music_genre.get(), status.get()), font=('times new roman', 20))

    submit.grid(row=5, column=0, columnspan=2, pady=10, ipadx=80, ipady=20)

    close = Button(root, text="Close Window",
                   command=root.destroy, font=('times new roman', 20))

    close.grid(row=6, column=0, columnspan=2, pady=10, ipadx=70, ipady=20)

    root.mainloop()
