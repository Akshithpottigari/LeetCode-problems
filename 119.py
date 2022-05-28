def getRow(rowIndex):
    result = []
    if rowIndex==0:
        return [1]
    else: 
        while (len(result) < (rowIndex)):
                for i in range(rowIndex+1):
                    temp=[]
                    for j in range(i+1):
                        if (j == 0 or i == j):
                            temp.append(1)
                        else:
                            temp.append(result[i-1][j]+result[i-1][j-1])
                    result.append(temp)
        return result[rowIndex]

print(getRow(1))