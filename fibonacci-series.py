"""
COMP.CS.100 Programming 1.
Stuart Student, hamed.talebian@tuni.fi, student id 150360360.
Solution of task 2.6.3
"""


def main():
    f_counts = int(input("How many Fibonacci numbers do you want? "))

    current_fib = 1
    previous_fib = 0

    next_fib = 1
    counter = 0

    for counter in range (0, f_counts):
        print(f"{counter + 1}.", current_fib)
        next_fib = previous_fib + current_fib
        previous_fib = current_fib
        current_fib = next_fib

if __name__ == '__main__':
    main()
