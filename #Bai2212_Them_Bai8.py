k=int(input('nhap(k>2)'))
m=[1,1]
tong=0
while k>len(m):
 m+=[m[-1]+m[-2]]
print(m)