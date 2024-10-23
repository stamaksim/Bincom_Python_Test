def sum_fibonacci(n=50):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total
