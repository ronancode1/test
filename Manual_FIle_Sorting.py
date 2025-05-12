my_list = []
messedupdigits = []

def createlist():
    while True:
        q4 = input("What Would You Like To Add To The List Or Enter q To Start Sorting").lower()
        if q4 == "q":
            sort_list()
            return
        is_valid = isinstance(q4, str) and all(c.isalpha() or c.isspace() for c in q4)
        if is_valid == True:
            print(f"Sucessfuly Added {q4} To List")
            my_list.append(q4)
        else:
            print("Input Is Invalid")
            fix_error(q4)
        while True:
            q5 = input("Would You Like To Add Another Item. y/n: ").lower()
            if q5 == "y":
                break
            elif q5 == "n":
                sort_list(my_list)
                break
            else:
                continue
        continue


def fix_error(m):
    while True:
        q1 = input(f"Would You Like To Change The Value Of {m} y/n: ").lower()
        if q1 == "y":
            q2 = input(f"What Would You Like To Change {m} To: ")
            is_valid = isinstance(q2, str) and all(c.isalpha() or c.isspace() for c in q2)
            print(f"The Item {q2} is {is_valid}")
            if is_valid == True:
                my_list.append(q2)
            else:
                fix_error(q2)   
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

def sort_list(ml):
    finnished_list = []
    sorted_caractors = []
    alphabet_order = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 
    "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    if len(my_list) >= 2:
        for i in alphabet_order:
            def sort_letter(n):
                while True:
                    for item1 in my_list:
                        if item1[0] == alphabet_order[n]:
                            sorted_caractors.insert(1, item1)
                    if len(sorted_caractors) == 1:
                        continue
                    elif len(sorted_caractors) == 0:
                        print(f"Nothing Starts With {alphabet_order[i + 1]} In This List")
                    else:
                        for l in alphabet_order:
                            stuffforsorting == []
                            if  == l:

                        

createlist()