n=input("Enter the numbers:")
even="Even:"
odd="Odd:"
prime="Prime:"
with open("InputFile.txt",'w') as In:
    In.write(n)
l=list(map(int,n.strip().split()))
j=2
for i in l:
    if i%2==0:
        even+=' '+str(i)
    else:
        odd+=' '+str(i)
    for j in range(2,(i//j)+1):
        if i%j==0:
            break
    else:
        prime+=' '+str(i)
outl=even+"\t"+odd+"\t"+prime
with open("OutputFile.txt", 'w') as Out:
    Out.write(outl)
with open("InputFile.txt",'r') as In:
    data=In.read()
    print("Input File:")
    print(data)
with open("OutputFile.txt", 'r') as Out:
    datao=Out.read()
    print("Output File:")
    print(datao)