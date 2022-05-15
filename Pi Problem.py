import math # import math in order to use math.pi

x = input()
y = x.split() # split the line
# Know that y has to have 2 values


first_pi = len(y[0]) # find length of first value
second_pi = len(y[1]) # find length of second value

total = abs(second_pi - first_pi) # shows total value of overlap
xx = str(math.pi) # have math val as a string
print(xx[0:total + 1]) # print out the total amount of overlap do +1 since it is not inclusive