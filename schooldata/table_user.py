from Abel.schooldata.lecturers.lecturer_table import LecturerTable
from Abel.schooldata.students.student_table import StudentTable

# table=LecturerTable()
# result=table.create(entity_id=1, full_name="John Bosco", faculty="Business IT", no_of_courses= 2, no_of_student=10, title="Egineer")
# print(result)

table2= StudentTable()
result2=table2.create(entity_id=1000, gpa=6.5,full_names="John Bosco")
print(result2)

update=table2.update(1000,new_gpa=3.5 )
print(update)

