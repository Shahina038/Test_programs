import string
def freq(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i] + 1

    return dic


def panagram(s):
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True        
    
def Average(lst):
    sum=0
    if len(lst) == 0:
        return None
    for i in lst:
        sum= sum+i
    return sum/len(lst) 
     