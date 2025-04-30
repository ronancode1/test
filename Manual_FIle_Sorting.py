my_list = []
messedupdigits = []

def createlist():
    while True:
        q4 = input("What Would You Like To Add To The List Or Enter q To Quit").lower()
        if q4 == "q":
            sort()
            return
        is_valid = isinstance(q4, str) and all(c.isalpha() or c.isspace() for c in q4)
        print(f"The Item {q4} is {is_valid}")
        if is_valid == True:
            my_list.append(q4)
        else:
            fix_error(q4)
        while True:
            q5 = input("Would You Like To Add Another Item. y/n: ").lower()
            if q5 == "y":
                break
            elif q5 == "n":
                sort()
                break
            else:
                continue
        continue


def fix_error(m):
    while True:
        q1 = input(f"Would You Like To Change The Value Of {m} y/n: ").lower()
        if q1 == "y":
            q2 = input(f"What Would You Like To Change {m} To: ")
            my_list.append(q2)
        elif q1 == "n":
            while True:
                q3 = input("Would You Like To Recreate The List y/n: ")
                if q3 == "y":
                    my_list.clear()
                    createlist()
                    break
                elif q3 == "n":
                    break
                else:
                    print("Enter A Valid Answer")
                    continue
        else:
            print("Enter A Valid Answer")
            continue

def sort():
    print("hi")
createlist()