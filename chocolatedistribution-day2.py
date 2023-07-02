class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        A.sort()
        mini=2**63 -1
        val=0
        for i in range(N-M+1):
            if(A[i+M-1]-A[i]< mini):
                mini=A[i+M-1]-A[i]
                
        
        return mini
