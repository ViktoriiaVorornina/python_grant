class SetOfIntegers:
    def __init__(self, integers):
        self.integers = integers

    def sum(self):
        return sum(self.integers)

    def average(self):
        return sum(self.integers) / len(self.integers)

    def maximum(self):
        return max(self.integers)

    def minimum(self):
        return min(self.integers)


class Number:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def to_octal(self):
        return oct(self.value)

    def to_hexadecimal(self):
        return hex(self.value)

    def to_binary(self):
        return bin(self.value)
