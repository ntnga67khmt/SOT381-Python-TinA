def amstrong(a):
 k=str(a)
 tong=0
 for i in k:
  tong=tong+int(i)**3
 if tong==a:return True
 else:return False
n=list(map(int,input('nhap cac phan tu').split()))
for i in range(len(n)):
 if amstrong(n[i]):print(n[i],end=' ')
print(amstrong(153))#so 153 la so amstrong
