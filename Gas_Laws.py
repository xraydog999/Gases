import streamlit as st
import random

st.title("Gas Laws Quiz")

st.write("This quiz contains 4 questions. The figure Gas_Laws.png is used for reference.")
st.image("Gas_Laws.png", caption="Gas Law Equations A–D")

# ---------------------------------------------------------
# QUIZ DATA (fixed order, rotating answer positions)
# ---------------------------------------------------------
questions = [
    {
        "question": "1. At constant temperature, a gas changes state from 2.6 L at 2 atm to a new pressure of 0.5 atm. Compute the new volume.",
        "correct": "C",
        "correct_text": "10.4 L (Boyle’s Law)",
        "distractors": ["2.6 L", "5.2 L"]
    },
    {
        "question": "2. At constant pressure, a gas at 0.20 L and 100 K changes to 250 K. Find the new volume.",
        "correct": "A",
        "correct_text": "0.50 L (Charles’ Law)",
        "distractors": ["0.32 L", "0.80 L"]
    },
    {
        "question": "3. A gas at 1 atm, 200 K, and 1.2 L changes to 150 K and 0.5 atm. Compute the new volume.",
        "correct": "B",
        "correct_text": "1.8 L (Combined Gas Law)",
        "distractors": ["0.9 L", "3.6 L"]
    },
    {
        "question": "4. Find the volume occupied by 0.2 moles of an ideal gas at 27°C and 0.5 atm.",
        "correct": "B",
        "correct_text": "98.5 L (Ideal Gas Law)",
        "distractors": ["49.2 L", "24.6 L"]
    }
]

# ---------------------------------------------------------
# RANDOM ROTATION OF ANSWERS A/B/C
# ---------------------------------------------------------
def rotate_choices(correct_text, distractors):
    choices = [correct_text] + distractors
    random.shuffle(choices)
    correct_label = ["A", "B", "C"][choices.index(correct_text)]
    return ["A", "B", "C"], choices, correct_label

# ---------------------------------------------------------
# DISPLAY QUESTIONS
# ---------------------------------------------------------
user_answers = []
correct_labels = []
correct_texts = []

st.subheader("Answer the questions below:")

for i, q in enumerate(questions):
    labels, rotated, correct_label = rotate_choices(q["correct_text"], q["distractors"])
    correct_labels.append(correct_label)
    correct_texts.append(q["correct_text"])

    st.write(q["question"])
    answer = st.radio(
        f"Select an answer for Question {i+1}:",
        labels,
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

    for i in range(len(questions)):
        user = user_answers[i]
        correct = correct_labels[i]
        correct_text = correct_texts[i]

        if user == correct:
            score += 1
            st.write(f"**Question {i+1}: Correct!**")
        else:
            st.write(f"**Question {i+1}: Incorrect.** Correct answer: {correct} ({correct_text})")

    st.write(f"### Final Score: {score} / {len(questions)}")
