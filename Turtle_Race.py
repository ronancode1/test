import turtle

WIDTH, HEIGHT = 500, 800

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("TURTLE RACING!")


def get_number_of_turtles():
    turtles = 0
    while True:
        turtles = input("Enter The Number of Turtles (2-10): ")
        if turtles.isdigit():
            turtles = int(turtles)
            if 2 <= turtles <= 10:
                break
            else:
                print("Please Enter a Number Between 2 and 10.")
                continue
        else:
            print("Invalid Input. Please Enter a Number.")
            continue
    return turtles

turtles = get_number_of_turtles()
print(f"You Have Chosen {turtles} Turtles.")

