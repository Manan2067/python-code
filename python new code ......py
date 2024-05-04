from questions import QUESTIONS as Q
from easy_questions import EASY_QUESTIONS as EQ  # Importing easy quiz questions

# Function to conduct the easy quiz
def conduct_easy_quiz():
    print("EASY QUIZ ON INDIAN HISTORY")
    print("Take an Easy Quiz")
    print()

    score_easy = 0
    for index, question in enumerate(EQ, 1):
        print(f"{index}. {question['ques']}")
        options = question["opt"]
        for i, option in enumerate(options, 1):
            print(f"   {i}. {option}")

        ans = int(question["ans"])
        user_ans = int(input("Enter your answer (1, 2, 3, or 4): "))
        if user_ans == ans:
            score_easy += 1
            print("Correct!")
        else:
            print("Incorrect!")
    
    print(f"Your Easy Quiz Score is {score_easy}")
    return score_easy

# Ask for student's details
student_name = input("Enter your name: ")

# Ensure SAP ID is 9 numeric digits
while True:
    sap_id = input("Enter your SAP ID (9 digits only): ")
    if sap_id.isdigit() and len(sap_id) == 9:
        break
    else:
        print("Please enter a 9-digit numeric SAP ID.")

# Ensure roll number is 11 numeric digits
while True:
    roll_no = input("Enter your roll number (11 digits only): ")
    if roll_no.isdigit() and len(roll_no) == 11:
        break
    else:
        print("Please enter an 11-digit numeric roll number.")

# Ask for guardian's details
guardian_name = input("Enter your guardian's name: ")

# Ensure guardian's contact is 10 numeric digits
while True:
    guardian_contact = input("Enter your guardian's contact information (10 digits only): ")
    if guardian_contact.isdigit() and len(guardian_contact) == 10:
        break
    else:
        print("Please enter a 10-digit numeric contact number.")

score = 0
isQuizON = True
QNo = 0

print("QUIZ ON INDIAN HISTORY")
print("Take a Quiz")
print()

print("How much do you know about Indian history?")
print("a. A lot")
print("b. Good knowledge")
print("c. Some")
print("d. A little")

knowledge_level = input("Enter your choice (a, b, c, or d): ").lower()

if knowledge_level == 'yes':
    print("The quiz will be available on your gmail id by next week.")
else:
    print("Thank you for your time.")

while isQuizON:
    if QNo > len(Q)-1:
        print("Thanks For Taking The Quiz")
        print(f"Your Score is {score}")

        # If score is less than 5, conduct the easy quiz
        if score < 5:
            print("Since your score is less than 5, you are eligible for an Easy Quiz.")
            easy_score = conduct_easy_quiz()
            print(f"Your Total Score (including easy quiz): {score + easy_score}")
        else:
            print("You scored well. No need for the Easy Quiz.")

        # Write "THANKS FOR TAKING THE QUIZ" to a file
        with open("thanks_message.txt", "w") as file:
            file.write("THANKS FOR TAKING THE QUIZ\n")
        
        # Provide the score to the guardian
        print(f"Dear {guardian_name}, {student_name} scored {score} in the quiz.")
        
        break
    
    question = Q[QNo]["ques"]
    options = Q[QNo]["opt"]
    ans = Q[QNo]["ans"]
    optionList = ["a", "b", "c", "d"]

    print(f"Q{QNo+1}.{question}")
    for i in range(4):
        print(f" {optionList[i]}. {options[i]}")

    inp = input("Enter The Option (or type 'skip' to skip this question): ").lower()

    if inp == 'skip':
        QNo += 1
        print("Question skipped.")
        continue

    if inp not in optionList:
        print("Please Enter a valid option")
        continue

    if inp == ans:
        score += 1
        QNo += 1
        print(f"Correct! The answer is {ans}")
        print(f"Score: {score}")
    else:
        print("Wrong Answer! Try Again.")
        QNo += 1

# Ask for feedback
print("\nPlease provide your feedback on the quiz:")
print("1. You enjoyed it")
print("2. You found it hard")
print("3. It was moderate")

feedback_choice = input("Enter your feedback choice (1, 2, or 3): ")

feedback = ""
if feedback_choice == "1":
    feedback = "You enjoyed it"
elif feedback_choice == "2":
    feedback = "You found it hard"
elif feedback_choice == "3":
    feedback = "It was moderate"
else:
    feedback = "Invalid feedback choice"

# Display feedback
print("Thank you for your feedback!")
print(f"Student Name: {student_name}")
print(f"SAP ID: {sap_id}")
print(f"Roll Number: {roll_no}")
print(f"Guardian's Name: {guardian_name}")
print(f"Guardian's Contact: {guardian_contact}")
print(f"Quiz Score: {score}")
print(f"Feedback: {feedback}")

# Write "THANKS FOR TAKING THE QUIZ" to a file
with open("thanks_message.txt", "w") as file:
    file.write("THANKS FOR TAKING THE QUIZ\n")
