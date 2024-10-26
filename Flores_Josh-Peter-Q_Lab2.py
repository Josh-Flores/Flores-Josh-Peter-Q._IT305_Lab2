from datetime import datetime

def main():
    print("Program Started.")
    student_data = get_student_info()  # Store student data
    total_enrollment_fee = 0  # Initialize total enrollment fee

    while True:
        total_enrollment_fee += select_course()  # Add to the total enrollment fee
        another_course = input("Do you want to enroll in another course? (yes/no): ").strip().lower()
        if another_course != 'yes':
            break
    
    # Print student details and total enrollment fee at the end
    print("\n" + "_" * 60)
    print("Student Details:")
    print(f"Full Name: {student_data['full_name']}")
    print(f"Address: {student_data['address']}, {student_data['barangay']}, {student_data['city']}, {student_data['province']}")
    print(f"Birthdate: {student_data['birthdate']} | Age: {student_data['age']}")
    print(f"Total Enrollment Fee: ₱{total_enrollment_fee}")
    print("_" * 60)

def get_student_info():
    data = {}
    print("Enter Student Details:")
    data['last_name'] = input("LN: ").strip().capitalize()
    data['first_name'] = input("FN: ").strip().capitalize()
    data['mi'] = input("MI: ").strip().upper()
    data['address'] = input("Street #: ").strip()
    data['barangay'] = input("BRG: ").strip().capitalize()
    data['city'] = input("CTY: ").strip().capitalize()
    data['province'] = input("Province: ").strip().capitalize()
    
    birthdate = get_valid_birthdate()
    data['birthdate'] = birthdate  # Store the birthdate
    data['age'] = calculate_age(birthdate)
    data['full_name'] = f"{data['first_name']} {data['mi']} {data['last_name']}"  # Create full_name
    
    print(f"Student Data:\nFull Name: {data['full_name']}\nAddress: {data['address']}, {data['barangay']}, {data['city']}, {data['province']}\nBirthdate: {birthdate} | Age: {data['age']}")
    input("Press Enter to continue...")
    return data

def get_valid_birthdate():
    while True:
        birthdate = input("Birthdate (MM/DD/YYYY): ").strip()
        try:
            datetime.strptime(birthdate, "%m/%d/%Y")  # Validate the format
            return birthdate
        except ValueError:
            print("Invalid format. Use MM/DD/YYYY.")

def calculate_age(birthdate):
    birthdate_obj = datetime.strptime(birthdate, "%m/%d/%Y")
    age = datetime.now().year - birthdate_obj.year
    if (datetime.now().month, datetime.now().day) < (birthdate_obj.month, birthdate_obj.day):
        age -= 1
    return age

def select_course():
    courses = {
        "BSIT": [("Sub1", 3, 150), ("Sub2", 4, 350), ("Sub3", 4, 200), ("Sub4", 3, 200), ("Sub5", 4, 200)],
        "BSGE": [("Sub1", 3, 150), ("Sub2", 4, 350), ("Sub3", 4, 200), ("Sub4", 3, 200), ("Sub5", 4, 200)],
        "BSFT": [("Sub1", 3, 150), ("Sub2", 4, 350), ("Sub3", 4, 200), ("Sub4", 3, 200), ("Sub5", 4, 200)],
        "BSABEN": [("Sub1", 3, 150), ("Sub2", 4, 350), ("Sub3", 4, 200), ("Sub4", 3, 200), ("Sub5", 4, 200)],
    }
    
    course = choose_course(courses)
    subjects = courses[course]
    sel_subjects = choose_subjects(subjects)
    total = calculate_total(sel_subjects)
    
    print(f"Selected Subjects: {sel_subjects}\nTotal Enrollment Fee for this course: ₱{total}\n")
    return total  # Return the total for this course

def choose_course(courses):
    print("Available Courses:")
    for i, course in enumerate(courses.keys(), start=1):
        print(f"{i}. {course}")
    
    selected_course = 0
    while True:
        try:
            selected_course = int(input("Pick a course (number): "))
            if 1 <= selected_course <= len(courses):
                return list(courses.keys())[selected_course - 1]  # Return the course name
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Use a number.")

def choose_subjects(subjects):
    num_subjects = get_num_subjects(len(subjects))
    sel_subjects = []
    for i in range(num_subjects):
        subj = get_subject(subjects, sel_subjects)  # Pass selected subjects to prevent duplicates
        sel_subjects.append(subj)
    return sel_subjects

def get_num_subjects(max_subjects):
    while True:
        try:
            num = int(input(f"How many subjects to enroll in (1-{max_subjects}): "))
            if 1 <= num <= max_subjects:
                return num
            else:
                print(f"Invalid number. Use 1-{max_subjects}.")
        except ValueError:
            print("Invalid input. Use a number.")

def get_subject(subjects, sel_subjects):  # Accept sel_subjects to avoid duplicates
    for i, subject in enumerate(subjects):
        print(f"{i+1}. {subject[0]} - {subject[1]} units - ₱{subject[2]}")
    while True:
        try:
            subj_num = int(input("Pick a subject: ")) - 1
            if 0 <= subj_num < len(subjects) and subjects[subj_num] not in sel_subjects:
                return subjects[subj_num]
            else:
                print("Invalid choice or already selected.")
        except ValueError:
            print("Invalid input. Use a number.")

def calculate_total(subjects):
    return sum(sub[2] for sub in subjects)

if __name__ == "__main__":
    main()

