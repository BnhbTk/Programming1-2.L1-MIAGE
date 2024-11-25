if __name__=="__main__":
    arr1:list[int]=[1,2,3,4,5]
    arr2:list[int]=[1,2,3,6,5]

    # let's use a flag to know whether the elements are the same
    find:bool=False
    i:int
    for i in range(len(arr1)):
        if arr1[i]!=arr2[i]:
            print("Difference at position",i)
            find=True
            break
    # if all the elements are the same, find equals false
    if not find:
        print("These lists are the same")
