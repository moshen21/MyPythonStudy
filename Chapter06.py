'''Chapter06'''
'''6-1
if __name__ == '__main__':
    person = {
        'first_name' : 'Mu',
        'last_name' : 'Zhiyu',
        'age' : 19,
        'city' : 'ShangHai'
    }
    print(person)
'''
'''6-4
if __name__ == '__main__':
    person = {
        'first_name': 'Mu',
        'last_name': 'Zhiyu',
        'age': 19,
        'city': 'ShangHai'
    }
    person['girlfriend'] = 'Alice'
    for key in person.keys():
        print(key)
    print('\n')
    for value in person.values():
        print(value)
    for k,v in person.items():
        print(str(k) + ": " + str(v))
'''
'''6-5
if __name__ == '__main__':
    rivers = {
        'nile' : 'egypt',
        'Yellow River' : 'china',
        'Yangtze' : 'china'
    }
    for river, country in rivers.items():
        print("The " + river.title() +
              " runs through " + country.title())
    print('\n')
    for river in set(rivers.keys()):
        print(river.title())
    print('\n')
    for country in set(rivers.values()):
        print(country.title())
'''
'''6-6
if __name__ == '__main__':
    people = ['a','b','c','d','e','f']
    favorite_language = {
        'a' : 'python',
        'b' : 'c',
        'edward' : 'ruby',
        'phil' : 'python'
    }
    for per in people:
        if per in favorite_language.keys():
            print("Hi " + per + ", thank you.")
        else:
            print(per + ", can you take the survey?")
'''
'''6-7
if __name__ == '__main__':
    person1 = {
        'first_name': 'Mu',
        'last_name': 'Zhiyu',
        'age': 19,
        'city': 'Shanghai'
    }
    person2 = {
        'first_name' : 'A',
        'last_name' : 'B',
        'age' : 19,
        'city' : 'Beijing'
    }
    person3 = {
        'first_name' : 'C',
        'last_name' : 'D',
        'age' : 19,
        'city' : 'Xi\'an'
    }
    person = [person1, person2, person3]
    for per in person:
        print(per)
'''
'''6-8
if __name__ == '__main__':
    Andy = {
        'Type' : 'dog',
        'Host' : 'Mac'
    }
    Teddy = {
        'Type' : 'dog',
        'Host' : 'Lily'
    }
    Jones = {
        'Type' : 'cat',
        'Host' : 'Mike'
    }
    pets = [Andy, Teddy, Jones]
    for pet in pets:
        for k, v in pet.items():
            print(str(k) + ": " + str(v))
        print('\n')
'''
'''6-9
if __name__ == '__main__':
    favorite_places = {
        'Mac' : ['Beijing', 'Shanghai', 'Xi\'an'],
        'Lily' : ['Yuan', 'Harbin', 'Shenyang'],
        'Mike' : ['Wuhan', 'Shenzhen', 'Hong Kong']
    }
    for name, place in favorite_places.items():
        print(name)
        print(place)
'''
'''6-11
if __name__ == '__main__':
    Beijing = {
        'country' : 'China',
        'population' : 500000000,
        'fact' : "It is the capital of China"
    }
    Shanghai = {
        'country' : 'China',
        'population' : 500000000,
        'fact' : 'China\'s largest city'
    }
    cities = {
        'Beijing' : Beijing,
        'Shanghai' : Shanghai
    }
    for key,value in cities.items():
        print(str(key))
        for k, v in value.items():
            print(str(k) + ": " + str(v))
        print('\n')
'''