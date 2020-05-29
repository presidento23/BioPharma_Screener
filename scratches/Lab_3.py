### LAB 3

# Code for problem 1.

def main1():
    print("problem 1")
    total = 0
    week = {1: "Monday", 2: "Tuesday", 3: "Wedensday", 4: "Thursday", 5: "Friday"}
    for i in range(1,5):

        holder = int(input(f"How many bugs did you catch {week.get(i)}"))
        print(f"You caught {holder} bug(s) on {week.get(i)}")
        total += holder

    print(f"You caught {total} bugs during this work week. Congrats!!!")

main1()

## Code for problem 2

def main2():
    print("problem 2")
    burn_rate = 4.2

    time = int(input("What is your total time in minutes"))

    print(f"You've burned {burn_rate * time} calories in {time} minutes ")

main2()


## PRoblem 3

def main3():
    print("problem 3")
    expense_book =  {}
    budget = int(input("Please enter your budget for the month"))
    assert type(budget) == int, "Enter only numbers, no signs"
    still_going = True

    ### got fancy just for ya mr.elebuke

    while still_going:
        expense = int(input("Enter the price of your expense"))
        expense_name = input("Enter a name for your expense")
        expense_book[expense_name] = expense
        budget -= expense

        more = input("Do you want to enter more? Type 'Y' for 'Yes' and 'N' for 'No'")

        if more.lower() == "y":
            continue
        if more.lower() == "n":
            break

    print(f"Your budget is {budget}")

main3()


### Problem 4

def main4():
    print("problem 5")
    speed = int(input("Please enter your speed"))
    time = int(input("Please enter your total time spent traveling"))

    distance_traveled_by_hour(speed,time)

def distance_traveled_by_hour(speed,time):

    for i in range(1,time +1):
        print(f"You traveled {speed * i} miles at hour {i}, while going {speed} mph")



main4()


# Problem 5

def main5():
    print("Problem 5")
    calculate_rainfall()


def calculate_rainfall():
    years = int(input("Enter how many years you have data for"))
    total = 0
    for b in range(1,years +1):
        for i in range(1,13):
            monthly_rainfall =  int(input(f"Enter the rainfall for month {i} of year {b}"))
            total += monthly_rainfall
    total_months = years * 12
    print(f" It rained a total of {total} inches in {total_months} months for an average of {total / total_months}")


main5()