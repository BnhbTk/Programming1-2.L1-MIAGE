if __name__=="__main__":
    # We check if arr1 occurs in arr2 and at which position
    arr1:list[int]=[1,5,4]
    arr2:list[int]=[4,1,5,1,5,4]
    
    # Since we don't know the position, initialize it to -1
    position:int=-1

    # loop until the length of arr2 - length of arr1
    i:int
    for i in range(len(arr2)-len(arr1)+1):
        # if the first element is the same as the current position in arr2
        if arr1[0]==arr2[i]:
            find_diff:bool=False
            # test if arr1 is the same as the next len(arr1) elements of arr2
            j:int
            for j in range(1,len(arr1)):
                if arr1[j]!=arr2[i+j]:
                    find_diff=True
                    break
            # if no difference, we found a match
            if not find_diff:
                position=i
                break
    
    # if position==-1 then no match has been found
    if position>=0:
        print(f"Occurrence found at position {position}")
    else:
        print("No occurrence")
