## Code for problem number 1.

print("Problem 1")

name = input("Enter your Full Name")
address = input("Enter your Address")
number = input("Enter your Phone Number")
major = input("Enter your Major")

print(f"Your Name: {name} \n Address: {address} \n Phone Number: {number} \n Major: {major} \n" )

## Code for problem number 2.
print("Problem 2 " )

total = int(input("Please enter the projected amount of total sales"))
print(total)

print(f"Your projected annual profit is {total * 0.23} \n")


## Code for problem number 3
print("Problem 3 " )

inches = int(input("Please enter the total square feet"))
print(f"{inches} is {inches/43560} acres\n")


## Code for problem number 4
print("Problem 4" )
item1 = int(input("Please enter the price for item1"))
item2 = int(input("Please enter the price for item2"))
item3 = int(input("Please enter the price for item3"))
item4 = int(input("Please enter the price for item4"))
item5 = int(input("Please enter the price for item5"))
subtotal = item1 + item2+ item3+ item4 + item5

print(f"Subtotal:{subtotal}  \n"
      f"Sales tax:{subtotal *.07} \n"
      f"Total: {subtotal + (subtotal *.07)} \n")


### code for problem number 5
print("\n Problem 5")
print("The car traveled %d in %d hours"%(70*6,6))
print("The car traveled %d in %d hours"%(70*10,10))
print("The car traveled %d in %d hours"%(70*15,15))



