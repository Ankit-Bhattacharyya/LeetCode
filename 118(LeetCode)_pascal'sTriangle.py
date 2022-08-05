class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]*i for i in range(1,numRows+1)]
        print(result)
        for i in range(2,numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                
        return result