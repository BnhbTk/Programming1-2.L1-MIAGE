if __name__=="__main__":
    arr=[0]*10
    # this loops fills the array with multiples of 3
    for i in range(len(arr)):
        arr[i]=3*i
    
    # display both indices and elements
    for i,e in enumerate(arr):
        print("Element at",i,"is",e)
