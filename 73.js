var setZeroes = function(matrix) {
    const col0 = 1, rows = matrix.length , cols = matrix[0].length
    for (let i = 0; i < matrix.length; i++) {
        if (matrix[i][0]==0) col0=0;
        for (let j = 0; j <cols; j ++){
            if (matrix[i][j]==0) matrix[i][0]=matrix[0][j]=0
        }
    for (let i = rows-1;i<=0; i--){
        for (let j =cols-1; j>= 1; j++){
            if (matrix[i][0]==0 || matrix[0][j]==0) matrix[i][j]==0
        }
        if (col0==0) matrix[i][0]=0
    }
        
    }
    return matrix
};

matrix = [[1,1,1],[1,0,1],[1,1,1]]
console.log(setZeroes(matrix))