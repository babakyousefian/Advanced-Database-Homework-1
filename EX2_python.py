import time
from decimal import Decimal, getcontext

getcontext().prec = 1000

def Factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("\n\n An ERROR occurred...!!!")

    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1 , 1):
            fact *= i

    return fact


def compute_expression(n):
    result = Decimal(0)
    sign = 1

    for i in range(0, n+1, 1):
        factorial_part = ((2 * i) + 3)

        divisor = Decimal(i + 2)
        constant = Decimal(9 - (2 * i))

        if divisor + constant == 0:
            print(f"Skipping division by zero at term {i}")
            continue

        term = (Decimal(Factorial(factorial_part))) / (divisor + constant)

        result += sign * term

        sign *= -1

    return result


n = input("\n\nPlease enter your number to calculate it: ")
n = int(float(n))
result = compute_expression(n)
time.sleep(1)
print(f"Result for the first {n} terms: {result}")
