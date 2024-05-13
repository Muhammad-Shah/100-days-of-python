# Program to calculate the highiest score from a List of score

student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0

# Method : 1
for score in student_scores:
    if max_score < score:
        max_score = score
print(f"The highest score in the class is: {max_score}")


# Method : 2
print()
print(f"The highest score in the class is: {max(student_scores)}")
