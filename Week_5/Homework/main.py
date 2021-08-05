import math
from fractions import Fraction


class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return '{}/{}'.format(self.numarator, self.numitor)

    def __add__(self, other):
        self.den = math.gcd(self.numitor, other.numitor)

        self.den = (self.numitor * other.numitor) / self.den

        self.num = (self.numarator * (self.den / self.numitor) +
                    other.numarator * (self.den / other.numitor))

        self.gcd = math.gcd(int(self.num), int(self.den))

        return Fractie(int(self.num / self.gcd), int(self.den / self.gcd))

    def __sub__(self, other):
        self.den = math.gcd(self.numitor, other.numitor)

        self.den = (self.numitor * other.numitor) / self.den

        self.num = ((self.numarator) * (self.den / self.numitor) -
                    (other.numarator) * (self.den / other.numitor))

        self.gcd = math.gcd(int(self.num), int(self.den))

        if self.num == 0:
            return Fractie(0, 0)
        return Fractie(int(self.num / self.gcd), int(self.den / self.gcd))

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


f = Fractie(1, 4).__add__(Fractie(1, 4))

print(f.__str__())
print(Fraction(1, 4) + Fraction(1, 4))
f = Fractie(2, 1).__sub__(Fractie(19, 4).inverse())

print(f.__str__())
print(Fraction(2, 1) - Fraction(19, 4))
