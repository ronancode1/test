import random
import time

print("Welcome to the Math Game!")
print("You will be given a math problem to solve.")

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 25

Total_Problems = 1

def generate_problem():
    Left = random.randint(MIN_OPERAND, MAX_OPERAND)
    Right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(Left) + " " + operator + " " + str(Right)

    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press Enter to start the game!")
print("____________________________")

start_time = time.time()

for i in range(Total_Problems):
    expr, answer = generate_problem()
    while True:

        user_answer = input("Problem #" + str(i + 1) + ": " + expr + " = ")

        if user_answer == str(answer):
            print("Correct!")
            break
        else:
            print("Incorrect. Try again.")
            wrong += 1

end_time = time.time()
total_time = end_time - start_time
total_time = round(total_time, 2)
if total_time >= 60:
    total_time = round(total_time / 60, 2)
    print("____________________________")
    print("Nice Work! You finished In", total_time, "Minutes.")
    print("You got " + str(wrong) + " wrong")
else:
    print("____________________________")
    print("Nice Work! You finished In", total_time, "Seconds.")
    print("You got " + str(wrong) + " wrong")






