n=list(map(str,input('nhap bai hat:').split(',')))
ma=0
for i in range(len(n)):
  if len(n[ma])<len(n[i]):ma=i
  if 'yeu'in n[i] :print(n[i])
print(n[ma])