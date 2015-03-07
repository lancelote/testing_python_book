class Calculate(object):

    @staticmethod
    def add(x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    @staticmethod
    def subtract(x, y):
        if type(x) == int and type(y) == int:
            return x - y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    @staticmethod
    def multiply(x, y):
        if type(x) == int and type(y) == int:
            return x*y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero!")
        elif type(x) == int and type(y) == int:
            return x/y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))


class Store():

    def store(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':  # pragma: no cover
    calc = Calculate()
    result = calc.add(2, 2)
    print(result)