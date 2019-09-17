import re


class Transfer(object):

    def __init__(self, number):
        self.number = number
        self.dict = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }

    def transfer(self):
        if self.number.isdigit():
            return self.a2r()
        else:
            return self.r2a()

    def r2a(self):
        string = ''.join(self.number.split())
        result = 0
        for i in range(len(string)):
            try:
                if self.dict[string[i]] < self.dict[string[i+1]]:
                    result -= self.dict[string[i]]
                else:
                    result += self.dict[string[i]]
            except IndexError:
                result += self.dict[string[i]]
        return result

    def a2r(self):
        count = int(self.number)
        result = ""
        for rome_key, arab_value in sorted(self.dict.items(), key=lambda x: x[1], reverse=True):
            while count >= arab_value:
                result += rome_key
                count -= arab_value
        return result
