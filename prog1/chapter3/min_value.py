if __name__=="__main__":
    x=int(input("Give the value of x="))
    y=int(input("Give the value of y="))
    z=int(input("Give the value of z="))
    if x<y:
        if x<z:
            min_value=x
        else:
            min_value=z
    elif y>z:
            min_value=z
    else:
        min_value=y
    print("min(",x,",",y,",",z,")=",min_value)
