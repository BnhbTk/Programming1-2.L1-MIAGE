import sys

if __name__=="__main__":
    try:
        x:float=float(input("Value of x="))
        y:float=float(input("Value of y="))
        z:float=float(input("Value of z="))
        if x<=0 or y<=0 or z<=0:
            raise ValueError("")
    except:
        print("Wrong data")
        sys.exit(2)
    if x+y>z and x+z>y and y+z>x: # test whether the triangle is possible
        # ok it is triangle
        print("It is a triangle")
        if x==y==z:# test if it equilateral
            print("This is an equilateral triangle")
        else:
            if x==y or x==z or y==z:
                print("This is an isosceles triangle")
            if x**2+y**2==z**2 or x**2+z**2==y**2 or y**2+z**2==x**2:
                print("This is a right triangle")
        s=(x+y+z)/2
        area=(s*(s-x)*(s-y)*(s-z))**0.5
        print("Area=",area)
    else:
        print("This is not a triangle")
    
