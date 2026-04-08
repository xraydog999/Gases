import streamlit as st

st.title("Gas Laws Quiz")

st.write("This quiz contains 4 questions. The figure Gas_Laws.png is used for reference only.")
st.image("Gas_Laws.png", caption="Gas Law Equations A–D")

# ---------------------------------------------------------
# QUIZ DATA (fixed order, fixed answer positions)
# ---------------------------------------------------------
questions = [
    {
        "question": "1. At constant temperature, a gas changes from 2.6 L at 2 atm to a new pressure of 0.5 atm. Compute the new volume.",
        "choices": {
            "A": "2.6 L",
            "B": "5.2 L",
            "C": "10.6 L"
        },
        "correct": "C"
    },
    {
        "question": "2. At constant pressure, a gas at 0.20 L and 100 K changes to 250 K. Find the new volume.",
        "choices": {
            "A": "0.50 L",
            "B": "0.32 L",
            "C": "0.80 L"
        },
        "correct": "A"
    },
    {
        "question": "3. A gas at 1 atm, 200 K, and 1.2 L changes to 150 K and 0.5 atm. Compute the new volume.",
        "choices": {
            "A": "0.9 L",
            "B": "1.8 L",
            "C": "3.6 L"
        },
        "correct": "B"
    },
    {
        "question": "4. Find the volume occupied by 0.2 moles of an ideal gas at 27°C and 0.5 atm.",
        "choices": {
            "A": "49.2 L",
            "B": "24.6 L",
            "C": "98.5 L"
        },
        "correct": "C"
    }
]

# ---------------------------------------------------------
# DISPLAY QUESTIONS (NO SHUFFLING)
# ---------------------------------------------------------
user_answers = []

st.subheader("Answer the questions below:")

for i, q in enumerate(questions):
    st.write(q["question"])
    answer = st.radio(
        f"Select an answer for Question {i+1}:",
        list(q["choices"].keys()),
        format_func=lambda x, d=q["choices"]: f"{x}: {d[x]}",
        index=None,
        key=f"q{i}"
    )
    user_answers.append(answer)

st.write("---")

# ---------------------------------------------------------
# SUBMIT BUTTON
# ---------------------------------------------------------
if st.button("Submit Quiz"):
    score = 0
    st.subheader("Results")

    for i, q in enumerate(questions):
        user = user_answers[i]
        correct = q["correct"]
        correct_text = q["choices"][correct]

        if user == correct:
            score += 1
            st.write(f"**Question {i+1}: Correct!**")
        else:
            st.write(f"**Question {i+1}: Incorrect.** Correct answer: {correct} ({correct_text})")

    st.write(f"### Final Score: {score} / {len(questions)}")
