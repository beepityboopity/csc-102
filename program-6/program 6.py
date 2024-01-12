##########################
# Program 6
# magical flawless numbers
# ###################
# 10/18/2023
##########################

class Number:  # number class
    def __init__(self, value):  # only takes value
        self.value = value
        self.divisors = []
        # get all the divisors of the value
        for x in range(1, value):
            if (value % x) == 0:
                self.divisors.append(x)

    # getters and setters
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def divisors(self):
        return self._divisors

    @divisors.setter
    def divisors(self, divisors):
        self._divisors = divisors

    def isPerfect(self):  # checks if the divisors add up to the value
        total = 0
        for x in self.divisors:
            total += x
        if total == self.value:
            return True
        else:
            return False

    def __str__(self):  # prints number value and divisors
        return "The factors of {} are {}" .format(self.value, self.divisors)


# get number input
number = Number(int(input("Enter a number: ")))
if number.isPerfect():  # check if number is perfect
    print(number)
else:  # adds one to the number and tests its perfection until it finds a perfect one
    while not number.isPerfect():
        number = Number(number.value + 1)
    print(number)
