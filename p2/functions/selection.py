def select(ind:int,*arr:tuple[any,...]) -> any :
    if ind>=0 and ind<len(arr):
        return arr[ind]
    else:
        raise ValueError("There no such element")


def read_values() -> list[any]:
    res=[]
    while True:
        s=input("Next element (end to quit)")
        if s=="end":
            return res
        else:
            res.append(s)

def get_values(elements:tuple[any]) -> None:
    while True:
        ind=input("Give me an index: ")
        if ind=="end":
            break
        else:
            try:
                print(f"Element at position {ind} is {select(int(ind),*elements)}\n\n")
            except Exception as e:
                print(f"There was an error: {e}\n\n")

if __name__=="__main__":
    values=read_values()
    get_values(values)
