print("Welcome to simple calculator")

# input first number from user
number_1 = input("Input first number\n")
number_1 = float(number_1)

# input second number from user
number_2 = input("Input second number\n")
number_2 = float(number_2)

# input a function from user
ask_the_function =input('Please select the operation (+,/,*,-)\n')

if ask_the_function == '+':
    result = number_1 + number_2
    print(f'The result is: {result}')
elif ask_the_function == '/':
    result = number_1 / number_2
    print(f'The result is: {result}')
