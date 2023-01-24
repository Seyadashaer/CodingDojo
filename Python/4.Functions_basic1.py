#1. Predict: 5
def a():
    return 5
print(a())
print("---------------------------------------")


#2 Predict: 10
def a():
    return 5
print(a()+a())
print("---------------------------------------")


#3 Predict: 5
def a():
    return 5
    return 10
print(a())
print("---------------------------------------")


#4 Predict: 5
def a():
    return 5
    print(10)
print(a())
print("---------------------------------------")


#5 Predict: None(If there are no return statements, then it returns None)
def a():
    print(5)
x = a()
print(x)
print("---------------------------------------")


#6 Predict: TypeError (unsupported operand type(s) for +: 'NoneType' and 'NoneType')
def a(b,c):
    print(b+c)
#print(a(1,2) + a(2,3))
print("---------------------------------------")


#7 Predict: 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
print("---------------------------------------")


#8 Predict: 100 10 
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
print("---------------------------------------")


#9 Predict: 7 14 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
print("---------------------------------------")


#10 Predict: 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))
print("---------------------------------------")


#11 Predict: 500 500 300 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
print("---------------------------------------")


#12 Predict: 500 500 300 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
print("---------------------------------------")


#13 Predict: 500 500 300 300 
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
print("---------------------------------------")


#14 Predict: 1 3 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
print("---------------------------------------")


#15 Predict: 1 3 5 10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
print("---------------------------------------")







