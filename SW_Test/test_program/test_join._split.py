#2
print("\n#2字串連接")
sep="分隔符號"    #分隔符號
seq=('1','2','34','567')   #連接的字符順序
s=sep.join(seq)
print("len=",len(s),"s=",s) 

#7
print("\n#7分割字串")
s1=s.split(sep)
print("type(s1)=",type(s1),"s1=",s1)