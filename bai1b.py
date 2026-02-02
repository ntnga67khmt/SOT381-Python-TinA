import math
a,b=eval(input('nhap lan luot 2 so a,b:'))    
if a==0:
    if b==0:print('vo so nghiem')
    else:print('vo nghiem')
else:print('nghiem cua phuong trình la:',round((-b/a),2))