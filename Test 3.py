print("Welcome To The Blot Joint")
enter_age = (16)
print("Enter Age Is", enter_age)


 
 
def age_check(age_enter):
    # checks age
    age = int(input("Enter Your Age "))
    
    # checks if age is greater than or equal to 18
    if age >= enter_age:
        print("You Are a Adult")
    elif age <= enter_age:
        print("You Are a Minor")
    else:
        print("You Need to Enter a Valid Age")

# Starts The Function
age_check(enter_age)
    
    