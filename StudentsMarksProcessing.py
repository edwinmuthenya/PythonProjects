from datetime import datetime
import re


class Student:
    def __init__(self, name, registration_number, degree_program, school_years):
        self.name = name
        self.registration_number = registration_number
        self.degree_program = degree_program
        # Initialize transcripts using provided school years
        self.transcripts = {year: {'Semester 1': [], 'Semester 2': []} for year in school_years}

    def add_course(self, year, semester, course_code, course_description, marks):
        while True:
                if  self.validate_course_code(course_code):
                    break
                else:
                    raise ValueError(
                    f"Invalid course code: {course_code}. It must be alphanumeric and exactly 6 characters long.")
        grade = self.calculate_grade(marks)
        self.transcripts[year][semester].append({
            'course_code': course_code,
            'course_description': course_description,
            'marks': marks,
            'grade': grade
        })

    @staticmethod
    def validate_course_code(course_code):

        return bool(re.match(r'^[A-Za-z0-9]{6}$', course_code))



    @staticmethod
    def calculate_grade(marks):
        if marks >= 70:
            return 'A'
        elif marks >= 60:
            return 'B'
        elif marks >= 50:
            return 'C'
        elif marks >= 40:
            return 'D'
        else:
            return 'E'

    def calculate_mean_score(self):
        total_marks = 0
        total_courses = 0

        for year in self.transcripts.keys():  # Iterate over actual years
            for semester in ['Semester 1', 'Semester 2']:
                for course in self.transcripts[year][semester]:
                    total_marks += course['marks']
                    total_courses += 1

        return total_marks / total_courses if total_courses > 0 else 0

    def classify_degree(self):
        mean_score = self.calculate_mean_score()

        if mean_score >= 70:
            return "First Class Honours"
        elif mean_score >= 60:
            return "Second Upper Division"
        elif mean_score >= 50:
            return "Second Lower Division"
        elif mean_score >= 40:
            return "Pass"
        else:
            return "Fail"

    def print_transcripts(self):
        for year in self.transcripts.keys():  # Iterate over actual years
            print(f"\n--- Transcript for Year {year} ---")
            print(f"Student Name: {self.name}")
            print(f"Registration Number: {self.registration_number}")
            print(f"Degree Program: {self.degree_program}")
            for semester in ['Semester 1', 'Semester 2']:
                print(f"\n{semester}:")
                courses = self.transcripts[year][semester]
                if not courses:
                    print("No courses taken.")
                    continue
                for course in courses:
                    print(f"Course Code: {course['course_code']}, "
                          f"Description: {course['course_description']}, "
                          f"Marks: {course['marks']}, "
                          f"Grade: {course['grade']}")

    def print_certificate(self):
        mean_score = self.calculate_mean_score()
        classification = self.classify_degree()

        current_year = datetime.now().year

        print("\n--- Degree Certificate ---")
        print(f"University Name: Your University Name")
        print(f"Student Name: {self.name}")
        print(f"Degree Program: {self.degree_program}")
        print(f"Classification: {classification}")
        print(f"Mean Score: {mean_score:.2f}")
        print(f"Year of Completion: {current_year}")


def main():
    # Accept student details including school years
    name = input("Enter student name: ")
    registration_number = input("Enter registration number: ")
    degree_program = input("Enter degree program: ")

    # Input the years the student was in school (e.g., [2020, 2021, 2022, 2023])
    school_years_input = input("Enter the school years as comma-separated values (e.g., 2020,2021): ")
    school_years = [int(year.strip()) for year in school_years_input.split(',')]

    student = Student(name, registration_number, degree_program, school_years)

    # Input courses for each specified year
    for year in school_years:
        for semester in ['Semester 1', 'Semester 2']:
            print(f"\nEntering courses for Year {year}, {semester}:")
            for _ in range(5):  # Five units per semester
                course_code = input("Enter course code (e.g., SMA3103): ")
                course_description = input("Enter course description (e.g., Calculus 1): ")

                while True:
                    try:
                        marks = int(input("Enter the marks obtained (0-100): "))
                        if 0 <= marks <= 100:
                            break
                        else:
                            print("Marks must be between 0 and 100. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")

                student.add_course(year, semester, course_code, course_description, marks)

    # Print transcripts and certificate
    student.print_transcripts()
    student.print_certificate()


if __name__ == "__main__":
    main()
