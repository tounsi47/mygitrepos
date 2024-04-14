print('Count my life version 1.0 (non_gui)')
print('by fury project 2024')
print("let's start !!")
while True:
    age = input('Enter your age : ')
    try:
        age = int(age)
        print(f"So your age is {age} years old")
        break
    except:
        print('error, you may type an integer')

print('select the conversion mode')
print('1 - seconds')
print('2 - minutes')
print('3 - hours')
print('4 - days')
print('5 - weeks')
print('6 - months')
while True:
    choice = input('>> ')
    if choice == '1':
        age_in_second = age * 31536000
        print(f"Your age in second is {age_in_second} seconds")
        stop = input('do you want to end the program (y / n)')
        if stop.lower() == 'y':
            break
        else:
            print('restarting')
            
    elif choice == '2':
        age_in_minute = age * 525600
        print(f"your age in minutes is {age_in_minute} minutes")
    elif choice == '3':
        age_in_hours = age * 8760
        print(f"Your age in hours is {age_in_hours} hours")
    elif choice == '4':
        age_in_day = age * 365
        print(f"Your age in days in {age_in_day} days")
    elif choice == '5':
        age_in_weeks = age * 52
        print(f"Your age in weeks is {age_in_weeks} weeks")
    elif choice == '6':
        age_in_months = age * 12
        print(f"Your age in months is {age_in_months} months")
    stop = input('do you want to stop??? (y/n)')
    stop = stop.lower()
    if stop == 'y':
        break
