    a = float(input('Enter weight in kg: '))
    b = float(input('Enter height in cm: '))
    b = b / 100
    c = a / (b * b)
    if c <=18.5:
        print('under weight')
    elif 18.5 <c <= 24.5:
        print('normal weight')
    elif 24.5 < c < =29.5:
        print('over weight')
    else:
        print('obesity')

# or
#BMI in m 
while True:
    height=float(input("enter the height"))
    weight=float(input("enter the weight"))
    bmi=weight/ (height)**2
    print(bmi)
    if bmi<=18.5:
        print("under weight")
    elif bmi>18.5 and bmi<=24.5:
        print("normal weight")
    elif bmi>24.5 and bmi<=29.5:
        print("over weight")
    elif bmi>=30:
        print("obesity")
