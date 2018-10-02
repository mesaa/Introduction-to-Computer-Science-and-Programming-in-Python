#finger excercise 1.1
number1 = int(input('Enter 1st number:'))
number2 = int(input('Enter 2nd number:'))
number3 = int(input('Enter 3rd number:'))

if number1%2 or number2%2 or number3%2 > 0:
	# if number1<number2 and number2<number3:
	# 	print(number1, number2, number3)
	if (number1<number2)==False and (number2<number3)==False and (number1<number3)==False:
		print(number3, number2, number1)
	else: 
		print('Undefined.')
# else: 
# 	print('No odd numbers inputs.')
