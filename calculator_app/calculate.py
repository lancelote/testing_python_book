class Calculate(object):

    @staticmethod
    def add(x, y):
        """
        Takes two integers and adds them together to produce the result.

        >>> Calculate.add(1, 1)
        2
        >>> Calculate.add(125, 25)
        150
        >>> Calculate.add(1.0, 1.0)
        Traceback (most recent call last):
            ...
        TypeError: Invalid type: <class 'float'> and <class 'float'>
        """
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    @staticmethod
    def subtract(x, y):
        """
        Takes two integers and subtracts second from first to produce the result.

        >>> Calculate.subtract(2, 1)
        1
        >>> Calculate.subtract(10, 11)
        -1
        """
        if type(x) == int and type(y) == int:
            return x - y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    @staticmethod
    def multiply(x, y):
        """
        Multiplies two integers to produce the result.

        >>> Calculate.multiply(2, 2)
        4
        >>> Calculate.multiply(3, 4)
        12
        """
        if type(x) == int and type(y) == int:
            return x*y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    @staticmethod
    def divide(x, y):
        """
        Divides th first integer by the second to produce result.

        >>> Calculate.divide(6, 2)
        3
        >>> Calculate.divide(10, 2)
        5
        """
        if y == 0:
            raise ZeroDivisionError("Division by zero!")
        elif type(x) == int and type(y) == int:
            return int(x/y)
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


class Store():

    def store(self):
        pass

    def delete(self):
        pass

# Doctest direct start

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'c': Calculate()})