# higher-lower

from data import data
import random


e = True

while e is True:

    a = data[random.randint(0, len(data))]
    a_name = a['name']
    a_description = a['description']
    a_country = a['country']
    a_follower_count = a['follower_count']

    b = data[random.randint(1, len(data))]
    b_name = b['name']
    b_description = b['description']
    b_country = b['country']
    b_follower_count = b['follower_count']

    print(f"A - {a_name} ({a_description}) from {a_country} ")
    print(f"B - {b_name} ({b_description}) from {b_country} ")

    c = input("\n\n Guess?  -   ").lower()

    d = ""

    if a_follower_count > b_follower_count:
        d = "a"
    elif b_follower_count > a_follower_count:
        d = "b"

    if c == d:
        print('\n\n\n\n')
        e = True
    else:
        print(
            f'Wrong! \n      A has {a_follower_count} \n      B has {b_follower_count} ')
        e = False
