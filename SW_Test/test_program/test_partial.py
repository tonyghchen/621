import functools
def add(a,b):
    return a+b
#1
rst1=add(4,2)
print("add(4,2)=",rst1)

plus3= functools.partial(add,3)
plus5= functools.partial(add,5)

#2
print("plus3(4)=",plus3(4))
print("plus3(7)=",plus3(7))
print("plus5(10)=",plus5(10))
print("functools.partial(add,6)(7)=",functools.partial(add,6)(7))  #匿名函數

def plusn(n):
    return functools.partial(add,n)          #匿名函數
print(plusn(6)(7))