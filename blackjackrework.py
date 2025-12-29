import random
card=list(map(str,input('nhap la bai ma ban muon:').split()))
sumcard=numace=0
nhacai=random.randint(20,21)
for i in card:
    if '0'<i<'9':sumcard+=int(i)
    else:
        if i=='A':sumcard=sumcard+11;numace+=1
        else:sumcard+=10
while numace!=0 and sumcard>21:
    sumcard-=10
if sumcard>=nhacai:print('ban da thang nha cai')
else:print('ban da thua nha cai')
print(sumcard)
