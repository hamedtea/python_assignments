"""
COMP.CS.100 Programming 1.
Stuart Student, hamed.talebian@tuni.fi, student id 150360360.
Solution of task 8.11.
"""


def main():
    filename = input("Enter the name of the score file: ")
    try:
        read_file = open(filename, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return
    line = read_file.readlines()
    dic = {}
    for i in line:
        i = i.replace("\n", "")
        try:
            (key, value) = i.split(" ")
        except ValueError:
            print("There was an erroneous line in the file:")
            print(i)
            return
        try:
            if key in dic:
                value_int = int(value)
                dic[key] += value_int
            else:
                value_int = int(value)
                dic[key] = value_int
        except ValueError:
            print("There was an erroneous score in the file:")
            print(value)
            return
    print("Contestant score:")
    for i in sorted(dic):
        print(i, dic[i])

if __name__ == '__main__':
    main()
