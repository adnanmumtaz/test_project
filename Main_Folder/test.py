print("Welcome to Quiz App")
score = 0
answer1 = input("What does CPU stands for: ")
if answer1 == "Central Processing Unit":
    score += 1
    print("Correct")
else:
    print("Incorrect")

answer2 = input("What does ALU stands for: ")
if answer2 == "Arithematic and Logic Unit":
    score += 1
    print("Correct")
else:
    print("Incorrect")

answer3 = input("Who is PM of Pakistan: ")
if answer3 == "Shahbaz Sharif":
    score += 1
    print("Correct")
else:
    print("Incorrect")

print("Your score is:", score)
print("You got " + str(((score / 3) * 100)) + " percent")
