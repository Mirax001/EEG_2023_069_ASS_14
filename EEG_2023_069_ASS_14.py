def f(x):
    return x**3 - x - 2

def f_prime(x):
    return 3*x**2 - 1

# Bisection Method
def bisection_method(a, b, epsilon=1e-6):
    steps = 0
    while abs(b - a) > epsilon:
        steps += 1
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, steps

# Newton-Raphson Method
def newton_raphson(x0, epsilon=1e-6):
    steps = 0
    x = x0
    while abs(f(x)) > epsilon:
        steps += 1
        x = x - f(x) / f_prime(x)
    return x, steps

# Comparison
root_bisect, steps_bisect = bisection_method(1, 2)
root_newton, steps_newton = newton_raphson(1.5)

print("Bisection Root:", root_bisect, "Steps:", steps_bisect)
print("Newton-Raphson Root:", root_newton, "Steps:", steps_newton)