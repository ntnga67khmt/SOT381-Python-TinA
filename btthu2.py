n=int(input('nhap so dau can:'))
x=int(input('nhap so:'))
tong=0
tong1=0
for i in range(1,n+1):
    tong=(tong+x)**0.5
print(tong)
for i in range(n+1):
    tong1+=((x**i)/(i+1))