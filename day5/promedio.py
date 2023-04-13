student_heights =  input("Input a list of student heights: ").split()
counter = 0
sum = 0
for student in student_heights:
    sum += int(student)
    counter += 1
 
print(counter)   
print(round(sum / counter))