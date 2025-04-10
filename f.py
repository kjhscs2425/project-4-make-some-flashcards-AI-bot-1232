import json
import random
import os

questions = {
    "What year did the Titanic sink in the Atlantic Ocean on its maiden voyage?": "1912",
    "What is the capital city of Canada?": "Ottawa",
    "Which planet is known as the Red Planet?": "Mars",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "What is the smallest country in the world?": "Vatican City",
    "Who developed the theory of evolution by natural selection?": "Charles Darwin",
    "What is the chemical symbol for the element oxygen?": "O",
    "In what year did World War II end?": "1945",
    "What is the largest bone in the human body?": "Femur",
    "Which element has the atomic number 1?": "Hydrogen",
    "Who painted the ceiling of the Sistine Chapel?": "Michelangelo",
    "What is the longest river in the world?": "Nile",
    "Who is the author of the Harry Potter book series?": "J.K. Rowling",
    "What is the square root of 256?": "16",
    "Who was the first man to step on the Moon?": "Neil Armstrong",
    "What is the largest desert in the world?": "Antarctica",
    "What is the chemical formula for water?": "H2O",
    "Who is known as the 'Father of Modern Physics'?": "Albert Einstein",
    "What is the capital city of Australia?": "Canberra",
    "What is the hardest natural substance on Earth?": "Diamond",
}

try:
    if os.path.exists("memory.json") and os.path.getsize("memory.json") > 0:
        with open("memory.json", 'r') as f:
            data = json.load(f)
    else:
        data = {}
except:
    data = {}

# Initialize data for each question
for question in questions.keys():
    if question not in data:
        data[question] = {"attempts": []}

# Get questions as list and shuffle
items = list(questions.items())
random.shuffle(items)

correct_count = 0
total_questions = len(items)

print("\n--Naveen's Flashcard Quiz ")
print("Enter your answers. Press Enter to see the correct answer.")
print("Spelling doesn't matter")
# Loop through questions
for question, correct_answer in items:
    user_answer = input(f"\nQ: {question}\nMy answer: ").strip().lower()
    print(f"Correct Answer: {correct_answer}")
    
    # Check if answer is correct
    is_correct = user_answer.lower() in correct_answer.lower()
    
    if is_correct:
        print("Great Job! You got it correct")
        correct_count += 1
    else:
        print("Incorrect")
    
    # Save the attempt without date
    data[question]["attempts"].append({
        "correct": is_correct
    })

# Save data
with open("memory.json", "w") as f:
    json.dump(data, f, indent=4)

# After completing the quiz loop, calculate and display the statistics
# Current session statistics
print(f"\n--- Current Session Performance ---")
print(f"Correct Answers: {correct_count}/{total_questions}")
current_percentage = (correct_count / total_questions) * 100
print(f"Accuracy: {current_percentage:.2f}%")

# Calculate all-time statistics
all_time_correct = 0
all_time_attempts = 0

for question in data:
    question_attempts = len(data[question]["attempts"])
    all_time_attempts += question_attempts
    
    for attempt in data[question]["attempts"]:
        if attempt["correct"]:
            all_time_correct += 1

print("\n--- Overall Performance History ---")
print(f"Total Questions Answered: {all_time_attempts}")
print(f"Total Correct Answers: {all_time_correct}/{all_time_attempts}")

if all_time_attempts > 0:
    all_time_percentage = (all_time_correct / all_time_attempts) * 100
    print(f"Overall Accuracy: {all_time_percentage:.2f}%")