# Microservice to generate random songs

import time
import random

if __name__ == '__main__':

    while True:
        # sleep one second
        time.sleep(1)
        # open file and keep file open for reading
        with open('UI.txt', 'r', encoding="utf-8") as txt_file:
            # read file content
            file_content = txt_file.readline()
            songs = int(txt_file.readline())

        if file_content == 'run\n':
            random_num = random.randint(1, songs)
            with open('UI.txt', 'w', encoding="utf-8") as txt_file:
                txt_file.write(f'random_num\n{random_num}')
            print(
                f"Generated! Here is the number of the song recommendation: {random_num}\n")
