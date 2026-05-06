def countdown(n):
    if n==0:
        return "done"
    print(n)
    return countdown(n-1)
print(countdown(5))
