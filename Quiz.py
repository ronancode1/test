import streamlit as st


st.title("🧠 Python Quiz Game")
st.subheader("Answer all questions below. Click **Submit Answers** to find out how many coins you earned!")

# Initialize session state for coins and submission
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "coin" not in st.session_state:
    st.session_state.coin = 0

# Reset button
if st.button("🔄 Reset Quiz"):
    st.session_state.submitted = False
    st.session_state.coin = 0
    for i in range(11):
        st.session_state[f"q{i}"] = None
    st.experimental_rerun()

# Questions and answers
questions = [
    {
        "text": "What best describes a Python list?",
        "options": {
            "A": "An immutable sequence of items",
            "B": "A hash table implementation",
            "C": "A mutable ordered collection of heterogeneous elements",
            "D": "A type of numeric iterable used in loops",
        },
        "correct": "C",
        "explanation": "A list is mutable, ordered, and can store different data types.",
    },
    {
        "text": "What is a variable in Python?",
        "options": {
            "A": "A reserved keyword that defines a data type",
            "B": "A named location used to store data in memory",
            "C": "A constant reference to an object",
            "D": "A method used to access object attributes",
        },
        "correct": "B",
        "explanation": "A variable is a named reference to a value stored in memory.",
    },
    {
        "text": "Which option best defines a Python function?",
        "options": {
            "A": "A block of code that executes automatically when defined",
            "B": "A reusable block of code that runs when called and can return a value",
            "C": "A list of statements inside a loop",
            "D": "A Python object that holds only strings",
        },
        "correct": "B",
        "explanation": "Functions must be called and can return results.",
    },
    {
        "text": "Which best describes a Python string (`str`)?",
        "options": {
            "A": "An immutable sequence of Unicode characters",
            "B": "A mutable sequence of bytes",
            "C": "A numeric object that stores integers as text",
            "D": "A list of ASCII values",
        },
        "correct": "A",
        "explanation": "Strings are immutable and made of Unicode characters.",
    },
    {
        "text": "What defines a Python integer (`int`)?",
        "options": {
            "A": "A floating point number without a decimal",
            "B": "A numeric type for whole numbers with no fractional part",
            "C": "A string that stores only digits",
            "D": "A mutable numeric object",
        },
        "correct": "B",
        "explanation": "Integers are whole numbers without decimals.",
    },
    {
        "text": "What is a float in Python?",
        "options": {
            "A": "A string containing a decimal point",
            "B": "A whole number wrapped in a string",
            "C": "A built-in module for math",
            "D": "A numeric type used to represent decimal and fractional values",
        },
        "correct": "D",
        "explanation": "Floats are for decimal or fractional numbers.",
    },
    {
        "text": "What is the purpose of the `print()` function in Python?",
        "options": {
            "A": "To send data to a web server",
            "B": "To return a value from a function",
            "C": "To display output to the standard console",
            "D": "To write text to a file",
        },
        "correct": "C",
        "explanation": "The `print()` function displays output on screen.",
    },
    {
        "text": "How does a `while` loop work in Python?",
        "options": {
            "A": "It executes code a fixed number of times",
            "B": "It executes code until the loop variable exceeds a value",
            "C": "It repeats a block of code while a condition is True",
            "D": "It runs once regardless of the condition",
        },
        "correct": "C",
        "explanation": "A `while` loop runs as long as its condition is True.",
    },
    {
        "text": "What is the role of an `if` statement in Python?",
        "options": {
            "A": "It defines a function that only runs on error",
            "B": "It compares two values without execution",
            "C": "It executes a block of code based on a condition",
            "D": "It imports a module if it exists",
        },
        "correct": "C",
        "explanation": "`if` checks a condition and executes if it's True.",
    },
    {
        "text": "What is `elif` used for in Python?",
        "options": {
            "A": "To repeat a block of code multiple times",
            "B": "To declare multiple variables at once",
            "C": "To define a conditional branch after an `if` condition fails",
            "D": "To exit a loop early",
        },
        "correct": "C",
        "explanation": "`elif` allows for multiple conditional checks.",
    },
    {
        "text": "What is the purpose of the `else` clause in Python's conditional logic?",
        "options": {
            "A": "It runs if the `if` condition and all `elif` conditions are False",
            "B": "It executes when the previous condition is True",
            "C": "It is only used inside loops, not conditionals",
            "D": "It always runs regardless of any conditions",
        },
        "correct": "A",
        "explanation": "`else` runs only if no prior conditions are met.",
    },
]

# Display all questions
for i, q in enumerate(questions):
    st.radio(
        label=f"**Q{i+1}:** {q['text']}",
        options=[f"{key}. {value}" for key, value in q["options"].items()],
        key=f"q{i}",
        index=None,
    )

# Submit button
if st.button("✅ Submit Answers"):
    st.session_state.submitted = True
    st.session_state.coin = 0  # Reset coins before evaluation

    st.markdown("---")
    st.header("Results:")

    for i, q in enumerate(questions):
        user_answer = st.session_state.get(f"q{i}")
        if user_answer:
            letter = user_answer[0]
            if letter == q["correct"]:
                st.success(f"✅ Question {i+1}: Correct!")
                st.session_state.coin += 1
            else:
                st.error(f"❌ Question {i+1}: Incorrect!")
                st.info(f"**Explanation:** {q['explanation']}")
        else:
            st.warning(f"⚠️ Question {i+1}: No answer selected.")

# Final score
if st.session_state.submitted:
    st.markdown("---")
    st.subheader(f"🎉 You finished with **{st.session_state.coin}** coins!")

