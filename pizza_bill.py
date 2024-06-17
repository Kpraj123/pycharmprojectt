print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N") 
extra_cheese = input("Do you want extra cheese? Y or N")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
   print("You will have to pay $5")
   bill += 15
elif size == "M":
    print("You will have to pay $20")
    bill += 20
else:
    print("You will have to pay $25")
    bill += 25


if add_pepperoni == "Y":
  if size == "S":
    bill += 2
    print("$2 for pepperoni is added to you bill")
  else:
    bill += 3
    print("$3 for pepperoni is added to your bill")

if extra_cheese == "Y":
  bill += 1
  print("$1 for cheese is added to your bill")

print(f"Your final bill is: ${bill}.")