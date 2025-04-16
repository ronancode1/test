import streamlit as st

def print_x_block(times=100000):
    x_row = "X" * 1000000000 #Prints one long row of Xs
    for _ in range(times):
        st.text(x_row)

st.title("X Printer 3000 🚀")

if st.button("Unleash the Xs"):
    st.write("Brace yourself...")
    print_x_block(100000)  # You can change this number for more rows
