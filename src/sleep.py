# Most of us need to get more sleep...
# Your objective is, given a list of hours that a student
# has been awake, return the average amount of time
# that student has slept for

def sleep(awake):
    tot = 0
    for i in awake:
    	tot += i
    return(tot/len(awake))