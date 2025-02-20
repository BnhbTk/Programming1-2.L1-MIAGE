if __name__=="__main__":
    # the outer loop is used to print rows
    row:int
    for row in range(8):
        # the inner loop is used to print all the boxes in one row
        col:int
        for col in range(8):
            # here we used a condition expression. The parameter end="" means that print insert no char after printing
            # [ ] or [#]. By default, this parameters is \n (try to remove end="" to see the impact).
            print("[ ]" if col%2==row%2 else "[#]",end="")
        # print without any parameters creates a new line
        print()
