# ================================
# AI Tutor – Student Testing MVP
# ================================

# ---------- Student Profile ----------
student_profile = {
    "student_id": "001",
    "language": "Python",
    "level": "beginner",
    "topics": {
        "variables": 0.0,
        "loops": 0.0,
        "functions": 0.0
    }
}


# ---------- Question Bank (MVP) ----------
QUESTION_BANK = {
    "variables": [
        {
            "question": "What is a variable in Python?",
            "options": [
                "A loop",
                "A container for storing data",
                "A function"
            ],
            "correct": 1
        },
        {
            "question": "Which symbol is used to assign a value?",
            "options": [
                "=",
                "==",
                "=>"
            ],
            "correct": 0
        }
    ],
    "loops": [
        {
            "question": "Which loop is used to iterate over a sequence?",
            "options": [
                "if",
                "for",
                "def"
            ],
            "correct": 1
        }
    ],
    "functions": [
        {
            "question": "Which keyword is used to define a function?",
            "options": [
                "func",
                "define",
                "def"
            ],
            "correct": 2
        }
    ]
}


# ---------- Test Functions ----------

def conduct_test(topic):
    print("\n==============================")
    print(f"Testing topic: {topic.upper()}")
    print("==============================")

    questions = QUESTION_BANK[topic]
    answers = []

    for i, q in enumerate(questions):
        print(f"\nQ{i+1}: {q['question']}")
        for idx, opt in enumerate(q["options"]):
            print(f"  {idx}. {opt}")

        while True:
            try:
                user_answer = int(input("Your answer: "))
                if user_answer in range(len(q["options"])):
                    break
            except ValueError:
                pass
            print("Invalid input. Try again.")

        answers.append(user_answer)

    return questions, answers


def evaluate_test(questions, answers):
    correct = 0
    for q, a in zip(questions, answers):
        if a == q["correct"]:
            correct += 1

    score = correct / len(questions)
    return round(score, 2)


def update_student_profile(profile, topic, score):
    profile["topics"][topic] = score


def analyze_results(profile):
    weak_topics = []
    for topic, score in profile["topics"].items():
        if score < 0.6:
            weak_topics.append(topic)
    return weak_topics


def give_feedback(score):
    if score >= 0.8:
        return "Excellent understanding!"
    elif score >= 0.6:
        return "Good, but needs some practice."
    else:
        return "Weak understanding. Review this topic."


# ---------- Main Program ----------

def main():
    print("\n=== AI Tutor: Student Testing System ===")

    for topic in student_profile["topics"]:
        questions, answers = conduct_test(topic)
        score = evaluate_test(questions, answers)
        update_student_profile(student_profile, topic, score)

        print(f"\nScore for '{topic}': {score * 100}%")
        print("Feedback:", give_feedback(score))

    weak_topics = analyze_results(student_profile)

    print("\n==============================")
    print("STUDENT PROFILE SUMMARY")
    print("==============================")
    print("Student ID:", student_profile["student_id"])
    print("Language:", student_profile["language"])
    print("Knowledge by topics:")

    for topic, score in student_profile["topics"].items():
        print(f"  {topic}: {score * 100}%")

    if weak_topics:
        print("\nRecommended topics to review:")
        for t in weak_topics:
            print(" -", t)
    else:
        print("\nAll topics are well understood!")

    print("\nNext step: Generate personal learning plan (AI).")


# ---------- Run ----------
#if __name__ == "__main__":
main()
