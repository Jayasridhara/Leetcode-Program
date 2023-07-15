class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)-1
        n=len(matrix[0])-1
        for i in range(m+1):
            if(target<=matrix[i][n]):
                for k in range(n+1):
                    if target==matrix[i][k]:
                        return 1
        return 0