students={'Theo': 10, "bobby":18}
students['Asher']=17

print(students['bobby'])
print(students.values())

other_students= {"Mo":4, "Raymond":19}

combined_students = {**other_students, **students}
print(combined_students)