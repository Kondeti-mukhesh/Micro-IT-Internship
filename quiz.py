import json
import time
import random

# Load questions from JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

# Shuffle the questions
random.shuffle(questions)
questions = random.sample(questions, 10)

# Welcome message
print("🎉 Welcome to the Python Quiz Game! 🎉")
print("Choose the correct option: A, B, C, or D")
print("⏳ You will have 10 minutes to answer each question.")
print("🔀 10 unique questions will be randomly selected from a pool of 50 each time.\n")

# Track score and wrong answers
score = 0
wrong_answers = []
start_time = time.time()
time_limit=600


# Ask questions
for q in questions:
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("\n⏰ Time's up! The 10-minute limit has been reached.")
        break 

    print(q["question"])
    for key, value in q["options"].items():
        print(f"{key}. {value}")

    user_answer = input("Your answer: ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct answer!\n")
        score = score+1

    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")
        wrong_answers.append({
            "question": q["question"],
            "your_answer": user_answer,
            "correct_answer": q["answer"]
        })

# Stop the timer
end_time = time.time()
total_time = round(end_time - start_time, 2)

# Final result
print(f"\n🏁 Quiz Over! You scored {score} out of {len(questions)}.")
print(f"⏱️ Time Taken: {total_time} seconds")

# Feedback based on score
if score == len(questions):
    print("🎉 Perfect Score! You're a Python Pro!")
elif score >= 6:
    print("👍 Great Job! Keep practicing.")
else:
    print("📚 Don't worry! Study more and try again.")

# Review incorrect answers
if wrong_answers:
    print("\n📋 Review of Incorrect Answers:")
    for wa in wrong_answers:
        print(f"Q: {wa['question']}")
        print(f"   ❌ Your Answer: {wa['your_answer']}")
        print(f"   ✅ Correct Answer: {wa['correct_answer']}\n")

