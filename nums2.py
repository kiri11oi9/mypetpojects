import math

class Fraction:
    def __init__(self, raw_fraction: str):
        fraction_parts = Fraction.parse_fraction(raw_fraction)
        self.numerator = fraction_parts['numerator'] + fraction_parts['whole'] * fraction_parts['denominator']
        if fraction_parts['sign'] == -1:
            self.numerator *= -1
        self.denominator = fraction_parts['denominator']
        self.simplificator()

    def simplificator(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def parse_fraction(raw_fraction: str):
        sign = 1
        if raw_fraction.startswith('-'):
            sign = -1
            raw_fraction = raw_fraction[1:]
        pair = raw_fraction.split()
        whole = 0
        if len(pair) == 2:
            whole = int(pair[0])
            raw_fraction = pair[-1]
        pair = raw_fraction.split('/')
        numerator = int(pair[0])
        denominator = int(pair[1])
        return {'sign': sign, 'whole': whole, 'numerator': numerator, 'denominator': denominator}


    def __str__(self):
        whole = abs(self.numerator) // self.denominator
        numerator = self.numerator
        denominator = self.denominator
        if whole:
            numerator = abs(self.numerator) % self.denominator
        sign = ''
        if self.numerator < 0:
            sign = '-'
        return f"{sign}{whole or ''} {numerator}/{denominator}"

f1 = Fraction('-21/15')
print(f1.numerator)
print(f1)
print(f1.numerator)

