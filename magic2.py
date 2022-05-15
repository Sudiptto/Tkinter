x = input()
count = 0
x1 = x.split()
del x1[0]
count = 0
for i in x1:
    if i == "1":
        count += 1

if x[0] == "1":
    if count < 2:
        print(0)
    elif count == 2 or count == 3:
        print(1)
    elif count > 3:
        print(0)
else:
    if count == 3:
        print(1)
    else:
        print(0)