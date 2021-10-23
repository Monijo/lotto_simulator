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

