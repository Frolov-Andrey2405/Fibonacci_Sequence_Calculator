import sys


class FibonacciCalculator:
    def __init__(self):
        print('''
Fibonacci Sequence Calculator

The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
        ''')

    def run(self):
        while True:
            self.calculate_fibonacci()

    def calculate_fibonacci(self):
        nth = self.get_nth_fibonacci_number()

        if nth == 1:
            print('0')
            print('\nThe #1 Fibonacci number is 0.')
            return
        elif nth == 2:
            print('0, 1')
            print('\nThe #2 Fibonacci number is 1.')
            return

        self.display_warning(nth)

        second_to_last_number = 0
        last_number = 1
        fib_numbers_calculated = 2
        print('0, 1, ', end='')

        while True:
            next_number = second_to_last_number + last_number
            fib_numbers_calculated += 1

            print(next_number, end='')

            if fib_numbers_calculated == nth:
                print()
                print(
                    f'\nThe #{fib_numbers_calculated} Fibonacci number is {next_number}.')
                break

            print(', ', end='')

            second_to_last_number, last_number = last_number, next_number

    def get_nth_fibonacci_number(self):
        while True:
            response = input(
                '\nEnter the Nth Fibonacci number you wish to calculate (such as 5, 50, 1000, 9999), or QUIT to quit:\n> ').upper()

            if response == 'QUIT':
                print('Thanks for playing!')
                sys.exit()

            if response.isdecimal() and int(response) != 0:
                return int(response)

            print('Please enter a number greater than 0, or QUIT.')

    def display_warning(self, nth):
        if nth >= 10000:
            print('WARNING: This will take a while to display on the')
            print('screen. If you want to quit this program before it is')
            print('done, press Ctrl-C.')
            input('Press Enter to begin...')


if __name__ == '__main__':
    calculator = FibonacciCalculator()
    calculator.run()
