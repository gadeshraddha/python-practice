weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height **2)

print(f"Your BMI is: {BMI:.2f}")
 
if BMI < 18.5:
    print("Category: Underweight")
elif BMI < 25:
    print("Category: Normal weight")
elif BMI < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
 