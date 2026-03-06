import csv
def sum_average(grades):
    return sum(map(float,grades)) / len(grades)
    
with open('students.txt', 'r',encoding='utf-8') as file:
    txt = csv.reader(file)

    students = {}
    for row in txt:
        if not row:
            continue

        name, *grades = row[0].split(':')
        grades = grades[0].strip().split(',')
        average = round(sum_average(grades), 2)
        students[name.strip()] = average

best_student = max(students.items(), key=lambda x: x[1])

with open('result.txt','w',encoding = 'utf-8') as new_file:
    writer = csv.writer(new_file)
    
    for student,average in students.items():
        if average > 4.0: 
            writer.writerow([student,f'Средний балл:{average:.2f}'] )
    else:
        print("Нет студентов с оценками.")
    
    
print(f"Студент с наивысшим средним баллом: {
