def can_enroll(age):
    if 10 <= age <= 20:
        return "Enrollment successful."
    else:
        return "Enrollment denied. Age not within allowed range (10–20)."

student_age = int(input("Enter student's age: "))
print(can_enroll(student_age))
