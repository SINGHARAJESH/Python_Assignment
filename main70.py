from Student_module import Student



def main():

    student1 = Student(name="Rajesh", age=20, grades=[88, 92, 79, 85])
    student2 = Student(name="Amit", age=22, grades=[75, 85, 80, 90])
    student3 = Student(name="Depak", age=19, grades=[95, 90, 92, 89])
    
    print("Student details for student1:")
    print(student1.display_info())
    print('Average:',student1.average_grade())

    print("\nStudent details for student2:")
    print(student2.display_info())
    print('Average:',student2.average_grade())

    print("\nStudent details for students3")
    print(student3.display_info())
    print('Average:',student3.average_grade())





main()