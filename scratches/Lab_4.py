### Problem 1
import re

def main1():
    print("problem 1")


    converter_setting = input("Please type 'miles' if you would like to convert from Kilometers to Miles. "
                              "Type 'kilometer' if you would like to convert from Miles to Kilometers ")
    # casts string to lowercase for assurance that user entered data is in a usable format.
    converter_setting.lower()

    # So this is a regular expression or regex for short. It allows you to search for matches in strings in efficent/ easier ways
    # So the '\s' is for whitespaces. the '*' causes the result to match 0 or more repititon of the preceding characters.
    # ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
    # Also match returns type None when no match is found. So that is how i'm able to create settings

    if  re.match(r'\s*m\s*i\s*l\s*e\s*',converter_setting) != None:
        kilometers = float(input("Please enter how many kilometers you will be converting "))
        print(f"{kilometers * .6214}")

    elif re.match(r'\s*k\s*i\s*l\s*o\s*m\s*e\s*t\s*e\s*r*',converter_setting) != None:
        miles = float(input("Please enter how many miles you will be converting "))
        print (f"{miles/.6214}")

main1()

def main2():
    print("problem 2")
    # a seperate function for every operation for a clear concise main function
    value = acquire_purchase_value()
    sales_tax = calculate_sales_tax(value)
    county_tax = calculate_county_tax(value)
    display_total(value,sales_tax,county_tax)


def acquire_purchase_value():
    # self explanatory
    value = int(input("Please enter the purchase amount"))
    return value

def calculate_sales_tax(value):
    # self explanatory. Value is being passed in as a parameter from the main function. and it returns sales_tax to be used
    # as a variable. without a return statement sales_tax in main would be equal to type none.
    sales_tax = value * .05
    return sales_tax

def calculate_county_tax(value):
    # self explanatory. Value is being passed in as a parameter from the main function. and it returns county_tax to be used
    # as a variable. without a return statement county_tax in main would be equal to type none.
    county_tax = value * .025
    return county_tax

def display_total(value,sales_tax,county_tax):
    total_tax = sales_tax + county_tax
    total_sale = total_tax + value

    print(f" You wanted to purchase something for ${value}, sales tax was ${sales_tax}, county tax was ${county_tax}, "
          f"for a total of ${total_tax} tax paid. You spent ${total_sale} in total ")

main2()

def main3():
    # most of this is self_explanatory
    print("problem 3")
    replacement_cost = int(input("Please enter the replacement cost for your property"))

    insurance_calc(replacement_cost)

def insurance_calc(x):
    print(f"You will need a minimum of ${x *.80} of coverage for this property")

main3()


def main4():
    # self explanatory
    print("Problem 4")

    monthly_insurance = int(input("Please enter your monthly payment towards insurance"))
    monthly_loan = int(input("Please enter your monthly payments towards your loan"))
    monthly_gas = int(input("Enter an average amount you spend per month on gas"))
    monthly_tires = int(input("Please enter the average amount you spend on tires"))
    monthly_maintainence = int(input("Please enter the average amount you spend on maintainence"))

    expense_calc(monthly_insurance,monthly_loan, monthly_gas, monthly_tires, monthly_maintainence)


def expense_calc(insurance,loan,gas, tires, maintainence):

    monthly_total =  insurance + loan + gas + tires + maintainence
    annual_total = monthly_total *12

    print(f" You spend ${monthly_total} per month on car related expenses and ${annual_total} per annum on car related expenses")

main4()

def main5():
    print("problem 5")
    actual_value = int(input("Enter the actual value of your property"))
    calculate_property_tax(actual_value)

def calculate_property_tax(x):
    # we're told the assesment value is 60% of the actual value, in this case our x. We are then told for every 100 dollars, 72%
    # of it is taxed. That is how we get our formula. thats an effective tax rate of .0072 of the assessment value.
    assessment_value = x *.60
    tax = (assessment_value/100) *.72

    print(f"Your assesment value is ${assessment_value}, and your property tax has been evaluted to be ${tax}")

main5()