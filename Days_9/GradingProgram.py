student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}


def main():
    for i in student_scores:
        scores = student_scores[i]
        if scores >= 91:
            grade = "Outstading"
        elif scores >= 81:
            grade = "Exceeds Expectations"
        elif scores >= 71:
            grade = "Acceptable"
        else:
            grade = "Fail"
        student_grades[i] = grade
    print(student_grades)


if __name__ == '__main__':
    main()

