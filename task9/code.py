# Case Study 34: Student Feedback Sentiment Scoring

positive_words = ["good", "excellent", "helpful", "nice", "best"]
negative_words = ["bad", "poor", "boring", "worst", "difficult"]

feedbacks = [
    "The teacher is good and helpful",
    "The class is boring and difficult",
    "The teaching is excellent",
    "The subject is bad"
]

for feedback in feedbacks:
    positive = 0
    negative = 0

    words = feedback.lower().split()

    for word in words:
        word = word.strip(".,!?")

        if word in positive_words:
            positive += 1
        elif word in negative_words:
            negative += 1

    score = positive - negative

    print("\nFeedback:", feedback)
    print("Positive words:", positive)
    print("Negative words:", negative)
    print("Sentiment score:", score)

    if score > 0:
        print("Result: Positive Feedback")
    elif score < 0:
        print("Result: Negative Feedback")
    else:
        print("Result: Neutral Feedback")
