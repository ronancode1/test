inventory = {
    "food": {"item": "hi"},
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
            
        q3 = input(f"What Is The Price Of This Product/Item  'With Decimal Points': ")
        q3 = "$" + q3
        
add()
