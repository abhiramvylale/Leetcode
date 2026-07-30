class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []

        while matrix:

            for i in range(len(matrix[0])):
                res.append(matrix[0].pop(0))
            
            matrix = [sublist for sublist in matrix if sublist]
            
            if not matrix:
                break

            for i in range(len(matrix)):
                res.append(matrix[i].pop())
                
            matrix = [sublist for sublist in matrix if sublist]

            if not matrix:
                break

            for i in range(len(matrix[-1])):
                res.append(matrix[-1].pop())
                
            matrix = [sublist for sublist in matrix if sublist]
            
            if not matrix:
                break

            for i in range(len(matrix)-1, -1, -1):
                res.append(matrix[i].pop(0))
                
            matrix = [sublist for sublist in matrix if sublist]

            if not matrix:
                break
            
        return res

