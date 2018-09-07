# Introduction-to-Computer-Science-and-Programming-in-Python
6.0001 Introduction to Computer Science and Programming in Python
Ana Bell, Eric Grimson, and John Guttag. 6.0001 Introduction to Computer Science and Programming in Python. Fall 2016. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA.

number1 = int(input('Enter 1st number:'))
number2 = int(input('Enter 2nd number:'))
number3 = int(input('Enter 3rd number:'))

if number1%2 or number2%2 or number3%2 > 0:
	if number1<number2 and number2<number3:
		print(number1, number2, number3)
	else:
		print('numbers not sequential test 1 finished')

else: 
	print('No odd numbers inputs.')
