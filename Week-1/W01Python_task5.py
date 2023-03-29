def sqSum(a):
    ans=0
    for i in a:
        ans+=i**2
    return ans


l=eval(input())
print(sqSum(l))