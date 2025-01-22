from ast import literal_eval

from multipledispatch import dispatch


class Calculator:

    def __init__(self, first_number, second_number):
        self._first_number = first_number
        self._second_number = second_number
        self._result = None

    def set_first_number(self, value):
        self._first_number = value

    def set_second_number(self, value):
        self._second_number = value

    def set_result(self, value):
        self._result = value

    def get_first_number(self):
        return self._first_number

    def get_second_number(self):
        return self._second_number

    def get_result(self):
        return self._result

    def make_calculation(self):
        return

    def ask_for_first_number(self):
        while True:
            self.set_first_number((input(f"Please provide first number: ")))
            if check_if_null(self.get_first_number()):
                continue
            else:
                self.set_first_number(literal_eval(self.get_first_number()))
                break

    def ask_for_second_number(self):
        while True:
            self.set_second_number(input(f"Please provide second number: "))
            if check_if_null(self.get_second_number()):
                continue
            else:
                self.set_second_number(literal_eval(self.get_second_number()))
                break


class Add(Calculator):

    @dispatch(int, int)
    def make_calculation(self, a, b):
        self.set_result((a + b))
        return self.get_result()

    @dispatch(float, int)
    def make_calculation(self, a, b):
        self.set_result(a + b)
        return self.get_result()

    @dispatch(int, float)
    def make_calculation(self, a, b):
        self.set_result(a + b)
        return self.get_result()

    @dispatch(float, float)
    def make_calculation(self, a, b):
        self.set_result((a + b))
        return self.get_result()


class Subtract(Calculator):

    @dispatch(int, int)
    def make_calculation(self, a, b):
        self.set_result((a - b))
        return self.get_result()

    @dispatch(float, int)
    def make_calculation(self, a, b):
        self.set_result(a - b)
        return self.get_result()

    @dispatch(int, float)
    def make_calculation(self, a, b):
        self.set_result(a - b)
        return self.get_result()

    @dispatch(float, float)
    def make_calculation(self, a, b):
        self.set_result(a - b)
        return self.get_result()


class Divide(Calculator):

    @dispatch(int, int)
    def make_calculation(self, a, b):
        if self.get_second_number() == 0:
            self.set_result("You can't divide by 0!")
        else:
            self.set_result(a / b)
        return self.get_result()

    @dispatch(int, float)
    def make_calculation(self, a, b):
        if self.get_second_number() == 0:
            self.set_result("You can't divide by 0!")
        else:
            self.set_result(a / b)
        return self.get_result()

    @dispatch(float, int)
    def make_calculation(self, a, b):
        if self.get_second_number() == 0:
            self.set_result("You can't divide by 0!")
        else:
            self.set_result(a / b)
        return self.get_result()

    @dispatch(float, float)
    def make_calculation(self, a, b):
        if self.get_second_number() == 0:
            self.set_result("You can't divide by 0!")
        else:
            self.set_result(a / b)
        return self.get_result()


class Multiply(Calculator):

    @dispatch(int, int)
    def make_calculation(self, a, b):
        self.set_result((a * b))
        return self.get_result()

    @dispatch(float, int)
    def make_calculation(self, a, b):
        self.set_result(a * b)
        return self.get_result()

    @dispatch(int, float)
    def make_calculation(self, a, b):
        self.set_result(a * b)
        return self.get_result()

    @dispatch(float, float)
    def make_calculation(self, a, b):
        self.set_result(a * b)
        return self.get_result()


def check_if_null(number):
    if number == "":
        return True
