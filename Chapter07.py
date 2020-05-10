'''Chapter07'''
'''7-1
if __name__ == '__main__':
    car = input("What kind of car do you want to rent?")
    print("Let me see if I can find you a " + str(car),end = "")
'''
'''7-2
if __name__ == '__main__':
    num = input("Please enter the number of people: ")
    num = int(num)
    if num > 8:
        print("No seat available!",end = "")
'''
'''7-3
if __name__ == '__main__':
    num = input("Please enter a number: ")
    num = int(num)
    if num % 10 == 0:
        print("This number is an integer multiple of 10",end = "")
    else:
        print("This number is't an integer multiple of 10",end = "")
'''
'''7-4
if __name__ == '__main__':
    condiment = input("Please enter the condiment that"
                      " you want add to your pizza: ")
    while(condiment != 'quit'):
        print("We will add " + condiment + " to pizza!")
        condiment = input("Please enter the condiment that"
                          " you want add to your pizza again: ")
'''
'''7-5
if __name__ == '__main__':
    age = input("Please enter your age: (age < 0 to quit)")
    age = int(age)
    while age > 0:
        if age < 3:
            print("FREE")
        elif age >= 3 and age <=12:
            print("Your fare is $10.")
        else:
            print("Your fare is $15.")
        age = input("Please enter your age: (age < 0 to quit)")
        age = int(age)
'''
'''7-6
if __name__ == '__main__':
    age = input("Please enter your age: (age <= 0 to quit)")
    age = int(age)
    active = True
    if age <= 0:
        active = False
    while active:
        if age < 3:
            print("FREE")
        elif age >= 3 and age <= 12:
            print("Your fare is $10.")
        else:
            print("Your fare is $15.")
        age = input("Please enter your age: (age < 0 to quit)")
        age = int(age)
        if age <= 0:
            active = False
'''
