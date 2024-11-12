#Exercise 5-Days of the Month

days_in_month = {
    1: 31,   
    2: 28,   
    3: 31,   
    4: 30,   
    5: 31,   
    6: 30,   
    7: 31,   
    8: 31,   
    9: 30,   
    10: 31,  
    11: 30,  
    12: 31   
}

Month = int(input("Enter the Month number (1-12): "))

# Check if the input is valid
if 1 <= Month <= 12:
    # Check for February and ask if it's a leap year
    if Month == 2:
        Leap_Year = input("Is it a Leap Year? (yes/no): ").strip().lower()
        if Leap_Year == "Yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days in a non-leap year.")
    else:
        print(f"The month has {days_in_month[Month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")