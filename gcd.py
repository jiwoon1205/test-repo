def gcd1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
def gcd2(a, b):
    while a != 0 and b != 0:  
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b
def gcd3(a, b):
    if a == 0 or b == 0:
        return a+b
    return gcd3(b, a%b)

A, B, C = gcd1(3323, 12), gcd2(3323, 12), gcd3(3323, 12)
print(f"{A}, {B}, {C}")
print(3323%23)


