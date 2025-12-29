n=int(input('nhap so:'))
def tong(n):
 tu=mau=0
 for i in range(1,n+1):
   tu+=i
 for i in range(2,2*n+1,2):
  mau+=i
 return( tu/mau)
print(tong(n))