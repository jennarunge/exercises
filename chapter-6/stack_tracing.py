#STACK TRACING CAUSE WHY NOT?!
def a(x):
    return b(x)
def b(x):
    try:
        return c(x-1)
    except:
        raise AssertionError("Oops, something broke")
def c(x):
    return d(x)
def d(x):
    if x ==0:
        raise AssertionError("Zero is going to cause an error")
    return 4/x

print(a(1))