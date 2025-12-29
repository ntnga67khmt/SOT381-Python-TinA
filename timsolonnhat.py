a=list(map(int,input('nhap cac so:').split()))
def mx(a):
 ma=0
 for i in range(len(a)):
  if a[ma]<a[i]:ma=i
 return a[ma]
def mn(a):
 mi=0
 for i in range(len(a)):
  if a[mi]>a[i]:mi=i
 return a[mi]
print('so lon nhat',mx(a),'so nho nhat la',mn(a))

