# Longest common string = kdng

a = "glfkdngdf"
b = "kcmdkdngfmbvfl" 

def findLongestCommonSubstring(a,b):
    findString = ""
    maxLength = 0
    iMax,jMax = 0,0
    w,h = len(b),len(a)
    matrix = [[0 for x in range(w)] for y in range(h)]
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            match = a[i] == b[j]
            if(match):
                if(i == 0 or j == 0):
                    matrix[i][j] = 1
                else:
                    stringLen = matrix[i - 1][j - 1] + 1
                    if(stringLen > maxLength):
                        maxLength = stringLen
                        iMax,jMax = i,j
                    matrix[i][j] = stringLen
    if(maxLength > 0):      
        for i in range(1,maxLength + 1):
            findString = findString + a[iMax - maxLength + i]
    return findString
 
 
findString = findLongestCommonSubstring(a,b)
print(findString)

