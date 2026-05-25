about_python = '''Python is a versatile, high-level programming language known for its simple and readable syntax that resembles everyday English. 
Created by Guido van Rossum and first released in 1991, it has become one of the world's most popular languages due to its beginner-friendly nature and vast ecosystem of libraries'''
print(len(about_python))
print(f"First Character : {about_python[0]} \nLast Character : {about_python[-1]}")
print(f"First 50 characters : {about_python[:51]}")
python_replaced = about_python.replace("Python","PYTHON")
print(f"Replaced with PYTHON : {python_replaced}")
python_low = about_python.lower()
print(f"In lower case : {python_low}")
print(f"Without white space : {about_python.strip()}")
splitted = about_python.split()
print(f"In splitted : {splitted}")
print("course" in about_python)
print("The course description is {0} characters long and has {1} words.".format(len(about_python),len(splitted)))
