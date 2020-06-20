# put your python code here
marks = input()
list_marks = marks.split()
print(str(round(list_marks.count("A") / len(list_marks), 2)))
