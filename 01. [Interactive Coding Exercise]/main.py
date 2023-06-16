# 🚨 Don't change the code below 👇🏻
student_heights = input(' Input a list of students heights: ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)
# 🚨 Don't change the code above 👆🏻

# Write your code below this line 👇🏻
total_height = 0

for height in student_heights:
    total_height += height
# print(total_height)

number_of_students = 0

for number in student_heights:
    number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)
# Write your code above this line 👆🏻