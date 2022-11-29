"""
COMP.CS.100 Programming 1.
Stuart Student, hamed.talebian@tuni.fi, student id 150360360.
Solution of task 2..
"""


def main():

    num_of_days = int(input('Enter the number of days: '))
    data = 0
    mean = 0
    counter = 0

    for number in range(1, num_of_days + 1):
        running_length = float(input(f'Enter day {number} running length: '))
        if running_length != 0:
            data = data + running_length
            mean = data / num_of_days
            counter = 0
        else:
            counter += 1
            if counter < 3:
                continue
            else:
                break
    print()
    if counter == 3:
        print('You had too many consecutive lazy days!')
    elif mean < 3:
        print(f"Your running mean of {mean:.2f} km was too low!")
    else:
        print(f"You were persistent runner! With a mean of {mean:.2f} km.")

if __name__ == '__main__':
    main()
