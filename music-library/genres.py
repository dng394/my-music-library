# Name: Donna Ng
# Description: This displays the music genres on a page.

import json
from tkinter import *


def display(songGenre):
    result = "The " + songGenre + " genre has the following songs:\n"
    with open('songs.json', 'r') as infile:
        songs = json.load(infile)
    for song in songs['element']:
        if songs['element'][song]['genre'] == songGenre:
            result += ('\t' + song + '. ' + songs['element'][song]['title'] + " " + "by" + " " + songs['element'][song]['artist'] +
                       '\n\t****' + songs['element'][song]['status'] + '\n')
    root = Tk()
    root.title(songGenre)
    root.geometry("980x1200")
    message = Label(root, text="My Music Library",
                    font=('times new roman', 70), anchor=CENTER)
    message.grid(row=0, column=0, columnspan=2,
                 padx=45, pady=20)
    data = Label(root, text=result, font=(
        'times new roman', 20), anchor='w', justify=LEFT)
    data.grid(row=1, column=0, columnspan=2, pady=10, ipadx=25, ipady=20)
    close = Button(root, text="Close Window",
                   command=root.destroy, font=('times new roman', 24))
    close.grid(row=4, column=0, columnspan=2,
               pady=10, ipadx=90, ipady=10)
    root.mainloop()


def listGenre():
    root = Tk()
    root.title("Music Genres")
    root.geometry("980x650")
    message = Label(root, text="My Music Library",
                    font=('times new roman', 80), anchor=CENTER)
    message.grid(row=0, column=0, columnspan=2, padx=45, pady=20)

    pop = Button(root, text="Pop", command=lambda: display(
        "Pop"), font=('times new roman', 36))
    pop.grid(row=1, column=0, pady=10, ipadx=80, ipady=20)

    rock = Button(root, text="Rock", command=lambda: display(
        "Rock"), font=('times new roman', 36))
    rock.grid(row=1, column=1, pady=10, ipadx=80, ipady=20)

    rnb = Button(root, text="RnB", command=lambda: display(
        "RnB"), font=('times new roman', 36))
    rnb.grid(row=1, column=2, pady=10, ipadx=80, ipady=20)

    edm = Button(root, text="EDM", command=lambda: display(
        "EDM"), font=('times new roman', 36))
    edm.grid(row=2, column=0, pady=10, ipadx=68, ipady=20)

    ambient = Button(root, text="Ambient", command=lambda: display(
        "Ambient"), font=('times new roman', 36))
    ambient.grid(row=2, column=1, pady=10, ipadx=55, ipady=20)

    hip_hop = Button(root, text="Hip Hop", command=lambda: display(
        "Hip Hop"), font=('times new roman', 36))
    hip_hop.grid(row=2, column=2, pady=10, ipadx=52, ipady=20)

    trance = Button(root, text="Trance", command=lambda: display(
        "Trance"), font=('times new roman', 36))
    trance.grid(row=3, column=0, pady=10, ipadx=58, ipady=20)

    new_age = Button(root, text="New Age", command=lambda: display(
        "New Age"), font=('times new roman', 36))
    new_age.grid(row=3, column=1, pady=10, ipadx=50, ipady=20)

    country = Button(root, text="Country", command=lambda: display(
        "Country"), font=('times new roman', 36))
    country.grid(row=3, column=2, pady=10, ipadx=55, ipady=20)

    close = Button(root, text="Close Window",
                   command=root.destroy, font=('times new roman', 35))
    close.grid(row=4, column=1, columnspan=1, pady=10, ipadx=60, ipady=20)
    root.mainloop()
