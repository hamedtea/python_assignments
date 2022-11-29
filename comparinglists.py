"""
COMP.CS.100 Programming 1.
Stuart Student, hamed.talebian@tuni.fi, student id 150360360.
Solution of task 5.5.
"""
def are_all_members_same(my_list):
    """

    :param my_list: list, a list of integers
    :return: bool, true if all index values are the same
    """
    result = True
    index = 0
    while index < len(my_list) - 1:
        if my_list[index] == my_list[index + 1]:
            index += 1
        else:
            result = False
            break
    return result



