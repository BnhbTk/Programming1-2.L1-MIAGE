if __name__=="__main__":
    # we don't have to store all values. We only need to store the sum of marks (in s) and their number (in n)
    s:int=0
    n:int=0
    
    while True: # it is simpler to define an "infinite" loop that will be broken when the user types "end"
        mark:str=input("Give the next mark, or type end to stop data input: ")
        
        if mark=="end": # end of input, break
            break
        else: # data have been input, add it to the sum and increment the counter n
            s=s+float(mark)
            n=n+1
    
    if n==0: # no data have been introduced, no average to compute
        print("No data have been given. Unable to compute the average")
    else: # at least one data have been given, so compute the average
        print("Average=",s/n)
