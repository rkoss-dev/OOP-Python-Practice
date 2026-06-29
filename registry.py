class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.grades = []

    def add_grade(self, grade: int):
        """Adds a grade to the grades list."""
        self.grades.append(grade)

    def average_grade(self) -> float:
        """Returns the average of all grades."""
        if not self.grades:
            return 0.0  # Prevents division by zero if no grades exist
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Prints the student's name, email, and grades."""
        print(f"Student Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade()}")

    def grades_tuple(self) -> tuple:
        """Returns the grades list converted into a tuple."""
        return tuple(self.grades)

def get_student_by_email(email: str):
    """Retrieves a student safely, returning None (or a message) if not found."""
    return student_dict.get(email, "Student not found in the system.")

# --- Create 3 students ---
student1 = Student("Megan Harry", "mh@example.com")
student2 = Student("Robert Harry", "rh@example.com")
student3 = Student("Andrew Harry", "ah@example.com")

# --- Give those 3 students grades ---
student1.add_grade(76)
student1.add_grade(82)
student1.add_grade(74)
student1.add_grade(75)
student1.add_grade(84)

student2.add_grade(64)
student2.add_grade(58)
student2.add_grade(46)
student2.add_grade(61)
student2.add_grade(24)

student3.add_grade(84)
student3.add_grade(92)
student3.add_grade(88)
student3.add_grade(93)
student3.add_grade(98)

# Display student info and print a break before the next part
student1.display_info()
print()
student2.display_info()
print()
student3.display_info()
print("---------------------------------")

# Create dictionary that ties email to student info
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Use a set to find unique grades (it ignores duplicates)
unique_grades = set()
for student in student_dict.values():
    unique_grades.update(student.grades)
print(unique_grades)

# --- Fetch the grades as a tuple ---
grades_tup = student1.grades_tuple()
print(f"Original Tuple: {grades_tup}")
print(f"Type: {type(grades_tup)}\n")

# --- Attempting to modify the tuple ---
print("Attempting to change the first grade in the tuple to 100...")

try:
    # This will trigger a TypeError because tuples are immutable
    grades_tup[0] = 100 
    
except TypeError as error:
    print(f"Exception Caught! Error message: '{error}'")
    print("Conclusion: You cannot modify a tuple once it is created!")

# Verify the original list in the object is untouched
print(f"\nStudent's actual grades list remains: {student1.grades}")

# --- Show initial state for comparison ---
print("--- Initial State ---")
for student in student_dict.values():
    print(f"{student.name}: {student.grades}")

# --- Remove each student's last grade ---
print("\n--- 1. Popping the Last Grade ---")
for student in student_dict.values():
    # Checking to make sure list isn't empty
    if student.grades: 
        popped_grade = student.grades.pop()
        print(f"Removed {popped_grade} from {student.name}'s list.")

# --- Print first and last grades ---
print("\n--- 2. First and Last Grades ---")
for student in student_dict.values():
    if student.grades:
        first = student.grades[0]
        last = student.grades[-1]
        print(f"{student.name} -> First Grade: {first} | Last Grade: {last}")

# --- Print total number of grades ---
print("\n--- 3. Total Number of Grades ---")
for student in student_dict.values():
    count = len(student.grades)
    print(f"{student.name} currently has {count} grades recorded.")