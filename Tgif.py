"""
COMP.CS.100 Programming 1.
Stuart Student, hamed.talebian@tuni.fi, student id 150360360.
Solution of task 2.8.2: a program that prints the fridays of a year
"""

def main():

    month = 0
    dates = 0
    counter = 0

    for month in range (1, 12 + 1):
        if month == 1:
            for dates in range (3, 31 +1):
                if counter % 7 == 0:
                    print(f"{dates}.{month}.", sep="")
                    counter += 1
                else:
                    counter += 1
        elif month == 2:
            for dates in range(1, 28 + 1):
                if counter % 7 == 0:
                    print(f"{dates}.{month}.", sep="")
                    counter += 1
                else:
                    counter += 1
        elif month == 3 or month == 5 or month == 7 or month == 8 \
                or month == 10 or month == 12:
            for dates in range(1, 31 + 1):
                if counter % 7 == 0:
                    print(f"{dates}.{month}.", sep="")
                    counter += 1
                else:
                    counter += 1
        else: 
            for dates in range(1, 30 + 1):
                if counter % 7 == 0:
                    print(f"{dates}.{month}.", sep="")
                    counter += 1
                else:
                    counter += 1



if __name__ == '__main__':
    main()
