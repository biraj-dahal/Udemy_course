print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''
)
operations = {
        "*" : multiply,
        "+" : add,
        "-" : subtract,
        "/" : divide,
    }

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def divide(num1, num2):
    return num1/num2
def multiply(num1, num2):
    return num1*num2


direction = 'n'
while True:
    if direction == 'n':
        f_n = float(input("What's the first number?: "))
    elif direction == 'y':
        f_n = answer

    print("+\n-\n*\n/")
    
    sym = input("Pick on operation: ")
    s_n = float(input("What's the next number?: "))
    answer = operations[sym](f_n,s_n)
    print(f"{f_n} {sym} {s_n} = {answer}")
    direction = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")


