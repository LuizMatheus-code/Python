print("this program calculates your Body mass index using centimeters and kilograms")

#collecting the necessary information and converting centimeters to meters
person_height = float(input('type your height in centimeters: '))
person_height = person_height / 100
person_weight = float(input('type your weight in kilograms: '))

#calculatin the bmi based on previous information
bmi = person_weight / person_height**2

#gives the user the final result about their bmi
if bmi < 18.5:
    print("BMI: {:.2f}\nyou're underweight".format(bmi))
elif 18.5 <= bmi <= 24.9:
    print("BMI: {:.2f}\nyour weight is within the normal".format(bmi))
elif 25 <= bmi <= 29.9:
    print("BMI: {:.2f}\nyou're overweight".format(bmi))
else:
    print("BMI: {:.2f}\nyou're obese".format(bmi))
