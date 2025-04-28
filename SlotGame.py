import streamlit as st
import random

# Constants
MAX_LINES = 3
CARD_BALANCE = 500
MIN_BET = 1
MAX_BET = 1000000

ROWS = 3
COLS = 3

symbol_count = {
    "🍀": 1,
    "💎": 3,
    "⭐": 5,
    "🍒": 7,
}

symbol_value = {
    "🍀": 10,
    "💎": 7,
    "⭐": 4.5,
    "🍒": 3.5,
}

# Functions
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

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

def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += symbol_value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def display_slot_machine(columns):
    for row in range(len(columns[0])):
        row_symbols = [column[row] for column in columns]
        st.write(" | ".join(row_symbols))

# Streamlit App
st.title("🎰 Slot Machine Game")
st.write("Welcome to the Streamlit Casino!")

if "card_balance" not in st.session_state:
    st.session_state.card_balance = CARD_BALANCE

# Deposit
with st.form("deposit_form"):
    deposit_amount = st.number_input("Enter deposit amount:", min_value=1, max_value=st.session_state.card_balance, step=1)
    submit_deposit = st.form_submit_button("Deposit")
    if submit_deposit:
        st.session_state.spending_money = deposit_amount
        st.session_state.card_balance -= deposit_amount
        st.success(f"Deposited ${deposit_amount}. Remaining card balance: ${st.session_state.card_balance}")

# Betting
if "spending_money" in st.session_state:
    with st.form("betting_form"):
        lines = st.slider("Select number of lines to bet on:", 1, MAX_LINES, 1)
        bet_per_line = st.number_input("Enter your bet per line:", min_value=MIN_BET, max_value=MAX_BET, step=1)
        total_bet = lines * bet_per_line

        submitted_bet = st.form_submit_button("Spin!")
        if submitted_bet:
            if total_bet > st.session_state.spending_money:
                st.error(f"Not enough funds! You have ${st.session_state.spending_money} available.")
            else:
                slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
                st.subheader("🎰 Spin Result:")
                display_slot_machine(slots)

                winnings, winning_lines = check_winnings(slots, lines, bet_per_line)
                st.session_state.spending_money -= total_bet
                st.session_state.spending_money += winnings

                if winnings > 0:
                    st.success(f"You won ${winnings} on lines {', '.join(map(str, winning_lines))}!")
                else:
                    st.error("No win this time!")

                st.info(f"Current game balance: ${st.session_state.spending_money}")
                st.info(f"Card balance (outside game): ${st.session_state.card_balance}")

    if st.button("Cash Out"):
        st.session_state.card_balance += st.session_state.spending_money
        st.success(f"You cashed out ${st.session_state.spending_money}! New card balance: ${st.session_state.card_balance}")
        del st.session_state.spending_money