def equation(X, equation_string):
    return eval(equation_string)

def bisection_method(a, b, tolerance, equation_string):
    if equation(a, equation_string) * equation(b, equation_string) >= 0:
        print("Bisection method fails.")
        return None

    while (b - a) >= tolerance:
        c = (a + b) / 2
        if equation(c, equation_string) == 0.0:
            return c
        if equation(c, equation_string) * equation(a, equation_string) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Example usage:
equation_string = input("Enter the equation (use Python syntax, e.g., X**2 - 2*X - 1): ")
a = float(input("Enter lower bound of the interval: "))
b = float(input("Enter upper bound of the interval: "))
tolerance = float(input("Enter tolerance: "))

root = bisection_method(a, b, tolerance, equation_string)
if root is not None:
    print("The real root of the equation is approximately:", root)
