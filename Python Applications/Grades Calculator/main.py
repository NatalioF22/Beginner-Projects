'''
    Write a program that reads grades on midterm(0-100), final(0-100), quizzes(0-120), and lab projects(0-130)
    and then prints the overall grade(0-100). The scores are weighted as follows:
    Midterm: 25%
    Final: 25%
    Quiz: 10%
    Projects: 40%
'''


def grades_calculator():
    # First we get the input from the user"
    # We determine the scale of the grade(e.g) if user enters 50 in midterm it equals 50 %
    # However if the user enters 50 in quiz: it equals 41.66 because it is on a scale of 120, not 100
    midterm = eval(input("Enter midterm (0-100): "))
    midterm_percentage = ((midterm / 100) * 100)
    
    final = eval(input("Enter final (0-100): "))
    final_percentage = ((final / 100) * 100)

    quiz = eval(input("Enter quiz (0-120): "))
    quiz_percentage = ((quiz / 120) * 100)

    lab = eval(input("Enter lab projects (0-130): "))
    lab_percentage = ((lab / 130) * 100)
    overal_grade = (midterm_percentage + final_percentage + quiz_percentage + lab_percentage) / 4 
    print(overal_grade)


if __name__ == "__main__":
    grades_calculator()
