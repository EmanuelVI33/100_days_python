height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if (bmi < 18.5):
    print(f"Under {bmi} they are underweight")
elif(bmi < 25):
    print(f"Over {bmi} but below 25 they have a normal weight")
elif(bmi < 30):
    print(f"Over {bmi} but below 30 they are overweight")
elif(bmi < 35):
    print(f"Over {bmi} but below 35 they are obese")
else:
    print(f"Above {bmi} they are clinically obese")