

x = 1
def test():
    x = 2
test()
print(x)# 1 or 2


x = 1
def test():
    global x
    x = 2
test()
print(x)# 1 or 2


x = [1]
def test():
    x = [2]
test()
print(x)# 1 or 2


x = [1]
def test():
    global x
    x = [2]
test()
print(x)# 1 or 2


x = [1]
def test():
    x[0] = 2
test()
print(x)# 1 or 2