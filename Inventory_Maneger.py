
inventory = {"example": "Hello"}
all_items = {"example": "Hello"}

categorys = ["food", "cleaning", "decor", "fidget"]

for i in categorys:
    inventory[i] = {}
    all_items[i] = []

def add():

    q1 = input("What Do You Want To Add To The Inventory: ").lower()
    while True:
        q2 = input(f"What Is The Category Of The Product/Item, The Categorys Are {categorys}: ").lower()
        if q2 in categorys:
            break
        else:
            print("Invalid Category. Please Choose From The Available Categories Or Add A New One.")
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
        q4 = input("How Many Products/Items Do You Have In Stock 'Whole Number': ")
        if q4.isdigit:
            break
        else:
            print("Is Not A Whole Number")
            continue
    
    while True:
        print(f"Confirm Your Deposit Of The Product/Item {q1} That Will Be Put In The Category {q2} With The Price Of {q3} And The Stock Is {q4}")
        q5 = input("Would You Like To Confirm Your Deposit Enter 'y' To Confirm And Enter 'n' To Re-Enter The Deposit Enter 'q' To Quit: ").lower()
        if q5 == "y":
            print("Deposit Confirmed")
            inventory[q2][q1] = {"price": q3, "stock": q4}
            all_items[q2].append(q1)
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
    while True:
        q1 = input(f"What Category Is The Item You Want To Remove The Categorys Are {categorys}: ").lower()
        if q1 in categorys:
            break
        else:
            print("Invalid Category. Please Choose From The Available Categories Or Add A New One.")
            continue
    while True : 
        q2 = input(f"What Item In The Category {q1} Do You Want To Add The Items Are {all_items}: ").lower()
        if q2 in all_items[q1]:
            continue
        else:
            print(f"Invalid Category. Please Choose From The Availible Items In The Category {q1}")




add()
