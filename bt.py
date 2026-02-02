a=float(input('nhap diem mon toan:'))
b=float(input('nhap diem mon ly:'))
c=float(input('nhap diem mon hoa:'))
if a+b+c>=15 and a>4 and b>4 and c>4:
    if a>5 and b>5 and c>5:print('hoc deu cac mon')
    else:print('hoc chua deu')
else:print('thi hong ')