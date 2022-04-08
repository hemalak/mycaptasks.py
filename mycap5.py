def word_count(x):
    a={}
    for i in x:
        if i not in a:
            a[i]=1
        else:
            a[i]=a[i]+1
    print(sorted(a.items(),key=lambda ab:(ab[1],ab[0]),reverse=True))
s=input("Please enter a string : ")
word_count(s)


