#average height
import random
student_height_test = [random.randint(156, 178) for i in range(5)]
total_height = 0
no_of_students = 0
for height in student_height_test:
  total_height+=height
  no_of_students+=1
print(f"total height {total_height}")
print(f"no of students {no_of_students}")
#find average
average_students = total_height / no_of_students
print(f"average height {average_students}")