def findAge(current_date, current_month, current_year,  
            birth_date, birth_month, birth_year): 
  
    # if birth date is greater then current birth_month 
    # then donot count this month and add 30 to the date so 
    # as to subtract the date and get the remaining days 
      
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if (birth_date > current_date): 
        current_month = current_month - 1
        current_date = current_date + month[birth_month-1] 
          
          
    # if birth month exceeds current month, then 
    # donot count this year and add 12 to the 
    # month so that we can subtract and find out 
    # the difference  
    if (birth_month > current_month):          
        current_year = current_year - 1; 
        current_month = current_month + 12; 
          
    # calculate date, month, year 
    calculated_date = current_date - birth_date; 
    calculated_month = current_month - birth_month; 
    calculated_year = current_year - birth_year; 
      
    # print present age 
    print("\n Your Age in ---> 1/10/ " + str (required_year))
    print("\n Years:", calculated_year , "\n Months:",   
         calculated_month, "\n Days:", calculated_date) 
      


# birth dd//mm//yyyy 
while True:
    print("\n Welcome to RMC Soft for Programming Solutions ! Your Dream became a Code :)" + "\n")
    user_day= int(input(" Please enter your Day of birth : "))
    user_month = int(input("\n Please enter your Month of birth : "))
    user_year = int(input("\n Please enter your Year of birth : "))

    birth_date = user_day
    birth_month = user_month
    birth_year = user_year

    # driver code  

    current_date = 1
    current_month = 10
    required_year = int(input("\n Please Enter required year to calculate age in:  " ))
    current_year = required_year

    Max_compared_day = 20
    Max_compared_month = 11
    Max_compared_year = 5

    Min_compared_day= 1
    Min_compared_month = 9
    Min_Compared_year = 5

    if calculated


    findAge(current_date, current_month, current_year,  
            birth_date, birth_month, birth_year)

    user_decision = input ("\n Would you like to do another operation?  (y/n) ")

    if user_decision == "y":
        continue
    else:
        print("\n It was a pleasure to help you ! , Thanks for your rating :)" + "\n")
        break
    

