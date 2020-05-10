'''Chapter10'''
'''10-1
if __name__ == '__main__':
    filename = 'learning_python.txt'
    with open(filename) as files_object:
        contents = files_object.read()
        print(contents)
    print()
    with open(filename) as files_object:
        for line in files_object:
            print(line.rstrip())
    with open(filename) as files_object:
        lines = files_object.readlines()
    string = ''
    for line in lines:
        string += line.strip()
    print(string)
'''
'''10-2
if __name__ == '__main__':
    filename = 'learning_python.txt'
    with open(filename) as files_object:
        lines = files_object.readlines()
    string = ''
    for line in lines:
        string += line.strip()
    string.replace('Python', 'C++')
    print(string)
'''
'''10-3
if __name__ == '__main__':
    name = input("Please enter your name: ")
    with open('guest.txt','w') as file_object:
        file_object.write(name)
'''
'''10-4
if __name__ =='__main__':
    while True:
        name = input("Please enter you name: ")
        if name == "":
            break
        else:
            with open('guest_book.txt','a') as file_object:
                file_object.write(name + '\n')
            print('Hello, ' + name + ' Welcome.')
'''
'''10-5 & 10-6
if __name__ == '__main__':
    print("Give me two numbers, and I'll add them.")
    print("Enter 'q' to quit.")
    while True:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        try:
            first_number = int(first_number)
        except ValueError:
            print("Please enter the number!")
        second_number = input("Second number: ")
        if second_number == 'q':
            break
        try:
            second_number = int(second_number)
        except ValueError:
            print("Please enter the number!")
        else:
            print(first_number + second_number,end = "")
'''
'''10-7
if __name__ == '__main__':
    filename1 = 'cats.txt'
    filename2 = 'dogs.txt'
    try:
        with open(filename1) as file_object1:
            lines = file_object1.readlines()
    except FileNotFoundError:
        print("Can't find " + filename1)
    else:
        for line in lines:
            print(line.rstrip() + '  ')
    print()
    try:
        with open(filename2) as file_object2:
            lines = file_object2.readlines()
    except FileNotFoundError:
        print("Can't find " + filename2)
    else:
        for line in lines:
            print(line.rstrip() + ' ')
'''
'''10-8
if __name__ == '__main__':
    filename1 = 'cats.txt'
    filename2 = 'dogs.txt'
    try:
        with open(filename1) as file_object1:
            lines = file_object1.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.rstrip() + '  ')
    print()
    try:
        with open(filename2) as file_object2:
            lines = file_object2.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in lines:
            print(line.rstrip() + ' ')
'''
'''10-9
import json
if __name__ == '__main__':
    num = input("Please enter your favorite number: ")
    filename = 'fav_na.json'
    with open(filename, 'w') as file_object:
        json.dump(num, file_object)
    with open(filename) as file_object:
        numb = json.load(file_object)
    print(numb)
'''



