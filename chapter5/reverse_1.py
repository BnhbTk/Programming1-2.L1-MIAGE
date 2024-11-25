if __name__=="__main__":
    # the array to be reversed
    arr=[1,3,6,10,15,21]

    # Here, we're using another list to result
    res=[0]*len(arr)

    # in Python, -1 is used to access the last element, -2 the one before, and so on
    for i in range(len(arr)):
        res[i]=arr[-i-1]
    
    print(res)
