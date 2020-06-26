deposits = int(input())
year = 0
while deposits < 700000:
    deposits = deposits + int(0.071 * deposits)
    year = year + 1
print(str(year))
