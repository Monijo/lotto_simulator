import random

def get_number():
    '''Get number from user.
    Try until user gives 6 proper numbers
    between 1 and 49
    :return: list of chosen numbers
    '''
    index = 0
    chosen_numbers = []
    while index < 6:
        try:
            number = int(input("Give me number: "))
            if number >= 1 and number <= 49:
                if number not in chosen_numbers:
                    chosen_numbers.append(number)
                    index += 1
                else:
                    print("This number is already chosen!")
            else:
                print("Chose the number from the range 1-49!")
        except ValueError:
            print("Enter a number!")
    return chosen_numbers

def sort_number():
    '''Returns given numbers with ascending order '''
    chosen_numbers = get_number()
    chosen_numbers.sort()
    return chosen_numbers

def draw():
    '''Computer draws 6 different numbers
    :return: list with 6 random numbers
    '''
    drawn_number_list = []
    while len(drawn_number_list) <6:
        drawn_number = random.randint(1,49)
        if drawn_number not in drawn_number_list:
            drawn_number_list.append(drawn_number)
    return drawn_number_list

def lotto():
    '''Main function with our program.'''
    chosen_numbers_list = sort_number()
    print(f"Chosen numbers: {chosen_numbers_list}")
    drawn_numbers_list = draw()
    print(f"Drawn numbers: {drawn_numbers_list}")
    counter = 0
    for number in chosen_numbers_list:
        if number in drawn_numbers_list:
            counter += 1
    if counter >= 3:
        print(f"Congratulations! You guessed {counter} numbers!")
    else:
        print(f"Sorry.. You lost..You guessed {counter} {'number' if counter == 1 else 'numbers'}")

if __name__ == "__main__":
    lotto()
