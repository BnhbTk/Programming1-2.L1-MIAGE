import math
if __name__=="__main__":
    radius:float=float(input("What is the radius? "))
    volume:float=4/3*radius**3*math.pi
    surface:float=4*radius**2*math.pi
    print("Volume=",volume,", Surface=",surface)
