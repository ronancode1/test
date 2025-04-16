import streamlit as st

st.title("🌈 Welcome to the Gay Tester!")

# Collect user input
gender = st.radio("What is your gender?", ["Male", "Female"])
orientation = st.selectbox("What is your sexual orientation?", ["Gay", "Lesbian", "Bisexual", "Straight"])
behavior = st.selectbox("What sexual orientation do you *act like*?", ["Gay", "Lesbian", "Bisexual", "Straight"])

# Convert inputs to lowercase for logic
gender = gender.lower()
orientation = orientation.lower()
behavior = behavior.lower()

# Output logic
st.markdown("## Result:")

if behavior in ["gay", "lesbian"]:
    st.success("You are **Straight**.")
elif behavior == "bisexual":
    st.success("You are **Bisexual**.")
elif behavior == "straight":
    if gender == "male":
        st.success("You are **Gay**.")
    elif gender == "female":
        st.success("You are **Lesbian**.")
    else:
        st.warning("Couldn't determine based on gender.")
else:
    st.error("Something went wrong. Please check your inputs.")

