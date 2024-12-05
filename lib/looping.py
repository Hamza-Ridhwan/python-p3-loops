#!/usr/bin/env python3

def happy_new_year():
    year = 10
    while year > 0:
        print(year)
        year+= -1
    print('Happy New Year!') 

def square_integers(int_list):
    return [i**2 for i in int_list]

def fizzbuzz():
    for numbers in range(100):
        new_num = numbers + 1
        if new_num % 3 == 0 and new_num % 5 == 0:
            print('FizzBuzz')
        elif new_num % 3 == 0:
            print('Fizz')
        elif new_num % 5 == 0:
            print ('Buzz')
        else:
            print(new_num)


fizzbuzz()