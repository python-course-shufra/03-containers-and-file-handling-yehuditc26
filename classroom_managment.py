classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def found_index(name):
    for index,student in enumerate(classroom):
        if student['name']==name:
            return index
    return None         


# print(found_index('Alice'))

def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    if(email is None):
        email=f"{name.lower()}@example.com"
    new_student={'name':name, 'email':email, 'grades':[]}
    classroom.append(new_student)
    pass

#print(add_student('yehudit'))
    # def add_student(classroom, name, email=None):
    # if email is None:
    #     email = f"{name.lower()}@example.com"
    
    # new_student = {'name': name, 'email': email, 'grades': []}
    # classroom.append(new_student)
    # return "Student added successfully."

    


def delete_student(name):
    """Delete a student from the classroom"""
    for student in classroom:
        if student['name']==name:
            classroom.remove(student)
            return True
    return False
    
#print(delete_student('Alice'))

def set_email(name, email):
    """Sets the email of the student"""
    for student in classroom:
        if student['name']==name:
            student['email']=email
    pass

#set_email('Bob', 'bob.new@example.com')  
#print(set_email('Alice','udt@example.com'))

def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""

    index =found_index(name)
    # newGrade = {grade,profession}
    classroom[index]['grades'].append((profession,grade))
    pass

# def add_grade(name, profession, grade):
#     index = found_index(name)
#     classroom[index]['grades'].append((profession, grade))

# add_grade('Charlie', 'math', 95)

#add_grade('Charlie','math',95)

def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """ 
    total_grades = 0
    count = 0

    index =found_index(name)
    for grade in classroom[index]['grades']:
        if grade[0]==profession:
            total_grades+= grade[1]
            count+=1
    if(count>0):  
        average_grade = total_grades / count
        return average_grade
    return None

# def calculate_average_grade(classroom, student_name, profession):
#     total_grades = 0
#     count = 0
    
#     for student in classroom:
#         if student['name'] == student_name:
#             for grade in student['grades']:
#                 if grade[0] == profession:
#                     total_grades += grade[1]
#                     count += 1
    
#     if count == 0:
#         return f"No grades found for {student_name} in {profession}."
    
#     average_grade = total_grades / count
#     return average_grade


print(avg_grade('Alice','math'))


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""

    professions=set()

    index =found_index(name)
    for grade in classroom[index]['grades']:
        professions.add(grade[0])
    return list(professions)
    pass

#print(get_professions('Charlie'))

# def get_unique_professions(classroom, student_name):
#     unique_professions = set()
    
#     for student in classroom:
#         if student['name'] == student_name:
#             for grade in student['grades']:
#                 unique_professions.add(grade[0])
    
#     return list(unique_professions)
