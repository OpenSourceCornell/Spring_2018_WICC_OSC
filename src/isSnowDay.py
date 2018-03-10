#given a list of numeric values for inches of snow, return a list indicating whether Cornell would have a snowday
#rule: 4 inches = snowday. nothing more. nothing less.
#ex. [0, 8, 4, 999], return [False, False, True, False]
def is_snow_day(snowfallList):
    a = []
    for x in snowfallList:
    	if x==4:
    		a.append(True)
    	else: 
    		a.append(False)
    return a
