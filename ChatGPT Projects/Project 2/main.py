import Students as s
import os
import time
from datetime import date

os.system('cls')
def student_exists(name, roll):
    for student in s.students:
            if student.name == name and student.roll == roll:
                return True
    return False

while True:
    print('''
    Enter the task to perform: 
          1. Add Student
          2. View All Students
          3. Search Student
          4. Delete Student
          5. Update Student
          6. Exit
    ''')

#Choice 1
    try:
        user_choice = int(input(">>>"))
        if user_choice == 1:
            name = input("Name: ")
            grade = input("Grade: ")
            roll = input("Roll No.: ")
            age = input("Age: ")

            if student_exists(name, roll):
                print(f"Student '{name}' Already Exists!")
                continue
            else:
                name = s.StudentData(name, grade, roll, age)
                s.students.append(name)
                print("Student Added!")
        
    #Choice 2
        elif user_choice == 2:
            for student in s.students:
                print(f'''
                        Name: {student.name}
                        Grade: {student.grade}
                        Roll: {student.roll}
                        Age: {student.age}
                        ''')
            print(f"Total number of students: {len(s.students)}")
            user_input = input("Do you wish to print it in a txt file?(y/n) ")
            if user_input == "Y" or "y":
                current_date = date.today()

                current_time = time.localtime()
                hr = current_time.tm_hour
                minute = current_time.tm_min
                seconds = current_time.tm_sec

                
                file_name = "Student List-"+ str(current_date)+ "-" + str(hr)+ "-" + str(minute)+ "-" + str(seconds) + ".txt"
                with open(file_name, "w") as f:
                    for student in s.students:
                        f.write(f"Name: {student.name}\nGrade: {student.grade}\nRoll: {student.roll}\nAge: {student.age}\n--------------------------------------------------------------\n")
                    f.write(f"Total number of students: {len(s.students)}")    
                    f.close()
                        
            user_input = input("Press enter to continue")

    #Choice 3
        elif user_choice == 3:
            roll = input("Roll No.: ")
            for student in s.students:
                if roll == student.roll:
                    print(f'''
                            Name: {student.name}
                            Grade: {student.grade}
                            Roll: {student.roll}
                            Age: {student.age}
                        ''')
                    break
            else:
                print(f"No student found with roll no. {roll}")
                continue

    #Choice 4
        elif user_choice == 4:
            user_input = input("Do you have roll no. of student?(y/n) ")
            remove_students = []
            if user_input == "Y" or "y":
                roll = input("Roll No. of student to be deleted: ")
                for student in s.students:
                    if roll == student.roll:
                        remove_students.append(student.name)
                    
                    if len(remove_students) > 1:
                        print(f"{len(remove_students)} are found with same roll number")
                        print(*remove_students)
                        name = input("Enter name of student to remove: ")
                        for student in s.students:
                            if name == student.name:
                                s.students.remove(student)
                                print(f"{student.name} has been removed from the list")
                                continue
            elif user_input == "N" or "n":
                name = input("Name of the student to be deleted: ")
                for student in s.students:
                    if name.lower() == student.name.lower():
                        s.students.remove(student)
                        print(f"{student.name} with roll number {student.roll} have been removed.")
            else:
                continue

        
        elif user_choice == 6:
            print("Exiting the simulation....")
            exit()
    except Exception as e:
            print(e)
            print("Invalid Choice, Please try again!!")
            continue