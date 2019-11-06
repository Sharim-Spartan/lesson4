class batches():
    def __init__(self,studentID,module, student, start_date):
        self.studentID=studentID
        self.module=module
        self.student=student
        self.start_date=start_date

    def list_batch(students):
        list_students = []
        list_students.append(students.studentID)
        list_students.append(students.module)
        list_students.append(students.student)
        list_students.append(students.start_date)
        return (list_students)



students_1=batches(1, 'data stream', 'Sharim Babar', '30/02/2019')
students_2=batches(2, 'data stream', 'Mafzuhur Rahman','30/02/2019')
student_3=batches(3, 'data stream', 'Mohammad Ibrahim', '30/02/2019')
print(batches.list_batch(students_1))
print(batches.list_batch(students_2))
print(batches.list_batch(student_3))

print (batches.list_batch(student_3))

# def list_batch(students):
#     list_students = []
#     list_students.append(students.batches)
#     list_students.append(students.module)
#     list_students.append(students.student)
#     list_students.append(students.start_date)
#     return (list_students)





