# Slot Machine Game
import random

MAX_LINES = 3
CARD_BALENCE = 500
MIN_BET = 1
MAX_BET = 1000000

ROWS = 3
COLS = 3

symbol_count = {
    " 🍀 ": 1,
    " 💎 ": 3,
    " ⭐ ": 5,
    " 🍒 ": 7,
}

symbol_value = {
    " 🍀 ": 10,
    " 💎 ": 7,
    " ⭐ ": 4.5,
    " 🍒 ": 3.5,
}

def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_value[symbol] * bet
            winning_lines.append(line + 1)
            print(winnings)
            
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
                
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print()
        

    
def confirm_deposit(a):
    print(f"Your Deposit Amount Is: ${a} \nPlease Confirm")
    while True:
        confirmation = input("Press 'y' to confirm or 'n' to cancel: ").lower()
        if confirmation == "y":
            global CARD_BALENCE
            CARD_BALENCE = CARD_BALENCE - a
            print(f"Your Deposit Amount Of ${a} Has Been Confirmed")
            return CARD_BALENCE
        elif confirmation == "n":
            print("Deposit Cancelled")
            reenter = input("Would You Like To Re-Enter The Amount? (y/n): ").lower()
            if reenter == "y":
                deposit()
                break
            elif reenter == "n":
                print("Thank You For Playing!")
                exit()
        else:
            print("Invalid Input. Please Press 'y' to confirm or 'n' to cancel.")
            continue
def deposit():
    while True:
        amount = input("What Would You Like To Deposit? Press 'q' to Quit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 and amount <= CARD_BALENCE:
                confirm_deposit(amount)
                return amount
            elif amount > CARD_BALENCE:
                print("You Dont Have Enough Money Please Enter Another Amount")
                continue
        elif amount.lower() == "q":
            exit()
        else:
            print("Please Enter A Number")
            continue

def Betting():
    global CARD_BALENCE
    def get_number_of_lines():
        while True:
            lines = input("Enter The Number Of Lines To Bet On (1-" + str(MAX_LINES)+ ")?: ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter A Valid Number Of Lines")
            else:
                print("Please Enter A Number")
                continue
        return lines
            
    def get_bet():
        while True:
            bet = input("What Would You Like To Bet On Each Line? $")
            if bet.isdigit():
                bet = int(bet)
                if MIN_BET <= bet <= MAX_BET:
                    if bet * lines > spending_money:
                        print(f"You Do Not Have Enough Money To Bet ${bet} On {lines} Lines. Please Enter A Lower Bet.")
                        continue
                    elif bet * lines <= spending_money:
                        print(f"Your Bet Of ${bet} On {lines} Lines Has Been Confirmed")
                        break
                else:
                    print(f"Please Enter A Bet Between ${MIN_BET} - ${MAX_BET}.")
                    continue
            else:
                print("Please Enter A Number")
                continue
        return bet

    spending_money = deposit()  
    print(f"You Deposited ${spending_money} And Your Current Card Balance Is: ${CARD_BALENCE}")
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"You Are Betting ${bet} On {lines} Lines With A Total Bet Of ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet)
    
    print(f"Your Total Winnings Are: ${winnings}")
    if winnings == 0:
        print("You Lost!")
        CARD_BALENCE = CARD_BALENCE + (spending_money - total_bet)
        CARD_BALENCE = int(CARD_BALENCE)
    else:
        print(f"You Won On Lines:", *winning_lines)
        CARD_BALENCE = CARD_BALENCE + winnings
        CARD_BALENCE = int(CARD_BALENCE)
    print(f"Your New Balance Is: ${CARD_BALENCE}")
    while True:
        play_again = input("Would You Like To Bet Again? (y/n): ").lower()
        if CARD_BALENCE == 0:
            print("You Have No Money Left!")
            exit()
        elif play_again == "y":
            Betting()
            break
        elif play_again == "n":
            print("Thank You For Playing!")
            exit()
       
        else:
            print("Invalid Input. Please Press 'y' to play again or 'n' to quit.")
            continue

Betting()