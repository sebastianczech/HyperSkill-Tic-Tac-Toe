numbers = [4, 1, 0, 3, 2, 5]
# put your python code here
index = 0
for _ in numbers:
    numbers[index] = index
    index += 1
print(numbers)