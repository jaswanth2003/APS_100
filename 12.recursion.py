n=5
arr=[1,2,3,4,5]
# smalloutput=0
def su(n):
    if n<=0:
        return 0
    smalloutput = su(n-1);
    return smalloutput +arr[n-1]
print(su(n))