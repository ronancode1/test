inventory = {
    "food": {},
    "cleaning": {},
    "decor": {}
}
categorys = ["food", "cleaning", "decor", "fidget"]

def add():

    q1 = input("What Do You Want To Add To The Inventory: ")
    while True:
        q2 = input(f"What Is The Category Of The Item, The Categorys Are {categorys}: ")
        if q2 in categorys:
            break
        else:
            print("Invalid category. Please choose from the available categories.")
            continue

    while True:
        q3 = input(f"What Is The Price Of This Product/Item  'With Decimal Points': ")
        if q3.isdigit:
            print("There Is No Decimal Point Re-Enter The Price")
            continue
        else:
            q3 = "$" + q3
            break
    while True:
        q4 = input("How Many Products Do You Have In Stock 'Whole Number': ")
        if q4.isdigit:
            break
        else:
            print("Is Not A Whole Number")
            continue
    
    while True:
        print(f"Confirm Your Deposit Of The Product{q1} That Will Be Put In The Category {q2} With The Price Of {q3} And The Stock Is {q4}")
        q5 = input("Would You Like To Confirm Your Deposit Enter 'y' To Confirm And Enter 'n' To Re-Enter The Deposit Enter 'q' To Quit").lower()
        if q5 == "y":
            print("Deposit Confirmed")
            inventory[q2][q1] = {"price": q3, "stock": q4}
            break
        elif q5 == "n":
            print("Re-Enter The Deposit")
            add()
            break
        elif q5 == "q":
            Main_Menu()
            break
        else:
            print("Confirm Your Order Again Invalid Awncer")
            continue

def remove():
    q1 = input(f"What Category Is The Product You Want To Remove In ")


add()
