class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        output = []

        def BackTracking(open_count,closing_count):
            if len(output) == 2*n:
                res.append(''.join(output))
                return 

            if open_count < n :
                output.append('(')
                BackTracking(open_count + 1 , closing_count)
                output.pop()
            
            if open_count > closing_count:
                output.append(')')
                BackTracking(open_count, closing_count + 1)
                output.pop()
                
        BackTracking(0,0)  
        return res