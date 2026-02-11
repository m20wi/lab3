#lab3 Question 5
from unittest import case

menu=(input('Choose an option:Addition,Subtraction,Multiplication,Division:'))
num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
match menu:
    case 'Addition':
        print('the total is',num1+num2)
    case 'Subtraction':
        print('the total is',num1-num2)
    case 'Multiplication':
        print('the total is',num1*num2)
    case 'Division':
        print('the total is',num1/num2)



