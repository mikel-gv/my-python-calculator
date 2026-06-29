# Define the calculator function.
def calc(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        if num2 == 0:
            return 'Error: Cannot divide by zero.'
        return num1 / num2
    elif oper == '**':
        return num1 ** num2
    elif oper == '%':
        if num2 == 0:
            return 'Error: Cannot perform modulo by zero.'
        return num1 % num2
    elif oper == '//':
        if num2 == 0:
            return 'Error: Cannot perform floor division by zero.'
        else: 
            return num1 // num2
    else: 
        return 'Error: Invalid operator. Please choose from the list.'

# Loop the function.
first_enter = True 
while True:
    if first_enter:
        print('--- Welcome to the calculator ---')
        first_enter = False
    else:
        print('--- Next operation ---')
    
    # Get the data input from the user.
    num1_input = input('Enter first number (or "Exit" to quit): ')
    if num1_input.capitalize() == 'Exit':
        print('Quitting...')
        break
    elif num1_input.strip() == '':
        print('Input cannot be empty.')
        continue
    # Handle user input errors for non-numeric values.
    try: 
        num1 = float(num1_input)
        oper = (input('Choose an operator (+, -, *, /, **, %, //): '))
        num2 = float(input('Enter second number: ')) 

    # Send the data to the function.
        result = calc(num1, oper, num2)

    # Show the result to the user.
        if isinstance(result, (int, float)):
            print(f'Result: {result:g}')
        else:
            print(result)
    except ValueError:
        print('Invalid input: please enter a valid number.')
        continue