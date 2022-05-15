def shirley_minics(x, y=4):
    if type(x) == int and type(y) == int:
        if x == 1 or x == 3 or y == 1 or y == 3:
            x = True
            y = True
        elif x == 2 or x == 4 or y == 2 or y == 4:
            x = False
            y = False
        if x or y:
            return "mimic"
        else:
            return "real"
    if type(x) == str:
        if x[0] == "A":
            return "real"
        if x[0] == "C":
            return "real"
        if x[0] == "B":
            return "mimic"
x1 = input()
x2 = x1.split()

value = input()
v = value.split()
x = v[0]
print(shirley_minics(int(x2[0]), int(x2[1])))
print(shirley_minics(x,1))
print(len(v))




