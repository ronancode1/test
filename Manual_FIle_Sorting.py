my_list = ["Banana", "Apple", "Orange1"]
messedupdigits = []

def fix_error(m):
    while True:
        q1 = input(f"Would You Like To Change The Value Of {m} y/n: ").lower()
        if q1 == y:
            q2 = input(f"What Would You Like To Change {m} To: ")
            my_list.remove(m)
            my_list.append(q2)
        elif q1 == n:
            while True:
                q3 = input("Would You Like To Recreate The List y/n: ")
                if q3 == y:
                    createlist()
                    break
                elif q3 == n:
                    break
                else:
                    print("Enter A Valid Answer")
                    continue
        else:
            print("Enter A Valid Answer")
            continue

def sort():
    for i in my_list:
        is_valid = isinstance(i, str) and all(c.isalpha() or c.isspace() for c in i)
        print(f"The Item {i} is {is_valid}")
        fix_error(is_valid)
sort()