import math
if __name__=="__main__":
    n1:float=float(input("n1="))
    n2:float=float(input("n2="))
    n3:float=float(input("n3="))
    n4:float=float(input("n4="))
    avg:float=(n1+n2+n3+n4)/4
    std:float=((n1-avg)**2+(n2-avg)**2+(n3-avg)**2+(n4-avg)**2)/4
    std=std**0.5
    print("AVG=",avg,"STD=",std)
