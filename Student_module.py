class Student:
  def __init__(self,name,age,grades):
    self.name = name
    self.age = age
    self.grades = grades

  def average_grade(self):
    return sum(self.grades) / len(self.grades)
    
  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Grades: {self.grades}")