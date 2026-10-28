# Case Study 31: Examination Answer Evaluation

answer_key = ["A", "B", "C", "D", "A"]
answers = []

for i in range(5):
    ans = input("Enter answer for question " + str(i + 1) + " (A/B/C/D or blank): ")
    answers.append(ans.upper())

correct = 0
incorrect = 0
unanswered = 0

for i in range(5):
    if answers[i] == "":
        unanswered += 1
    elif answers[i] == answer_key[i]:
        correct += 1
    else:
        incorrect += 1

score = (correct * 2) - (incorrect * 0.5)

print("\n--- Examination Result ---")
print("Correct Answers:", correct)
print("Incorrect Answers:", incorrect)
print("Unanswered Questions:", unanswered)
print("Final Score:", score, "out of 10")
