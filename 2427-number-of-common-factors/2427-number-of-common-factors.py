class Solution:
    def commonFactors(self, a: int, b: int) -> int: 
        num=min(a,b)
        result=[]
        for i in range(1,num+1):
            if a%i==0 and b%i==0:
                result.append(i)
        return len(result)
    
        