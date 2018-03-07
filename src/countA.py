# count the number of a's
def count_a(str):
    numNonAs = str.replace("a", "")
    return len(str) - len(numNonAs)
    
