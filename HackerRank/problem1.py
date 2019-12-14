n = int(input("Enter no. of records: "))
student_marks = {}
for _ in range(n):
    name, *line = input("Enter student record: ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
print(student_marks)
name = input ('Enter name to calculate average score: ')
l = len(scores)
sum = 0
avg = 0
if name in student_marks:
    for i in range (0, l):
        sum += scores[i]
    print("sum: ", sum)
    avg = sum/l
    print("avg: ", avg)
