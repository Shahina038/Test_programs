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
    
def average(lst):
    if not  lst:
        return None
    acc = 0
    for i in lst:
        acc = acc +i   # acc: accumulator
    return acc/len(lst) 
     