class MyCounter:
    __secretCount=0   #私有變數
    publicCount=5     #公共變數

    def __privateCountFun(self):
        print("這是私有方法")
        self.__secretCount+=1
        self.publicCount+=1
    def publicCountFun(self):
        print("這是公共方法")
        self.__privateCountFun()

if __name__=="__main__":
    counter=MyCounter()
    counter.publicCountFun()
    counter.publicCountFun()
    print("instance publicCount=",counter.publicCount)
    print("class publicCount=",MyCounter.publicCount)
    #print(counter.__secretCount)
    #print(counter.__privateCountFun())