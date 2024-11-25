if __name__=="__main__":
    # the array to be reversed
    arr=[1,3,6,10,15,21]

    # In this solution, we will use the same array to compute the reverse. We will have to browse half of the array an 'swap' it with the other half

    i=0
    j=len(arr)-1 # the index of the last element
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        # Don't forget to update indices, otherwise the loop won't stop
        i+=1 # next element in the first half
        j-=1 # previous element in second half
    
    print(arr)
