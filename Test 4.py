Products = []

print("Welcome to the Product Management System")
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Products")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_product(Products)
        elif choice == '2':
            remove_product(Products)
        elif choice == '3':
            view_products(Products)
        elif choice == '4':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please try again.")

def add_product(products):
    product = input("Enter the product name: ")
    while True:
        while True:
            min_price = input("Enter the min product price: ")
            if min_price.isdigit():
                min_price = int(min_price)
                if min_price == 1:
                    print("Max price Must Be a Higher Number.")
                    continue
                else:
                    break
            else:
                print("Please Enter a Valid Number.")
                continue
        
        while True:
            max_price = input("Enter the max product price: ")
            if max_price.isdigit():
                max_price = int(max_price)
                if max_price == 0:
                    print("Max price Must Be a Higher Number.")
                    continue
                else:
                    break
            else:
                print("Please Enter a Valid Number.")
                continue
        
        if min_price > max_price:
                    print("Min Price Must Be Lower Then Max Price.")
                    continue
        else:
            break

    

    products.append({"Product": product, "Min_Prince": min_price, "Max_Price": max_price,})
    print(f"Product {product} added successfully!")
    main_menu()


def remove_product(products):
    product = input("Enter the product name to remove: ")
    for i in products:
         if i["Product"] == product:
            products.remove(i)
            print(f"Product {product} removed successfully!")
            main_menu()
    print(f"Product {product} not found.")

def view_products(products):
    if not products:
        print("No products available.")
    else:
        print("\nProducts:")
        for i in products:
            print(f"Product: {i['Product']}, Min Price: {i['Min_Prince']}, Max Price: {i['Max_Price']}")

main_menu()
