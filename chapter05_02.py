# chapter 05-02
# 파이썬 사용자 입력
# input 사용법
# 기본 타입은 무조건 str 이다.

# ex1
# name = input('Enter Your Name : ')
# grade = input('Enter Your Grade : ')
# company = input('Enter Your Company Name : ')

# print(name, grade, company)

# ex2
# number = input('Enter Number : ')
# name = input('Enter Name : ')

# print('type of number', type(number))
# print('type of name', type(name))

# ex3
# first_number = int(input('Enter number1 : '))
# second_number = int(input('Enter number2 : '))

# total = first_number + second_number
# print("first_number + second_number = ", total)

# ex4
# float_number = float(input("Enter a float number : "))

# print('input float : ', float_number)
# print('input type : ', type(float_number))

# ex5
print('FirstName - {0}, LastName - {1}'.format(
    input('Enter first name : '), input('Enter second name : ')))
