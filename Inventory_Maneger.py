inventory = {
    "food": {},
    "cleaning": {},
    "decor": {}
}
categorys = ["food", "cleaning", "decor", "fidget"]

def add():

    q1 = input("What Do You Want To Add To The Inventory: ")
    while True:
        q2 = input(f"What Is The Category Of The Item, The Categorys Are {categorys} ")
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
        q4 = input("How Many Products Do You Have In Stock 'Whole Number'")
        if q4.isdigit:
            
        
add()
