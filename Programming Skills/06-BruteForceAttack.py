#Exercise 6-Brute Force Attack

Correct_Password = "12345"

Max_Attempts = 5

Attempts = 0

while Attempts < Max_Attempts:
  
    user_input = input("Please Enter the Password: ")
    
    if user_input == Correct_Password:
        print("Access Granted.")
        break  
    else:
        
        Attempts += 1
        remaining_attempts = Max_Attempts - Attempts
        
        if remaining_attempts > 0:
            print(f"The Password is incorrect, you have {remaining_attempts} attempts remaining.")
        else:
           
            print("The Password is incorrect, maximum attempts reached. Authorities have been alerted.")
