import math_operations as mo

def main():
    num1 = int(input('enter the first number: '))
    num2 = int(input('enter the second number: '))
    task = input('Enter what you want to do: ')

    if task == '+':
        print(mo.add(num1,num2))
    elif task == '-':
        print(mo.subtract(num1,num2))
    elif task == '*':
        print(mo.multiply(num1,num2))
    elif task == '/':
        try:
            print(mo.divide(num1,num2))
        except ValueError as e:
            print(e)
    else:
        print('invalid operator')
main()



        


