import data_processor as dp

def main():
    while True:
        task = input("""
                1.Enter 1 for sorting
                2. Enter 2 for average
                3.Enter 3 for check prime
                4.Enter q to quite
                """)
        
        if task == '1':
            user_input = input('Enter a list of numbers separated by spaces:')
            data = list(map(int, user_input.split()))
            print('Sorted list: ',dp.Sorting(data))
        elif task == '2':
            user_input = int(input('Enter a list of numbers separated by spaces:'))
            data = list(map(int, user_input.split()))
            print('Average:',dp.Average(data))

        elif task == '3':
            num = int(input('Enter the number'))
        
            print("Is Prime",dp.check_prime(num))
        elif task == 'q':
            break
        else:
            print('please give valid input')


#main()

