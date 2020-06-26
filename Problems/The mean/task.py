numbers = []
while True:
    n = input()
    if n != '.':
        numbers.append(int(n))
    else:
        break
print(str(sum(numbers) / len(numbers)))
