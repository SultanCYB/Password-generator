#!/usr/bin/env python3
'''random password generator'''

from string import punctuation
import random


def pwd_generator(length=0, num=True, symbol=True):
    '''This function has 3 optional parameters :

	- length : length of the password must be at least 8 characters, there is no max range,
	if no length given; the function will choose a random length between 8 and 40

	- num : if False given; it will exclude digits from the password

	- symbol : if False given; it will exclude symbols from the password'''

    letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
    # letters, small and capital

    choices = [letters]

    password = ""

    if num:
        # if you didnt pass a value ( True or False) to num paramter, then it will be used a default
        num = list("0123456789")
        choices.append(num)

    if symbol:
        # if you didnt pass a value ( True or False) to symbol paramter, then it will be used a default
        symbol = list(punctuation)
        choices.append(symbol)

    else:
        # if the user didnt want symbols
        symbol = []  # this was declared to prevent errors

    if not length:
        # if no length given it will give a random length between 8-40


        length = random.choice(range(8,41))

    elif length < 8:
        return "Length must be at least 8"

    while len(password) != length:

        if not password:
            # this will always make the password starts with letters
            password += random.choice(random.choice(letters))

        else:
            check = random.choice(random.choice(choices))

            last_char = password[-1].lower()

            # this will prevent duplicate character
            if check.lower() != last_char:

                # this will prevent two symbols being after each other respectively
                if check not in symbol or last_char not in symbol:

                    password += check

    return password