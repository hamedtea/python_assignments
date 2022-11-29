"""
COMP.CS.100 Programming 1.
Stuart Student, hamed.talebian@tuni.fi, student id 150360360.
Solution of task 6.10.
"""
def read_message():
    """
    input data function + error checking
    :return: list, list of input values
    """
    msg = []
    while True:
        data = input('')
        msg.append(data)
        if not data:
            break

    msg.remove('')
    return msg

def encrypt(j):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    k = j.lower()
    if k not in regular_chars:
        return k
    if k != j:
        index = regular_chars.index(k)
        output = encrypted_chars[index]
        return output.upper()
    else:
        index = regular_chars.index(j)
        output = encrypted_chars[index]
        return output


def row_encryption(msg):
    """
    function for Rot-13 row encryption
    :param string: str, input string
    :return: str, an encrypted string
    """
    string = str(msg)
    output_string = ""
    for j in string:
        output = encrypt(j)
        output_string += output
    return output_string
def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    print("ROT13:")
    for i in range(0, len(msg)):
        output_string = row_encryption(msg[i])
        print(output_string)

if __name__ == "__main__":
    main()