#YUSUF ONARAN
# GPA CALCULATOR

current_credit = 0.00
current_gpa = 0.00
semester_lesson = []
semester_credit = []
semester_grades = []

def SemesterGrades(semester_lesson,semester_credit,semester_grades):
    while True:
        class_input = input("Enter the name of your lesson: ")
        while class_input:
            semester_lesson.append(class_input)
            break
        credit_input = input("Enter the number of credit for the lesson: ")
        while credit_input:
            if credit_input.isdigit() == False:
                print("Invalid Entry. Please enter a digit.")
                credit_input = input("Enter the number of credit for the lesson: ")
            else:
                semester_credit.append(credit_input)
                break
        grade_input = input("Enter your expected letter grade for the lesson,\nfor exp. (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, or F): ")
        grade_input = grade_input.upper()
        while grade_input:
            if grade_input.upper() == "A+":
                semester_grades.append("4")
                break
            elif grade_input.upper() == "A":
                semester_grades.append("4")
                break
            elif grade_input.upper() == "A-":
                semester_grades.append("3.7")
                break
            elif grade_input.upper() == "B+":
                semester_grades.append("3.3")
                break
            elif grade_input.upper() == "B":
                semester_grades.append("3")
                break
            elif grade_input.upper() == "B-":
                semester_grades.append("2.7")
                break
            elif grade_input.upper() == "C+":
                semester_grades.append("2.4")
                break
            elif grade_input.upper() == "C":
                semester_grades.append("2.2")
                break
            elif grade_input.upper() == "C-":
                semester_grades.append("2")
                break
            elif grade_input.upper() == "D+":
                semester_grades.append("1.7")
                break
            elif grade_input.upper() == "D":
                semester_grades.append("1.5")
                break
            elif grade_input.upper() == "F":
                semester_grades.append("0")
                break
            else:
                print("Invalid Entry")
                grade_input = input("Enter your expected letter grade for the lesson,\nfor exp. (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, or F): ")
                grade_input = grade_input.upper()
        add_classes = input("Would you like to add another class? ")
        if add_classes.lower().startswith("n") == True:
            break
        else:
            pass

print("Welcome to the GPA Calculator program!")
initial_option = input("Would you like to enter your current GPA and credit hour totals? (Yes/No) ")


while initial_option:
    if initial_option.isalpha() == False:
        print("Invalid entry. Plase enter Yes or No!")
        initial_option = input("Would you like to enter your current GPA and credit hour totals? (Yes/No) ")
    elif initial_option.lower().startswith('y'):
        current_credit_entry = input("Enter your total earned credit: ")
        while current_credit_entry:
            if current_credit_entry.isnumeric() == True:
                current_credit = float(current_credit_entry)
                break
            else:
               print("Invalid entry. Plase enter an integer.")
               current_credit_entry = input("Enter your total earned credit: ")
        current_gpa_entry = input("Enter your total earned GPA: ")
        while current_gpa_entry:
            if float(current_gpa_entry) > 4:
                print("Invalid entry. GPA must be an digit and lower than 4!")
                current_gpa_entry = input("Enter your total earned GPA: ")
            elif current_gpa_entry.isalpha() == False:
                current_gpa = float(current_gpa_entry)
                break
            else:
               print("Invalid entry. GPA must be an digit and lower than 4!")
               current_gpa_entry = input("Enter your total earned GPA: ")
        break
    else:
        break

print("Current hours:", current_credit)
print("Current GPA:", current_gpa)
print()
print("Enter your current lessons, credit and expected grades.")

SemesterGrades(semester_lesson, semester_credit, semester_grades)
total_credit = current_credit
for num in semester_credit:
    total_credit += float(num)
total_gpa = current_credit * current_gpa
for num in range(0, len(semester_credit)):
    total_gpa += float(semester_credit[num]) * float(semester_grades[num])
total_gpa = total_gpa / total_credit
now_gpa = float("{:.2f}".format(total_gpa))

print()
print("Total credit:", total_credit)
print("Total Expected GPA:", now_gpa)
print("Thank you for using the GPA Calculator!")