#Check if the string consists of two words each starting with a capital letter
def check_if_name(str):
    tmp = str.split()
    if (len(tmp) == 2 and tmp[0][0].isupper() and tmp[1][0].isupper()):
        return True
    return False

