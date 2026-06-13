
score = 0

# Question 1
answer1 = input("Q1. What is the capital of India? ")
if answer1.strip().lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong. The correct answer is Delhi.")

# Question 2
answer2 = input("Q2. 5 + 7 = ? ")
if answer2.strip() == "12":
    print("Correct!")
    score += 1
else:
    print("Wrong. The correct answer is 12.")

# Question 3
answer3 = input("Q3. Is Python a compiled or interpreted language? ")
if answer3.strip().lower() == "interpreted":
    print("Correct!")
    score += 1
else:
    print("Wrong. The correct answer is interpreted.")

print(f"\nYour final score: {score}/3")

if score == 3:
    print("Perfect score!")
elif score >= 2:
    print("Good job!")
else:
    print("Needs improvement.")