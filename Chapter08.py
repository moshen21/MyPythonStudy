'''Chapter08'''
'''8-6
def city_country(city, country):
    citycountry = city + ', ' + country
    return citycountry
if __name__ == '__main__':
    CC = city_country('Beijing', 'China')
    print(CC)
'''
'''8-7
def make_album(name, albumname, num = 1):
    album = {
        'name' : name,
        'albumname' : albumname,
        'number' : num
    }
    return album
if __name__ == '__main__':
    album1 = make_album('Jack', 'ABCD')
    print(album1)
    album2 = make_album('Mac', 'EFGH',2)
    print(album2)
'''
'''8-8
def make_album(name, albumname, num = 1):
    album = {
        'name' : name,
        'albumname' : albumname,
        'number' : num
    }
    return album
if __name__ == '__main__':
    while True:
        name = input("Please enter your name: ")
        albumname = input("Please enter your album's name: ")
        album = make_album(name, albumname)
        if name == "" or albumname == "":
            break
        else:
            print(album)
'''
'''8-9
def show_magicians(magicians):
    for magician in magicians:
        print(magician + '  ',end = "")
if __name__ == '__main__':
    magicians = ['Max', 'Lily', 'Mod']
    show_magicians(magicians[:])
'''
'''8-10
def show_magicians(magicians):
    for magician in magicians:
        print(magician + '  ',end = "")
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]
if __name__ == '__main__':
    magicians = ['Max', 'Lily', 'Mod']
    show_magicians(magicians[:])
    print('\n')
    make_great(magicians)
    show_magicians(magicians)
'''
'''8-11
def show_magicians(magicians):
    for magician in magicians:
        print(magician + '  ',end = "")
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]
    return magicians
if __name__ == '__main__':
    magicians = ['Max', 'Lily', 'Mod']
    show_magicians(magicians[:])
    print('\n')
    magicians2 = make_great(magicians[:])
    show_magicians(magicians)
    print('\n')
    show_magicians(magicians2[:])
'''
'''8-12
def sandwich(*Ingredients):
    print("The ingredients of the sandwich: ", end = "")
    for ingredient in Ingredients:
        print(ingredient + ', ', end = "")
if __name__ == '__main__':
    sandwich('A','B','C','D')
'''
'''8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
if __name__ == '__main__':
    user_profile = build_profile('Tom', 'And Jerry',
                                 location = 'princeton',
                                 field = 'physics',
                                 country = 'America')
    for k, v in user_profile.items():
        print(k + ": " + v)
'''
'''8-14
def cars(manufacturer, model, **car_):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for k, v in car_.items():
        car[k] = v
    return car
if __name__ == '__main__':
    manufacturer = 'subaru'
    model = 'outback'
    car_total = cars(manufacturer, model, color='blue', tow_package=True)
    print(car_total)
'''