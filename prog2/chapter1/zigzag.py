def create_matrix(nrows:int,ncols:int) -> list[list[str]]:
    """This function creates a matriw with nrows rows
    and ncols columns. Each element is initialized to a space (" ")
    """
    return [[" "]*ncols for _ in range(nrows)]

def display_matrix(mat:list[list[int]]):
    for row in mat:
        print(" ".join(row))
        
def str2zigzag(s:str,rows:int,cols:int) -> list[list[int]]:
    mat=create_matrix(rows,cols)
    row=0
    col=0
    up=False
    for c in s:
        mat[row][col]=c
        if up:
            row=row-1
            if row<0:
                row=1
                up=False
            else:
                col=col+1
        else:
            row+=1
            if row==rows:
                row=row-2
                col=col+1
                up=True
    return mat

if __name__=="__main__":
    mat=str2zigzag("LetshavefunwithPython",5,15)
    display_matrix(mat)
