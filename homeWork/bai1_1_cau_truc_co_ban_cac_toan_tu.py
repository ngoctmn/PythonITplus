a = 16
b = 3
c = 5

# Arithmetic Operators
sum = a + b
print(sum)

minus = a - b
print(minus)

multiple = a * b
print(multiple)

divide = a / 3
print(divide)

exponential = b ** 2
print(exponential)

naturalPart = a // 3
print(naturalPart)

# Comparison Operators
print(a > b)
print(a >= c)
print(b < a)
print(b <= c)
print(b == c)
print(b != c)

# Assignment Operators
a += b
print(a)
b -= 1
print(b)
c *= 2
print(c)
a /= c
print(a)
a %= c
print(a)
a //= 2
print(a)
b **= 2
print(b)

# Logical Operators
checkAB = (a == b) or (a > b)
print(checkAB)

checkBC = (b < c) and (b != c)
print(checkBC)

checkAC = not (a > c)
print(checkAC)

# Bitwise Operators
d = 3
e = 5
f = 8
bitAnd = d & e
print(bitAnd)

bitOr = e | f
print(bitOr)

bitXor = d ^ e
print(bitXor)

bitNot = ~ f
print(bitNot)

moveBitLeft = e << 3
print(moveBitLeft)
moveBitRight = f >> 2
print(moveBitRight)