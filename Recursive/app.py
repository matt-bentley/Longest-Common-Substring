a = "fdlysdknv"
b = "foamysdkn"

def findSubstringRecursive(a,b,l):
    if(l == 0):
        return ""
    findString = findSubstring(a,b,l)
    if(findString == ""):
        l = l - 1
        findString = findSubstringRecursive(a,b,l)
    else:
        return findString
    return findString

def findSubstring(a,b,l):
    lenB = len(b)
    for i in range(0,lenB - l):
        findString = a[i:i + l]
        if(findString in b):
            return findString
    return ""
        
findString = findSubstringRecursive(a,b,len(a))
print(findString)