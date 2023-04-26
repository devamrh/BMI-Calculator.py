promptQuestion01 = int(input('Do you want to measure your BMI (press 1 to measure)?'))

if promptQuestion01 == 1:
    promptQuestion02 = int(input('Do you want to measure it in Pounds[1] or in KGs[2] :'))

    if promptQuestion02 == 1:
        weight = float(input('Please give your weight(lbs) :'))
        height = float(input('Please give your height(in) :'))
        formula = ((weight/height**2) *703)
        result = print('Your BMI Is : %.2f' % formula)

    elif promptQuestion02 == 2:
        weight = float(input('Please give your weight(kg) :'))
        height = float(input('Please give your height(meter) :'))
        formula = (weight)/(height**2)
        result = print('Your BMI Is : %.2f' % formula)

    else:
        print('Invalid Input. Please Re-Run The Program')

else:
    print('Invalid Input. Please Re-Run The Program')
