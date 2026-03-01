def fibonacci(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.

    Args:
        n: A non-negative integer representing the position in the Fibonacci sequence

    Returns:
        The nth Fibonacci number

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Example usage
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
