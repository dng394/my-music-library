# Name: Donna Ng
# Description: Use to display song information on GUI.


import json
import time
from tkinter import *


def randomNum(song):
    with open('../microservice/UI.txt', 'w') as f:
        f.write(f"run\n{song}")
    time.sleep(1)
    with open('../microservice/UI.txt', 'r') as f:
        read_data = f.readline()
        if read_data == 'random_num\n':
            index = f.readline()
        else:
            index = '-1'
    return index


def randomSong():
    with open('songs.json', 'r') as infile:
        songs = json.load(infile)
    recommendation = songs['number']
    index = randomNum(recommendation)

    RS = Tk()
    RS.title("Recommendation")
    RS.geometry("845x620")

    welcome = Label(RS, text="My Music Library",
                    font=('times new roman', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45,
                 pady=20)

    if index == '-1':
        errorLabel = Label(RS, text='Error! Microservice Not Running!',
                           font=('times new roman', 48), anchor=CENTER)
        errorLabel.grid(row=1, column=0, columnspan=2, padx=45,
                        pady=20)
    else:
        title = songs['element'][index]['title']
        artist = songs['element'][index]['artist']
        genre = songs['element'][index]['genre']
        status = songs['element'][index]['status']
        dataLabel = Label(RS, text=f'Song number:\n'
                                   f'Song title:\n'
                                   f'Song artist:\n'
                                   f'Song genre:\n'
                                   f'Song status:',
                          font=('times new roman', 24), anchor='w',
                          justify=LEFT)
        dataLabel.grid(row=2, column=0, pady=10, ipadx=25, ipady=20)
        contentLabel = Label(RS, text=f'{index}\n'
                                      f'{title}\n'
                                      f'{artist}\n'
                                      f'{genre}\n'
                                      f'{status}',
                             font=('times new roman', 24), anchor='w',
                             justify=LEFT)
        contentLabel.grid(row=2, column=1, pady=10, ipadx=25, ipady=20)

    terminate = Button(RS, text="Close Window", command=RS.destroy,
                       font=('times new roman', 36))
    terminate.grid(row=5, column=0, columnspan=2,
                   pady=10, ipadx=90, ipady=20)
    RS.mainloop()
