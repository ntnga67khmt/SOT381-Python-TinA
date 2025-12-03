def ucln(a,b):
    while a!=b:
        if a>b:a=a-b
        else:b=b-a
    return a
a,b=eval(input('nhap so:'))
print(int((a*b)/ucln(a,b)))