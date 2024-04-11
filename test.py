# вводные данные
number = int(input())

# продолжите решение здесь
first_digit = 0
while number > 0:
    last_digit = number % 10
    first_digit = number
    number //= 10

print(first_digit)