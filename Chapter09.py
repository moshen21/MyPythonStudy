'''Chapter09'''
'''9-1
class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    def describe_restaurant(self):
        print("Restaurant name: " + self.restaurant_name.title())
        print("Cuisine type: " + self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is open.")
if __name__ == '__main__':
    restaurant = Restaurant('Good luck','Chinese food')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
'''
'''9-3
class User :
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
    def greet_user(self):
        print("Hi, " + self.last_name + " " + self.first_name)
if __name__ == '__main__':
    user1 = User('Jackson','Michael')
    user1.describe_user()
    user1.greet_user()
'''
'''9-4
class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
    def describe_restaurant(self):
        print("Restaurant name: " + self.restaurant_name.title())
        print("Cuisine type: " + self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is open.")
    def set_number_served(self, num):
        self.number_served = num
    def increment_number_served(self, increment_num):
        self.number_served += increment_num
if __name__ == '__main__':
    restaurant = Restaurant('Good luck','Chinese food')
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    print(str(restaurant.number_served) + " people have eaten at this restaurant.")
    restaurant.set_number_served(100)
    print(str(restaurant.number_served) + " people have eaten at this restaurant.")
    restaurant.increment_number_served(50)
    print(str(restaurant.number_served) + " people have eaten at this restaurant.")
'''
'''9-5
class User :
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0
    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
    def greet_user(self):
        print("Hi, " + self.last_name + " " + self.first_name)
    def increment_login_attempt(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
if __name__ == '__main__':
    user1 = User('Jackson','Michael')
    user1.describe_user()
    user1.greet_user()
    user1.increment_login_attempt()
    user1.increment_login_attempt()
    user1.increment_login_attempt()
    user1.increment_login_attempt()
    print(user1.login_attempts)
    user1.reset_login_attempts()
    print(user1.login_attempts)
'''
'''9-6
class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
    def describe_restaurant(self):
        print("Restaurant name: " + self.restaurant_name.title())
        print("Cuisine type: " + self.cuisine_type.title())
    def open_restaurant(self):
        print("The restaurant is open.")
    def set_number_served(self, num):
        self.number_served = num
    def increment_number_served(self, increment_num):
        self.number_served += increment_num
class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['A', 'B', 'C', 'D']
    def show_icecreamstand(self):
        for flavor in self.flavors:
            print(flavor + " ", end = "")
if __name__ == '__main__':
    ICS = IceCreamStand('Good luck', 'Chinese ice cream')
    ICS.show_icecreamstand()
'''
'''9-7
class User :
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0
    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
    def greet_user(self):
        print("Hi, " + self.last_name + " " + self.first_name)
    def increment_login_attempt(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User) :
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("The privileges of administrator: ", end = "")
        for privilege in self.privileges:
            print(privilege + ', ', end = "")
        print('\n')
if __name__ == '__main__':
    admin1 = Admin('Jackson', 'Michael')
    admin1.show_privileges()
'''
'''9-8
class User :
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0
    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
    def greet_user(self):
        print("Hi, " + self.last_name + " " + self.first_name)
    def increment_login_attempt(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User) :
    def __init__(self, first, last):
        super().__init__(first, last)
        self.privileges = Privileges()
class Privileges() :
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        print("The privileges of administrator: ", end = "")
        for privilege in self.privileges:
            print(privilege + ', ', end = "")
        print('\n')
if __name__ == '__main__':
    admin1 = Admin('Jackson', 'Michael')
    admin1.privileges.show_privileges()
'''
'''9-9
from collections import OrderedDict
if __name__ =='__main__':
    favorite_languages = OrderedDict()
    favorite_languages['jen'] = 'python'
    favorite_languages['sarah'] = 'c++'
    favorite_languages['edward'] = 'ruby'
    favorite_languages['phil'] = 'python'
    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " + language.title() + ".")
'''
'''9-10
from random import randint
class Die :
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))
if __name__ == '__main__':
    die = Die(6)
    for i in range(10):
        die.roll_die()
    print()
    die = Die(10)
    for i in range(10):
        die.roll_die()
    print()
    die = Die(20)
    for i in range(10):
        die.roll_die()
    print()
'''