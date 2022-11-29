"""
COMP.CS.100 Programming 1.
Stuart Student, hamed.talebian@tuni.fi, student id 150360360.
Solution of task 5.5.2
"""
def performance_input():
    """

    :return: list, performance list of cube solving in second level
    """
    performance_list = []
    for i in range(0, 5):
        values = float(input(f"Enter the time for performance {i + 1}: "))
        performance_list.append(values)
    return performance_list

def average_operation(performance_list):
    """

    :param performance_list: list, list of time inputs
    :return: float, the mean of values
    """
    # index of min and max, then deleting the value
    result = True
    index = 0
    while index < len(performance_list) - 1:
        if performance_list[index] == performance_list[index + 1]:
            index += 1
            del(performance_list[index + 1])
            return performance_list[0]
        else:
            index_min = performance_list.index(min(performance_list))
            index_max = performance_list.index(max(performance_list))
            performance_list[index_max] = 0
            performance_list[index_min] = 0
    # averaging values in the list
            sum_list = 0
            for j in performance_list:
                sum_list += j
            return sum_list / (len(performance_list) - 2)

def main():
    performance_list = performance_input()
    mean = average_operation(performance_list)
    print(f"The official competition score is {round(mean, 2)} seconds.")
if __name__ == '__main__':
    main()
