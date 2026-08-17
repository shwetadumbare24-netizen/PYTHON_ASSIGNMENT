'''1. Create a Student Management System using Class and Object in Python. 
What to Do
1. Create a class named Student.  
2. Create a constructor __init__() to initialize:  o Student name  o Roll number  o Age  o Marks of 3 subjects 
3. Create a display_details() method to display all student information.  
4. Create a calculate_total() method to calculate the total marks. 
5. Create a calculate_percentage() method to calculate the percentage.  
6. Create a check_result() method:  o Student passes if marks in every subject are 35 or above.  o Otherwise, display FAIL.  
7. Create an update_marks() method to update the marks of a selected subject.  '''

class Student():
    def __init__(self,student_name,Roll_No,Age,Marks):
        self.student_name = student_name
        self.Roll_No = Roll_No
        self.Age = Age
        self.Marks = Marks

    def display_details(self):
            print("\n Student Name:",self.student_name)
            print("Student Roll No:",self.Roll_No)
            print("Student Age:",self.Age)
            print("Student Marks:",self.Marks)
    
    def  calculate_total(self):
        total = sum(self.Marks)
        print("Total Marks:",total)

    def  calculate_percentage(self):
        total = sum(self.Marks)
        percentage = total/3
        print("Total Percentage:",percentage)

    def check_result(self):
        total = sum(self.Marks)
        percentage = total/3
        if percentage >= 35:
            print("Student Pass")
        else:
            print("Student Fail")

    def update_marks(self, subject, new_marks):
        if subject == 1:
            self.Marks[0] = new_marks
        elif subject == 2:
            self.Marks[1] = new_marks
        elif subject == 3:
            self.Marks[2] = new_marks
        else:
            print("Invalid Subject Number")
        return

    print("Marks Updated Successfully")

Student1 = Student("Shwetali", 1 , 22 , [95, 85, 90]) 
while True:
    print("\n ------ Student Management System----")
    print("1. Display Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Check Result")
    print("5. Update Marks")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            Student1.display_details()

        case 2:
            Student1.calculate_total()

        case 3:
            Student1.calculate_percentage()

        case 4:
            Student1.check_result()

        case 5:
            subject = int(input("Enter subject number (1-3): "))
            new_marks = int(input("Enter New Marks: "))

            Student1.update_marks(subject,new_marks)

        case 6:
            print("Thank You!")
            break
        case _:
            print("Invalid Choice")



