w=float(input('nhap chieu rong hcn:'))
h=float(input('nhap chieu dai hcn:'))
while w<=0 or h>=100:
    w=float(input('nhap lai chieu rong hcn:'))
    h=float(input('nhap lai chieu dai hcn:'))
print(f"cvchu nhat la{(w+h)*2}")
print(f"chu vi hinh chu nhat la{ w*h}")