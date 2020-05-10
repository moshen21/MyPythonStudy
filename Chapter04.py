'''Chapter04'''
'''4-3
if __name__ == '__main__':
    for value in range(1,21):
        print(value)
'''
'''4-4
if __name__ == '__main__':
    values = [value for value in range(1,1000001)]
    for i in range(0,100000):
        print(values[i])
'''
'''4-5
if __name__ == '__main__':
    values = [value for value in range(1,1000001)]
    print(min(values))
    print(max(values))
    print(sum(values))
'''
'''4-6
if __name__ == '__main__':
    values = [value for value in range(1,21,2)]
    for value in values:
        print(value)
'''
'''4-7
if __name__ == '__main__':
    values = [value for value in range(3,31,3)]
    for value in values:
        print(value)
'''
'''4-8
if __name__ == '__main__':
    values = [value ** 3 for value in range(1,11)]
    for value in values:
        print(value)
'''
'''4-9
if __name__ =='__main__':
    values = [value ** 3 for value in range(1,11)]
    print(values)
'''
'''4-10
if __name__ == '__main__':
    my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
    print("The first three items in the list are: ")
    print(my_foods[0:3])
    print("Three items from the middle of the list are: ")
    print(my_foods[1:4])
    print("The last three items in the list are: ")
    print(my_foods[-3:])
'''
'''4-11
if __name__ == '__main__':
    my_pizzas = ['pizza', 'falafel', 'carrot cake']
    friend_pizzas = my_pizzas[:]
    my_pizzas.append('cannoli')
    friend_pizzas.append('ice cream')
    print("My favorite pizzas are: ")
    for i in range(0,4):
        print(my_pizzas[i].title())
    print("My friend favorite pizzas are: ")
    for i in range(0,4):
        print(friend_pizzas[i].title())
'''
'''4-13
if __name__ == '__main__':
    foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')
    for food in foods:
        print(food.title())
    foods = ('A','B','C','D','E')
    for food in foods:
        print(food.lower())
'''
