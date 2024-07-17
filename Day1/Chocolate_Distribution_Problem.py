class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        if(N==0 or M==0):
            return 0
        A.sort()
        if(len(A) < M):
            return -1
        min_diffrence = A[1] - A[0]
        
        for i in range(len(A) - M + 1):
            min_diffrence = min(min_diffrence, A[i + 1] - A[i])
        return min_diffrence