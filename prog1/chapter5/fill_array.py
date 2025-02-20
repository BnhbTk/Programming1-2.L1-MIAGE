if __name__=="__main__":
    arr:list[int]=[0]*10
    # this loops fills the array with multiples of 3
    i:int
    for i in range(len(arr)):
        arr[i]=3*i
    
    # display both indices and elements
    e:int
    for i,e in enumerate(arr):
        print("Element at",i,"is",e)
