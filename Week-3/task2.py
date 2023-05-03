def NewFile():
    s=input("Enter name for file:")
    file=open(s, 'w')
    file.close()

def copy():
    s=input("Enter the Name of file to be copied:")
    n=input("Enter the Name of destination:")
    ch=input("Overwrite file??(y/n):")
    while True:
        try:
            with open(s, 'r') as con:
                data=con.read()
        except FileNotFoundError:
            print("Oops! Content file not found.")
            break
        if ch=='y':
            with open(n, 'w') as file:
                file.write(data)
        else:
            with open(n, 'a') as file:
                file.write(data)
        print("Copied")
        break
def display():
    s=input("Enter name for file:")
    try:
        with open(s, 'r') as con:
            data=con.read()
            print(data)
    except FileNotFoundError:
        print("Oops! File not found.")
i='n'
while(i=='n'):
    ch=int(input('''MENU
1. NEW FILE
2. COPY
3. DISPLAY
Choose operation with corresponding number:'''))
    if ch==1:
        NewFile()
    elif ch==2:
        copy()
    elif ch==3:
        display()
    else:
        print("Invalid Option!!")
    i=input("Do you wish to exit(y/n):")
