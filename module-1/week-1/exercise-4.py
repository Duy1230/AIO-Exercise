def factorial(n):
    if n != 0:
        return n*factorial(n-1)
    return 1

def approx_sin(x, step):
    sum = 0
    for i in range(step):
        sum += ((-1)**i * x**(2*i+1))/factorial(2*i+1)
    return sum

def approx_cos(x, step):
    sum = 0
    for i in range(step):
        sum += ((-1)**i * x**(2*i))/factorial(2*i)
    return sum

def approx_sinh(x, step):
    sum = 0
    for i in range(step):
        sum +=  (x**(2*i+1))/factorial(2*i+1)
    return sum

def approx_cosh(x, step):
    sum = 0
    for i in range(step):
        sum +=  (x**(2*i))/factorial(2*i)
    return sum

if __name__ == "__main__":
    print("Sine of 3.14 over 10 steps:",approx_sin(3.14 , 10))
    print("Cosine of 3.14 over 10 steps:",approx_cos(3.14 , 10))
    print("Sinh of 3.14 over 10 steps:",approx_sinh(3.14 , 10))
    print("Cosh of 3.14 over 10 steps:",approx_cosh(3.14 , 10))
    
