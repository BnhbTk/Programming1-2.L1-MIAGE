if __name__=="__main__":
  p:int=int(input("p="))
  q:int=int(input("q="))
  div:int=p # this will be the result of the division
  rem:int=0 # this will be the remainder of the division
  while q<=rem:
    div=div+1
    rem=rem-q
  print(div,q)
