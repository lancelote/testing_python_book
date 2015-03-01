class Calculate(object):

    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x), type(y)))

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass


class Store():

    def store(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2, 2)
    print(result)