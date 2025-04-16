import streamlit as st

def print_x_block(times):
    x_row = "X" * 1000000  # Much smaller row
    for _ in range(times):
        st.text(x_row)

st.title("X Printer 3000 🚀")

if st.button("Unleash the Xs"):
    st.write("Brace yourself...")
    print_x_block(10000)  # Reasonable number of rows
