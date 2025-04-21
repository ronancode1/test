# Slot Machine Game
card_balence = 100
def confirm_deposit(a):
    print(f"Your Deposit Amount Is: ${a} \n Please Confirm")
    while True:
        confirmation = input("Press 'y' to confirm or 'n' to cancel: ").lower()
        if confirmation == "y":
            print(f"Your Deposit Amount Of ${a} Has Been Confirmed")
            break
        elif confirmation == "n":
            print("Deposit Cancelled")
            reenter = input("Would You Like To Re-Enter The Amount? (y/n): ").lower()
            if reenter == "y":
                deposit()
                break
            elif reenter == "n":
                print("Thank You For Playing!")
                exit()
        else:
            print("Invalid Input. Please Press 'y' to confirm or 'n' to cancel.")
            continue
def deposit():
    while True:
        amount = input("What Would You Like To Deposit? Press 'q' to Quit: $")
        if amount.isdigit():
            amount = int(amount)
            
            if amount > 0:
                confirm_deposit(amount)
                return amount
            elif amount > card_balence:
                print("You Dont Have Enough Money Please Enter Another Amount")
                continue
        elif amount.lower() == "q":
            exit()
        else:
            print("Please Enter A Number")
            continue

balence = deposit()  
         
  