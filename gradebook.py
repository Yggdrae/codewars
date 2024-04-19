#Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
#Numerical Score	Letter Grade
#90 <= score <= 100	'A'
#80 <= score < 90	'B'
#70 <= score < 80	'C'
#60 <= score < 70	'D'
#0 <= score < 60	'F'

def get_grade(s1, s2, s3):
    med = (s1+s2+s3)/3
    return 'A' if med>=90 else 'B' if med>=80 else 'C' if med>=70 else 'D' if med>=60 else 'F'

print(get_grade(95, 90, 93))
print(get_grade(70, 70, 100))
print(get_grade(70, 70, 70))
print(get_grade(65, 70, 59))
print(get_grade(44, 55, 52))