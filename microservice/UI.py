# File not needed in microservice

import time

if __name__ == '__main__':
    while True:
        # Request user input
        user_input = ''
        # Type 1 to generate new integer or 2 to exit
        while user_input != '1' and user_input != '2':
            user_input = input(
                'Enter 1 to generate a random integer, or 2 to exit: ')
        if user_input != '1' and user_input != 2:
            print('unknown option')
        if user_input == '2':
            print('Exiting, Goodbye')
            exit()
        else:
            # writes the word "run" to UI.txt
            with open('UI.txt', 'w', encoding="utf-8") as txt_file:
                txt_file.write('run')
                txt_file.close()

            # sleep for two seconds
            time.sleep(2)

            # reads UI.txt to get the pseudo-random number
            with open('UI.txt', 'r', encoding="utf-8") as txt_file:
                random_num = txt_file.read()
                print('The random integer is: ', random_num)
                txt_file.close()
