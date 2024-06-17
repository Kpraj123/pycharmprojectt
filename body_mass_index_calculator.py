# 1st input: enter height in meters e.g: 1.65
height = input("what is your height")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("what is your weight")
# 🚨 Don't change the code above 👆

# Write your code below this line 
weight_kg = int(weight)
height_mt = float(height)

Bmi = int(weight_kg/(height_mt * height_mt))

print(Bmi)