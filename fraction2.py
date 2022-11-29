"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def complement(self):
        comp_numinator = -1 * self.__numerator
        return Fraction(comp_numinator, self.__denominator)

    def reciprocal(self):
        reciprocal_numerator = self.__denominator
        reciprocal_denominator = self.__numerator
        return Fraction(reciprocal_numerator, reciprocal_denominator)

    def multiply(self, frac2):
        numerator = self.__numerator * frac2.__numerator
        denominator = self.__denominator * frac2.__denominator
        return Fraction(numerator, denominator)

    def divide(self, frac2):
        numerator = self.__numerator * frac2.__denominator
        denominator = self.__denominator * frac2.__numerator
        return Fraction(numerator, denominator)

    def add(self, frac2):
        denominator = self.__denominator * frac2.__denominator
        numerator = self.__numerator * (denominator // self.__denominator) + frac2.__numerator * (denominator // frac2.__denominator)
        return Fraction(numerator, denominator)

    def deduct(self, frac2):
        denominator = self.__denominator * frac2.__denominator
        numerator = self.__numerator * (denominator // self.__denominator) - frac2.__numerator * (denominator // frac2.__denominator)
        return Fraction(numerator, denominator)

    def simplify(self):
        a = greatest_common_divisor(self.__numerator, self.__denominator)
        numerator = self.__numerator // a
        denominator = self.__denominator // a
        return Fraction(numerator, denominator)

    def __lt__(self, frac2):
        a = self.__numerator / self.__denominator
        b = frac2.__numerator / frac2.__denominator
        return a < b
    def __gt__(self, frac2):
        a = self.__numerator / self.__denominator
        b = frac2.__numerator / frac2.__denominator
        return a > b

    def __str__(self):
        return self.return_string()

def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def input_data():
    """
    A function to get data from input command
    :return: a list of input data
    """
    data = []
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")
    while True:
        d = str(input())
        data.append(d)
        if d =="":
            data.remove("")
            break
    return data

def operation(data):
    """

    :param data: list, a data list of input data
    :return: list, data list of Fraction objects
    """
    fraction_list = []
    for i in data:
        a = i.split("/")
        a[0] = int(a[0])
        a[1] =int(a[1])
        c = Fraction(a[0], a[1])
        fraction_list.append(c)
    return fraction_list

def print_out(fraction):
    """

    :param fraction: list, a fraction list of inputs
    :return: None
    """
    print("The given fractions in their simplified form:")
    for i in fraction:
        print(f"{i.return_string()} = {i.simplify().return_string()}")
def main():
    data = input_data()
    fraction = operation(data)
    print_out(fraction)
if __name__ == "__main__":
     main()