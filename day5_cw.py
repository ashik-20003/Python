python_students = {"Georgekutty","Geetha","Prabhakar"}
data_students = {"Georgekutty","Anumol","Varun"}
python_students.add("Thomas")
data_students.pop()
print("Student in both course : ",python_students & data_students)
print("Students who are only in Python : ",python_students-data_students)
print("Combined List : ", python_students | data_students)