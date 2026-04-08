import streamlit as st
import random

st.title("Gases Quiz")

st.write("This quiz contains 11 questions. The first seven use the attached figure (Graphs.png).")
st.image("Graphs.png", caption="Graphs A, B, C, and D")

# ---------------------------------------------------------
# QUIZ DATA (fixed order, but answer positions will rotate)
# ---------------------------------------------------------
questions = [
    {
        "question": "1. Using the figure, which selection represents Boyle's Law?",
        "options": ["A", "B", "C"],
        "correct": "D"
    },
    {
        "question": "2. Using the figure, which selection represents Charles' Law?",
        "options": ["A", "B", "C"],
        "correct": "B"
    },
    {
        "question": "3. Using the figure, which one represents constant temperature with time?",
        "options": ["A", "B", "C"],
        "correct": "A"
    },
    {
        "question": "4. Which graph in the figure represents a direct proportion?",
        "options": ["A", "B", "C"],
        "correct": "B"
    },
    {
        "question": "5. Which graph in the figure represents an inverse proportion or hyperbola?",
        "options": ["A", "B", "C"],
        "correct": "D"
    },
    {
        "question": "6. Which graph in the figure could represent y = 0.40?",
        "options": ["A", "B", "C"],
        "correct": "A"
    },
    {
        "question": "7. Which graph could represent exponential growth?",
        "options": ["A", "B", "C"],
        "correct": "C"
    },
    {
        "question": "8. At constant temperature, if the pressure of an ideal gas is quadrupled, its volume is decreased by a factor of:",
        "options": ["1/4", "1/2", "4"],
        "correct": "1/4"
    },
    {
        "question": "9. At constant pressure, if the temperature of an ideal gas is quadrupled, its volume:",
        "options": ["Doubles", "Increases by 4", "Decreases by 4"],
        "correct": "Increases by 4"
    },
    {
        "question": "10. What kind of proportion is Boyle's Law?",
        "options": ["Direct", "Inverse", "Quadratic"],
        "correct": "Inverse"
    },
    {
        "question": "11. What kind of proportion is Charles' Law?",
        "options": ["Inverse", "Direct", "Logarithmic"],
        "correct": "Direct"
    }
]

# ---------------------------------------------------------
# RANDOM ROTATION OF ANSWERS A/B/C
# ---------------------------------------------------------
def rotate_three_choices(correct_answer, wrong_answers):
    """
    Takes the correct answer and two wrong answers,
    shuffles them, and assigns them to A, B, C.
    Returns:
        labels -> ["A", "B", "C"]
        displayed_answers -> shuffled answers
        correct_label -> "A" or "B" or "C"
    """
    displayed = [correct_answer] + wrong_answers
    random.shuffle(displayed)

    correct_label = ["A", "B", "C"][displayed.index(correct_answer)]
    return ["A", "B", "C"], displayed, correct_label


# ---------------------------------------------------------
# DISPLAY QUESTIONS
# ---------------------------------------------------------
user_answers = []
correct_labels = []

st.subheader("Answer the questions below:")

for i, q in enumerate(questions):

    # For graph questions, the "correct" is A/B/C/D but we only display A/B/C
    # So we treat the correct answer as a label, not a text answer.
    if q["correct"] in ["A", "B", "C", "D"]:
        correct_text = q["correct"]
        wrong_texts = [x for x in ["A", "B", "C"] if x != correct_text][:2]
    else:
        # For conceptual questions, correct is text
        correct_text = q["correct"]
        wrong_texts = [opt for opt in q["options"] if opt != correct_text]

    labels, displayed, correct_label = rotate_three_choices(correct_text, wrong_texts)
    correct_labels.append(correct_label)

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

    for i, q in enumerate(questions):
        user = user_answers[i]
        correct = correct_labels[i]

        if user == correct:
            score += 1
            st.write(f"**Question {i+1}: Correct!**")
        else:
            st.write(f"**Question {i+1}: Incorrect.** Correct answer: {correct}")

    st.write(f"### Final Score: {score} / {len(questions)}")
