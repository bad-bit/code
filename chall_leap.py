def is_leap(year):
    leap = False
    
    if year % 4 == 0 or year % 400 == 0:
    	return True
    elif year % 100 == 0:
 

    	
  	

    return leap

year = int(input())
is_leap(year)

return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)