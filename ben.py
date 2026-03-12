
#write a function add_two_numbers that takes two numbers as parameters and returns their sum.
def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(3, 5))  # Example usage, should print 8
print(add_two_numbers(10, 20))  # Example usage, should print 30
#write a function greet that takes one parameter,a person's name, and prints a greeting message like "Hello, [name]!"
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # Example usage, should print "Hello, Alice!"
greet("Bob")  # Example usage, should print "Hello, Bob!"

#write  a function check_even that takes one  number, and prints"even" if the number is even and  "odd" if the number is odd.
def check_even(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
check_even(4)  # Example usage, should print "even"
check_even(7)  # Example usage, should print "odd"

#write a function sum_list that takes a list of numbers as a parameter and returns the sum of all the numbers in the list.
def sum_list(numbers):
    return sum(numbers)
print(sum_list([1, 2, 3, 4, ]))  # output 10
print(sum_list([5, 5, 5]))  # output 15

#write a function print_days that prints the days of the week(sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday) using a loop.
def print_days():
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days_of_week:
        print(day)      
print_days()  # Example usage, should print the days of the week

#write a function check_sighn that takes a number and prints whether the number is positive, negative, or zero.
def check_sign(number):
    if number > 0:
        print("positive")
    elif number < 0:
        print("negative")
    else:
        print("zero")
check_sign(10)  # Example usage, should print "positive"
check_sign(-5)  # Example usage, should print "negative"
check_sign(0)  # Example usage, should print "zero"

#write a function repeat_word that takes a word and a number as parameters and prints the word that many times.
def repeat_word(word, number):
    for _ in range(number):
        print(word)
repeat_word("Hello", 3)  # Example usage, should print "Hello" three times
repeat_word("goodbye", 2)  # Example usage, should print "goodbye" two times

