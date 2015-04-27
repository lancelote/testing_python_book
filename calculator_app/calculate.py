"""
Calculator implementation
"""


class Calculate(object):
    """
    Calculator object
    """

    @staticmethod
    def add(number_1, number_2):
        """
        Takes two integers and adds them together to produce the result.

        @type number_1: int
        @type number_2: int
        @return: sum of two numbers

        >>> Calculate.add(1, 1)
        2
        >>> Calculate.add(125, 25)
        150
        >>> Calculate.add(1.0, 1.0)
        Traceback (most recent call last):
            ...
        TypeError: Invalid type: <class 'float'> and <class 'float'>
        """
        if isinstance(number_1, int) and isinstance(number_2, int):
            return number_1 + number_2
        else:
            raise TypeError("Invalid type: {} and {}".format(type(number_1), type(number_2)))

    @staticmethod
    def subtract(number_1, number_2):
        """
        Takes two integers and subtracts second from first to produce the result.

        @type number_1: int
        @type number_2: int
        @return: difference between two numbers

        >>> Calculate.subtract(2, 1)
        1
        >>> Calculate.subtract(10, 11)
        -1
        """
        if isinstance(number_1, int) and isinstance(number_2, int):
            return number_1 - number_2
        else:
            raise TypeError("Invalid type: {} and {}".format(type(number_1), type(number_2)))

    @staticmethod
    def multiply(number_1, number_2):
        """
        Multiplies two integers to produce the result.

        @type number_1: int
        @type number_2: int
        @return: product of the two numbers multiplication

        >>> Calculate.multiply(2, 2)
        4
        >>> Calculate.multiply(3, 4)
        12
        """
        if isinstance(number_1, int) and isinstance(number_2, int):
            return number_1*number_2
        else:
            raise TypeError("Invalid type: {} and {}".format(type(number_1), type(number_2)))

    @staticmethod
    def divide(number_1, number_2):
        """
        Divides th first integer by the second to produce result.

        @type number_1: int
        @type number_2: int
        @return: product of the two numbers division

        >>> Calculate.divide(6, 2)
        3
        >>> Calculate.divide(10, 2)
        5
        """
        if number_2 == 0:
            raise ZeroDivisionError("Division by zero!")
        if isinstance(number_1, int) and isinstance(number_2, int):
            return int(number_1/number_2)
        else:
            raise TypeError("Invalid type: {} and {}".format(type(number_1), type(number_2)))

# Doctest direct start

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'c': Calculate()})
