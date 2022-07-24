class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                
        return False