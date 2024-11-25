if __name__=="__main__":
    # This solution assumes that the date is well formed. It won't work if the date 
    # is "8/12/2024". For this case, please see the other version
  
    # This is the date to be analyzed
    # it can also be read by input
    date="08/12/2024"

    # This list stores the names of the months
    months=["jan","feb","march","apr","may","jun","jul","aug","sep","oct","nov","dec"]

    # initialize the lists to spaces
    day=[' ']*2
    month=[' ']*2
    year=[' ']*4

    # extract the characters
    day[0],day[1]=date[0],date[1]
    month[0],month[1]=date[3],date[4]
    year[0],year[1],year[2],year[3]=date[6],date[7],date[8],date[9]

    # convert from string to int, note that we use "".join(...) to convert a list of chars into string
    i_day=int("".join(day))
    i_month=int("".join(month))
    i_year=int("".join(year))

    # print the result
    print(f"The date is {i_day:02d} {months[i_month-1]} {i_year}")

