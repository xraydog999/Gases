import streamlit as st
import random

st.title("Gases Quiz")

st.write("This quiz contains 11 questions. The first seven use the attached figure (Graphs.png).")
st.image("Graphs.png", caption="Graphs A, B, C, and D")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    {
        "question": "1. Using the figure, which selection represents Boyle's Law?",
        "choices": ["A", "B", "C", "D"],
        "correct": "D"
    },
    {
        "question": "2. Using the figure, which selection represents Charles' Law?",
        "choices": ["A", "B", "C", "D"],
        "correct": "B"
    },
    {
        "question": "3. Using the figure, which one represents constant temperature with time?",
        "choices": ["A", "B", "C", "D"],
        "correct": "A"
    },
    {
        "question": "4. Which graph in the figure represents a direct proportion?",
        "choices": ["A", "B", "C", "D"],
        "correct": "B"
    },
    {
        "question": "5. Which graph in the figure represents an inverse proportion or hyperbola?",
        "choices": ["A", "B", "C", "D"],
        "correct": "D"
    },
    {
        "question": "6. Which graph in the figure could represent y = 0.40?",
        "choices": ["A", "B", "C", "D"],
        "correct": "A"
    },
    {
        "question": "7. Which graph could represent exponential growth?",
        "choices": ["A", "B", "C", "D"],
        "correct": "C"
    },
    {
        "question": "8. At constant temperature, if the pressure of an ideal gas is quadrupled, its volume is decreased by a factor of:",
        "choices": ["1/2", "4", "1/4"],
        "correct": "4"
    },
    {
        "question": "9. At constant pressure, if the temperature of an ideal gas is quadrupled, its volume:",
        "choices": ["Doubles", "Increases by 4", "Decreases by 4"],
        "correct": "Increases by 4"
    },
    {
        "question": "10. What kind of proportion is Boyle's Law?",
        "choices": ["Direct", "Inverse", "Quadratic"],
        "correct": "Inverse"
    },
    {
        "question": "11. What kind of proportion is Charles' Law?",
        "choices": ["Inverse", "Direct", "Logarithmic"],
        "correct": "Direct"
    }
]

# -----------------------------
# RANDOM ROTATION OF ANSWERS
# -----------------------------
def rotate_choices(q):
    choices = q["choices"].copy()
    random.shuffle(choices)
    correct_choice = q["correct"]
    # Map correct answer to its new label
    for c in choices:
        if c == correct_choice:
            correct_label = c
    return choices, correct_choice

# Store user answers
user_answers = []

st.subheader("Answer the questions below:")

for i, q in enumerate(questions):
    st.write(q["question"])

    # Rotate choices A/B/C randomly
    choices = q["choices"].copy()
    random.shuffle(choices)

    # Display radio buttons
    answer = st.radio(
        f"Select an answer for Question {i+1}:",
        choices,
        index=None,
        key=f"q{i}"
    )
    user_answers.append(answer)

st.write("---")

# -----------------------------
# SUBMIT BUTTON
# -----------------------------
if st.button("Submit Quiz"):
    score = 0
    st.subheader("Results")

    for i, q in enumerate(questions):
        correct = q["correct"]
        user = user_answers[i]

        if user == correct:
            score += 1
            st.write(f"**Question {i+1}: Correct!**")
        else:
            st.write(f"**Question {i+1}: Incorrect.** Correct answer: {correct}")

    st.write(f"### Final Score: {score} / {len(questions)}")
