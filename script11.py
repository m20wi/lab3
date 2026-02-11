#lab3 Question 6
from unittest import case

score = int(input('enter student score:'))
if score>=60:
     print('student:passed')
else:
     print('student:failed')
if score>=90:
    gread='A'
elif score>=80:
    gread='B'
elif score>=70:
    gread='C'
elif score>=60:
    gread='D'
else:
    gread='F'
match gread:
    case 'A':
       print ('Great')
    case 'B':
        print('Very Good')
    case 'C':
        print('Good')
    case 'D':
        print('weak')
    case 'F':
        print('Fail')

