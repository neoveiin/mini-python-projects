import os

def get_str(prompt):
    while True:
        val = input(prompt).strip()

        if not val:
            print("Error: Enter a valid string\n")
            continue
        return val


def get_int(prompt, start=None, end=None):
    while True:
        try:
            val = int(input(prompt))

            if start is not None and end is not None:
                if not (start <= val <= end):
                    print(f"Error: Value must be between '{start}' and '{end}'. Provided: '{val}'")
                    continue
            return val
        except ValueError:
            print("Error: Enter a valid integer value only\n")
            continue


def display_report(students):

    marks = [student["marks"] for student in students]

    avg_marks = round(sum(marks) / len(students),  2)

    max_marks = max(marks)
    min_marks = min(marks)

    scorers = [student["name"] for student in students if student["marks"] == max_marks]
    losers = [student["name"] for student in students if student["marks"] == min_marks]
    
    heading1 = "Analysis of Student Marks"
    print('*' * len(heading1))
    print(heading1)
    print('*' * len(heading1))

    print(f"- Average marks scored: {avg_marks}")
    

    if min_marks == max_marks:
        print(f"- All students scored same marks: {max_marks}")
    else:
        print(f"- Highest marks scored: {max_marks} by {', '.join(scorers)}")

        print(f"- Lowest marks scored: {min_marks} by {', '.join(losers)}")

    print(f"- Total number of students: {len(students)}")

    heading2 = "Detailed overview of student marks"
    print('*' * len(heading2))
    print(heading2)
    print('*' * len(heading2))

    for student in students:
        print(f"- {student['name']} : {student['marks']}")


def student_already_exists(name, students):
    return any(name.lower() == student["name"].lower() for student in students)


def student_marks_analyzer():
    
    students = []

    i = 1
    while True:
        name = get_str(f"Name of student #{i} or 'done' to exit: ")

        if name.lower() == 'done':
            print()
            break

        if student_already_exists(name, students):
            print("Error: Student with this name already exists. Try again...\n")
            continue

        marks = get_int(f"Marks of '{name}': ", 0, 100)

        students.append({"name": name, "marks": marks})

        i += 1

        print()
    
    if not students:
        print("\nNo, student info to analyse. Try again")
        return
    
    display_report(students)


if __name__ == "__main__":

    os.system('cls' if os.name == 'nt' else 'clear')

    student_marks_analyzer()