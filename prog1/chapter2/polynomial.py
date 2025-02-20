if __name__=="__main__":
    # read the coefficients of the polynomial
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))

    # read the value of x
    x=float(input("x="))

    # compute the value of the polynomial
    res=a*x**2+b*x+c

    # now print the result
    print(a,"*x²+",b,"*x+",c,"=",res,"for x=",x)
