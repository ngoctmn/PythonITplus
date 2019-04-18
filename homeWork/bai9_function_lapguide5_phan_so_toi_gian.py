numerator = 10
denominator = 12


def reducing_fractions(numerator, denominator):
    greatest_common_divisor = 0
    for i in range (1, min(numerator, denominator) + 1):
        if numerator % i == denominator % i == 0:
            greatest_common_divisor = i
    numerator /= greatest_common_divisor
    denominator /= greatest_common_divisor
    return int(numerator), int(denominator)


print(reducing_fractions(10, 12))
