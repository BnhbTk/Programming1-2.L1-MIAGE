if __name__=="__main__":
    # define VAT constant
    VAT:float=0.196
    
    # read the name of the product and its price
    product_name:str=input("Give the product name:")
    product_price:float=float(input("What is the price?"))

    # compute the original price of the product
    original_price:float=product_price/(1+VAT)

    # just print the price
    print("The original price of",product_name,"is",original_price)
