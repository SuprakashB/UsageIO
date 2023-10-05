class MyNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        elif isinstance(other, (int, float)):
            return MyNumber(self.value + other)
        else:
            raise ValueError("Unsupported operand type")

    def __radd__(self, other):
        return self.__add__(other)

if __name__ == "__main__":

    num1 = MyNumber(5)
    num2 = MyNumber(10)
    result = num1 + num2
    print("Result:", result)


    result = num1 + 20
    print("Result:", result)

    result = 15 + num2
    print("Result:", result)
