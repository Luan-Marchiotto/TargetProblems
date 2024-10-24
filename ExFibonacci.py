def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0

num = int(input("Informe o número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência")
else:
    print(f"O número {num} não pertence à sequência")
