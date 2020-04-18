offset = int(input()) * 60
london = 10 * 60 + 30

if london + offset < 0:
    print("Monday")
elif london + offset > 24 * 60:
    print("Wednesday")
else:
    print("Tuesday")
