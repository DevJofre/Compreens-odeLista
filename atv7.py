def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primos = [num for num in range(1, 21) if eh_primo(num)]

print(primos)