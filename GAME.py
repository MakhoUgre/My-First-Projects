
# GAME

from random import randrange
import math

def main():
    game_mode = int(input('choose game mode \n user to guess the number, press 1:\n computerto guess the number, press 2:\n'))

    lower_bound = int(input("please enter lower bound: "))
    upper_bound = int(input("please enter upper bound: ")) 
    if game_mode == 1 :
       random_number_user(lower_bound , upper_bound)
    elif game_mode == 2 :
        guess_the_number_computer(lower_bound , upper_bound)
    

#  ფუნქცია
def random_number_user(lower_bound , upper_bound) :
    number_to_guess = randrange(lower_bound,upper_bound) 
    user_guess = math.inf # ინიციალიზაცია ? თუ user_guess = რაღაც რიცხვს ალბათობა იმისა რომ ეს რაღაც რიცხვი შეარჩიოს კომპმა, ამიტომ ვწერთ math.inf თუმცა შესაძლოა აგრეთვე დაგვეწერა 99999999999999 რაღაც დიდი რიცხვი.
    guess_counter = 0

    while    number_to_guess !=user_guess: # მანამ სანამ გამოსაცნობი რიცხვი არ უდრის იუზერის მიერ გამოცნობილი რიცხვი (ამიტომ არის inf ინფინიტი)
        guess_counter = guess_counter + 1   # იგივეა  guess_counter += 1
        user_guess = int(input(f"Gusse the number between {lower_bound} and {upper_bound}:\n")) # f ფორმატირება
        if user_guess < number_to_guess: 
            print("Too smalle, try again: ")
        elif user_guess > number_to_guess: 
            print("Too big, try egean: ")

    print(f"congratulations! You guessed the number {number_to_guess} in {guess_counter} tries") 

    game_over = input ('to return to main menue press (m) button, To quit the game press ENTER\n')
    if game_over == 'm':
        print(':-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: \n')
        main()
    return 0 

def guess_the_number_computer(lower_bound , upper_bound):
    feedback = ''
    computer_guess = math.inf
    guess_counter = 0
    while feedback != 'c':
        guess_counter += 1
        computer_guess = randrange(lower_bound,upper_bound)
        feedback = input(f'is {computer_guess} correct (c),too low (l) or to high (h): ')
        if feedback == 'l':
            lower_bound = computer_guess + 1
        elif feedback == 'h':
            upper_bound = computer_guess - 1 
        if lower_bound == upper_bound :
            guess_counter += 1
            print(f'number left is {lower_bound}')
            break

    print(f'computer guessed the number {computer_guess} in {guess_counter} ')

    game_over = input ('to return to main menue press (m) button, To quit the game press ENTER \n')
    if game_over == 'm':
        print(':-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: \n')
        main()

    return 0

main()