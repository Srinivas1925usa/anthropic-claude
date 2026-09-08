def factorial(n):
    """Return n! computed iteratively."""
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    n = 10
    print(f"{n}! = {factorial(n)}")
