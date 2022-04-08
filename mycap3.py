n=int(input("Enter a number : "))
i=0
x=0
y=1
while(i<n):
    if(i <= 1):
        z=i
    else:
        z=x+y
        x=y
        y=z
    print(z)
    i=i+1
