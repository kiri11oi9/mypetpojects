import math

def pasre_fraction(raw_fraction: str):
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
    return {'sign' : sign, 'whole' : whole, 'numerator' : numerator, 'denominator' : denominator}

def simplificator(fraction):
    fraction_parts = pasre_fraction(fraction)
    if fraction_parts['numerator'] > fraction_parts['denominator']:
        whole = fraction_parts['numerator'] // fraction_parts['denominator']
        fraction_parts['whole'] += whole
        fraction_parts['numerator'] = fraction_parts['numerator'] % fraction_parts['denominator']
    gcd = math.gcd(fraction_parts['numerator'],fraction_parts['denominator'])

    fraction_parts['numerator'] //=gcd
    fraction_parts['denominator'] //=gcd
    sign = ''
    if fraction_parts['sign'] == -1:
        sign = '-'
    return f"{sign}{fraction_parts['whole'] or ''} {fraction_parts['numerator']} {fraction_parts['denominator']}"
print(simplificator('3 12/15'))
print(simplificator(' -5 20/6'))
print(simplificator('3/7'))
print(simplificator('-6/4'))

