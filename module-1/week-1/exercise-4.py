def factorial(n):
    if n != 0:
        return n*factorial(n-1)
    return 1


def approx_sin(x, step):
    total = 0
    for i in range(step):
        total += ((-1)**i * x**(2*i+1))/factorial(2*i+1)
    return total


def approx_cos(x, step):
    total = 0
    for i in range(step):
        total += ((-1)**i * x**(2*i))/factorial(2*i)
    return total


def approx_sinh(x, step):
    total = 0
    for i in range(step):
        total += (x**(2*i+1))/factorial(2*i+1)
    return total


def approx_cosh(x, step):
    total = 0
    for i in range(step):
        total += (x**(2*i))/factorial(2*i)
    return total


if __name__ == "__main__":
    print("Sine of 3.14 over 10 steps:", approx_sin(3.14, 10))
    print("Cosine of 3.14 over 10 steps:", approx_cos(3.14, 10))
    print("Sinh of 3.14 over 10 steps:", approx_sinh(3.14, 10))
    print("Cosh of 3.14 over 10 steps:", approx_cosh(3.14, 10))
