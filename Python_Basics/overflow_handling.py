'''def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    try:
        for i in range(1, n + 1):
            result *= i
    except OverflowError:
        raise OverflowError("Factorial calculation resulted in overflow")
    return result

# Example usage of custom factorial function
# try:
print(factorial(100000))
# except OverflowError as e:
    # print("Overflow Error:", e)'''

def create_large_list():
    large_list = []
    for _ in range(10**8):  # Limiting the loop iterations
        large_list.append('data')
    return large_list
create_large_list()