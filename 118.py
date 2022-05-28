def generate(numRows):
        result = []
        while (len(result) < numRows):
            for i in range(numRows):
                temp=[]
                for j in range(i+1):
                    if (j == 0 or i == j):
                        temp.append(1)
                    else:
                        temp.append(result[i-1][j]+result[i-1][j-1])
                result.append(temp)
        return result

print(generate(5))