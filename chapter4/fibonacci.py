if __name__=="__main__":
    n:int=int(input("n="))
    res:int=1
    old=1
    i:int=2
    while i<=n:
        res,old=res+old,res
        i=i+1
    print(res)
