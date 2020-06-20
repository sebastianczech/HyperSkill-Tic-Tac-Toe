# put your python code here
str_numbers = input()
list_numbers = str_numbers.split()
x = input()
if x not in list_numbers:
    print("not found")
else:
    for i in range(len(list_numbers)):
        if x == list_numbers[i]:
            print(str(i) + " ", end="")
