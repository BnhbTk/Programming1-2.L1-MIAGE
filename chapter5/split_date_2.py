if __name__=="__main__":
    # This solution works in all cases (while the separator is /)
  
    # This is the date to be analyzed
    # it can also be read by input
    date:str="8/12/2024"

    # This list stores the names of the months
    months:list[str]=["jan","feb","march","apr","may","jun","jul","aug","sep","oct","nov","dec"]

    # We use here the split(...) methods that decomposes a string into parts separated by a given string. The result is a list of strings. We use unpacking here to have the three parts.
    day:str
    month:str
    year:str
    day,month,year=date.split("/")

    # convert from string to int, note that we use "".join(...) to convert a list of chars into string
    i_day:int=int(day)
    i_month:int=int(month)
    i_year:int=int(year)

    # print the result
    print(f"The date is {i_day:02d} {months[i_month-1]} {i_year}")
