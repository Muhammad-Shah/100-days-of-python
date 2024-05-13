# Program that calculates average student height from a list of heights

student_heights = input("Input a list of student height: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0;
for height in student_heights:
    total_height += height

number_of_students = 0
for student in student_heights:
    number_of_students += 1

average = total_height/number_of_students
print(round(average, 1))