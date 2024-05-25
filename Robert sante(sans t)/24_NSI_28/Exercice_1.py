#  correction : 
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
        

# 1
print(fibonacci(1))

# 1
print(fibonacci(2))

# 75025
print(fibonacci(25))

