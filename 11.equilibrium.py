#Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
def equilibriumPoint(self,a, n):
        # Your code here
        st=sum(a)
        lst=0
        if (n==1):
            return 1
        else:
            for i in range(n):
                lst+=a[i]
                if lst-a[i]==st-lst:
                    return i+1
                  
                   
        return -1