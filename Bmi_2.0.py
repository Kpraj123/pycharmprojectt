height = float(input("Enter Your Height"))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter Your Weight"))
#enter your height in metres.

bmi = weight / (height * height)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif  bmi <30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print( f"Your BMI is {bmi}, you are clinically obese.")
  
