## Problem 1


def main1():
    print("Running first problem")
    number = ask_for_number()
    week = {1:"Monday", 2: "Tuesday", 3:"Wedensday", 4:"Thursday", 5 : "Friday", 6: "Saturday", 7 : "Sunday"}
    print(week.get(number))


def ask_for_number():
    user_number  = int(input("Enter a number from 1 through 7 "))
    ### A while loop to catch an user error. Assert isn't used to ensure the program continues running.
    while user_number not in [1,2,3,4,5,6,7]:
        user_number = int(input("Please enter a number from 1 through 7 !!! "))
    return user_number

main1()


### Problem 2

def main2():
    print("Running second problem")
    lenrec1 = int(input("Enter the length of the first rectangle"))
    widthrec1 = int(input("Enter the width of the first rectangle"))
    lenrec2 = int(input("Enter the length of the second rectangle"))
    widthrec2 = int(input("Enter the width of the second rectangle"))

    ### Determines if a rectangle is bigger than the other or is equal
    ### Takes the user entered numbers as parameters with length followed by width for each rectangle.
    ## like this, length 1, width 1, length 2, width 2
    rectangle_area_determinator(lenrec1,widthrec1,lenrec2,widthrec2)



def rectangle_area_determinator(len1, width1, len2, width2):
    rec1_area = len1 * width1
    rec2_area = len2 * width2


    if rec1_area == rec2_area:
        print("the two areas are the same ")

    elif rec1_area > rec2_area:
        print(" The first rectangle is bigger than the second rectangle")

    else:
        print(' The second rectangle is bigger than the first rectangle')


main2()

### Code for problem 3

def main3():
    age = int(input("Please enter an age and I will determine your human status. "
                    "If you're under the age of one please input 0, months will not be accepted and will return an error"))
    assert type(age) == int, "Incorrect input. Run the code again and only enter numbers as advised"

    human_determinism(age)



def human_determinism(age):
    if age < 0:
        print("Your human status is infant")

    elif age >= 1 and age < 13:
        print("Your human status is a puny child")

    elif age >= 13 and age < 20:
        print (" Sorry! Your human status is a teenager")

    else:
        print (" CONGRATS! You have beat the game of survival. Your human status is Adult")


main3()

### problem 4

def main4():
    user_number = int(input("Enter a number, 1-10, that you would like to be converted to Roman Numerals"))
    assert user_number in [1,2,3,4,5,6,7,8,9,10], "Enter a number 1-10 fam!"
    converter(user_number)

def converter(number):
    roman_dictionary = {1 : "I", 2: "II", 3: "III", 4: 'IV', 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9:"IX", 10: "X"}
    print(roman_dictionary.get(number))

main4()


def main5():
    mass = int(input("Please enter a mass"))
    weight = mass *9.8
    if  weight > 500:
        print(f" Your object weighed {weight}N, it is too heavy")
    elif weight < 100:
        print(f" Your object weighed {weight}, it is too light")
    else:
        print(" We call this a golidlocks because it's just right")

main5()