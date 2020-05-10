'''Chapter05'''
'''5-3
if __name__ == '__main__':
    alien_color = 'red'
    if alien_color == 'green':
        print("You get five points")
'''
'''5-4
if __name__ == '__main__':
    alien_color = 'green'
    if alien_color == 'green':
        print("You get five points.")
    else:
        print("You get ten points.")
'''
'''5-5
if __name__ == '__main__':
    alien_color = 'red'
    if alien_color == 'green':
        print("You get five points.")
    elif alien_color == 'yellow':
        print("You get ten points.")
    else:
        print("You get fifteen points.")
'''
'''5-6
if __name__ == '__main__':
    age = 19
    if age < 2:
        print("He is a baby.")
    elif age >= 2 and age < 4:
        print("He is toddler.")
    elif age >= 4 and age < 13:
        print("He is a child.")
    elif age >= 13 and age < 20:
        print("He is a teenager.")
    elif age >= 20 and age < 65:
        print("He is an adult.")
    elif age >= 65:
        print("He is an old man.")
    else:
        print("ERROR.")
'''
'''5-7
if __name__ == '__main__':
    favorite_fruits = ['A','B','C','D','E']
    if 'A' in favorite_fruits:
        print("You really like " + 'A')
    if 'B' in favorite_fruits:
        print("You really like " + 'B')
    if 'C' in favorite_fruits:
        print("You really like " + 'C')
    if 'D' in favorite_fruits:
        print("You really like " + 'D')
    if 'E' in favorite_fruits:
        print("You really like " + 'E')
    if 'F' not in favorite_fruits:
        print("You don't like " + 'F')
'''
'''5-8
if __name__ == '__main__':
    usernames = ['admin', 'A', 'B', 'C', 'D']
    for username in usernames:
        if username == 'admim':
            print("Hello " + username + ", would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again")
'''
'''5-9
if __name__ == '__main__':
    usernames = ['admin', 'A', 'B', 'C', 'D']
    del usernames[0:5]
    if usernames:
        for username in usernames:
            if username == 'admim':
                print("Hello " + username + ", would you like to see a status report?")
            else:
                print("Hello " + username + ", thank you for logging in again")
    else:
        print("We need to find some users!")
'''
'''5-10
if __name__ == '__main__':
    current_users = ['A', 'B', 'C', 'D','E']
    new_users = ['a', 'c', 'D', 'F', 'f']
    for  new_user in new_users:
        if new_user in current_users \
                or new_user.upper() in current_users \
                or new_user.lower() in current_users:
            print(new_user + " already used, please change your username.")
        else:
            print(new_user + " is not used.")
            current_users.append(new_user)
'''
'''5-11
if __name__ == '__main__':
    numbers = [number for number in range(1,10)]
    for number in numbers:
        if number == 1:
            print("1st")
        elif number == 2:
            print("2nd")
        elif number == 3:
            print("3rd")
        else:
            print(str(number) + "th")
'''
