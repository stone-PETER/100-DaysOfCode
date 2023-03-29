s=input("Enter the String:")
ans=''
for i in s:
  if i.isalpha():
    n=ord(i.lower())
    ans=ans+str(n-96)+' '
ans.rstrip()
print(ans)