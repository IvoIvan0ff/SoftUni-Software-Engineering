def grades_to_word(grade):
    grade_as_word = ''
    if 2.00 <= grade <= 2.99:
        grade_as_word = 'Fail'
    elif 3.00 <= grade <= 3.49:
        grade_as_word = 'Poor'
    elif 3.50 <= grade <= 4.49:
        grade_as_word = 'Good'
    elif 4.50 <= grade <= 5.49:
        grade_as_word = 'Very Good'
    elif 5.50 <= grade <= 6:
        grade_as_word = 'Excellent'
    return grade_as_word


grade_as_number = float(input())
print(grades_to_word(grade_as_number))
