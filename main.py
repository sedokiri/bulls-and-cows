"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Kirill Sedov
email: Kirillsedov71@gmail.com
discord: Kirill S.
"""
import random
import time

print("Hi there")
print("_"*50)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print("_"*50)

numbers = random.sample("1234567890", 4)
number = int("".join(numbers))
if number < 1000:
    number = number*10
attempts = 0
start_time = time.time()
while True:
    digits = input("Enter a number: ")
    print("_" * 50)
    if digits.isdigit() and len(digits) == 4 and len(set(digits)) == 4 and digits[0] != '0':
        cows = 0
        bulls = 0
        for x in range(4):
            if digits[x] == str(number)[x]:
                bulls += 1
            elif digits[x] in str(number):
                cows +=1
        attempts +=1
        if bulls == 4:
            end_time = time.time()
            all_time = end_time - start_time
            minutes = int(all_time//60)
            seconds = all_time % 60
            print(f"""Correct, you've guessed the right number in {attempts} guesses!.
                  \nExecution time: {minutes:.0f} minutes and {seconds:.0f} seconds""")
            break
        else:
            print(f"Cows: {cows}, Bulls: {bulls} ")
    else:
        print("""Invalid input. Please make sure the number is four digits long, 
              has no duplicates, contains only digits, and does not start with zero.""")







