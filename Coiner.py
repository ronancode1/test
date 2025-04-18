coin = 0
print("You Have 0 Coins")
print("To Get Coins You Have To Answer Questions About Python")

def Coin_Gain(C):
    coin = C + 1
    print(coin)

def Coin_Loss(C):
    coin = C - 1
    print(coin)

def Question_1(C):
    answer = input(
        "What best describes a Python list? A, B, C, or D\n"
        "A. An immutable sequence of items\n"
        "B. A hash table implementation\n"
        "C. A mutable ordered collection of heterogeneous elements\n"
        "D. A type of numeric iterable used in loops\n"
    )
    if answer.upper() == "C":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – A list is mutable, ordered, and can store different data types.")
        C = Coin_Loss(C)
    return C
      
def Question_2(C):
    answer = input(
        "What is a variable in Python? A, B, C, or D\n"
        "A. A reserved keyword that defines a data type\n"
        "B. A named location used to store data in memory\n"
        "C. A constant reference to an object\n"
        "D. A method used to access object attributes\n"
    )
    if answer.upper() == "B":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – A variable is a named reference to a value stored in memory.")
        C = Coin_Loss(C)
    return C

def Question_3(C):
    answer = input(
        "Which option best defines a Python function? A, B, C, or D\n"
        "A. A block of code that executes automatically when defined\n"
        "B. A reusable block of code that runs when called and can return a value\n"
        "C. A list of statements inside a loop\n"
        "D. A Python object that holds only strings\n"
    )
    if answer.upper() == "B":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – Functions must be called and can return results.")
        C = Coin_Loss(C)
    return C
        
def Question_4(C):
    answer = input(
        "Which best describes a Python string (`str`)? A, B, C, or D\n"
        "A. An immutable sequence of Unicode characters\n"
        "B. A mutable sequence of bytes\n"
        "C. A numeric object that stores integers as text\n"
        "D. A list of ASCII values\n"
    )
    if answer.upper() == "A":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – Strings are immutable and made of Unicode characters.")
        C = Coin_Loss(C)
    return C
        
def Question_5(C):
    answer = input(
        "What defines a Python integer (`int`)? A, B, C, or D\n"
        "A. A floating point number without a decimal\n"
        "B. A numeric type for whole numbers with no fractional part\n"
        "C. A string that stores only digits\n"
        "D. A mutable numeric object\n"
    )
    if answer.upper() == "B":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – Integers are whole numbers without decimals.")
        C = Coin_Loss(C)
    return C

def Question_6(C):
    answer = input(
        "What is a float in Python? A, B, C, or D\n"
        "A. A string containing a decimal point\n"
        "B. A whole number wrapped in a string\n"
        "C. A built-in module for math\n"
        "D. A numeric type used to represent decimal and fractional values\n"
    )
    if answer.upper() == "D":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – Floats are for decimal or fractional numbers.")
        C = Coin_Loss(C)
    return C
           
def Question_7(C):
    answer = input(
        "What is the purpose of the `print()` function in Python? A, B, C, or D\n"
        "A. To send data to a web server\n"
        "B. To return a value from a function\n"
        "C. To display output to the standard console\n"
        "D. To write text to a file\n"
    )
    if answer.upper() == "C":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – The `print()` function displays output on screen.")
        C = Coin_Loss(C)
    return C

def Question_8(C):
    answer = input(
        "How does a `while` loop work in Python? A, B, C, or D\n"
        "A. It executes code a fixed number of times\n"
        "B. It executes code until the loop variable exceeds a value\n"
        "C. It repeats a block of code while a condition is True\n"
        "D. It runs once regardless of the condition\n"
    )
    if answer.upper() == "C":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – A `while` loop runs as long as its condition is True.")
        C = Coin_Loss(C)
    return C
        
def Question_9(C):
    answer = input(
        "What is the role of an `if` statement in Python? A, B, C, or D\n"
        "A. It defines a function that only runs on error\n"
        "B. It compares two values without execution\n"
        "C. It executes a block of code based on a condition\n"
        "D. It imports a module if it exists\n"
    )
    if answer.upper() == "C":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – `if` checks a condition and executes if it's True.")
        C = Coin_Loss(C)
    return C
        
def Question_10(C):
    answer = input(
        "What is `elif` used for in Python? A, B, C, or D\n"
        "A. To repeat a block of code multiple times\n"
        "B. To declare multiple variables at once\n"
        "C. To define a conditional branch after an `if` condition fails\n"
        "D. To exit a loop early\n"
    )
    if answer.upper() == "C":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – `elif` allows for multiple conditional checks.")
        C = Coin_Loss(C)
    return C
        
def Question_11(C):
    answer = input(
        "What is the purpose of the `else` clause in Python's conditional logic? A, B, C, or D\n"
        "A. It runs if the `if` condition and all `elif` conditions are False\n"
        "B. It executes when the previous condition is True\n"
        "C. It is only used inside loops, not conditionals\n"
        "D. It always runs regardless of any conditions\n"
    )
    if answer.upper() == "A":
        print("Correct")
        C = Coin_Gain(C)
    else:
        print("Incorrect – `else` runs only if no prior conditions are met.")
        C = Coin_Loss(C)
    return C

coin = Question_1(coin)
coin = Question_2(coin)
coin = Question_3(coin)
coin = Question_4(coin)
coin = Question_5(coin)
coin = Question_6(coin)
coin = Question_7(coin)
coin = Question_8(coin)
coin = Question_9(coin)
coin = Question_10(coin)
coin = Question_11(coin)

print(f"\nQuiz Complete! You finished with {coin} coins.")

