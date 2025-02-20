def zigzag(nrows:int,ncols:int) -> list[list[str]]:
    """This function creates a matriw with nrows rows
    and ncols columns. Each element is initialized to a space (" ")
    """
    return [[" "]*ncols for _ in range(nrows)]