# a list of students’ ids
students = [
# Codezilla school
['1100', '1101', '1102', '1103', '1104',
'1105', '1106', '1107', '1108', '1109'],
# Al Dorra school
['2100', '2101', '2102', '2103', '2104',
'2105', '2106', '2107', '2108', '2109'],
# Mostafa Kamel school
['3100', '3101', '3102', '3103', '3104',
'3105', '3106', '3107', '3108', '3109']
]

Codezilla_school = students[0] 
Al_Dorra_school = students[1] 
Mostafa_Kamel_school = students[2]

# amessege to ask for student id
student_id = (input("Enter student id: "))
print("-"*50)

# check the school of the student
if student_id in Codezilla_school:
    print("Student is in Codezilla school")
elif student_id in Al_Dorra_school:
    print("Student is in Al Dorra school")
elif student_id in Mostafa_Kamel_school:
    print("Student is in Mostafa Kamel school")
else:
    print("sorry, student is not in our records")
