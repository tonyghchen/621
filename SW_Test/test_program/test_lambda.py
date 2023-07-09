add10=lambda a:a+10 
print(add10(5),add10(10))

def fadd10(a):
    return(a+10)

print(fadd10(5),fadd10(10))



def myfunc(n):
    return lambda a: a*n       #lambda當匿名函數返回值

mydoubler=myfunc(2)
print(type(mydoubler),mydoubler(11))

