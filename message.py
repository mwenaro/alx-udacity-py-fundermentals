#getting names

names = input('Enter names seperated by commas: ')
names = list(names.split(','))

assignments = input('Enter assignment counts seperated by commas: ')
assignments = list(assignments.split(','))

grades = input('Enter grades seperated by commas: ')
grades = list(grades.split(','))
print(names)

n = 0
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

n = 0
for name in names:
    left = int(assignments[n])
    points = int(grades[n]) + 2 * left
   
    print(message.format(name, left, grades[n], points))
    n +=1
