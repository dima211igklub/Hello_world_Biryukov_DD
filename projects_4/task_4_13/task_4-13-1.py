a=[12,6,74,35]

minimum=min(a)
print("Наименьшее число:",minimum)

#или можно запариться =)

if a[0]<a[1]:
    b=a[0]
else:
    b=a[1]
if a[2]<a[3]:
    c=a[2]
else:
    c=a[3]
if b<c:
    print("То же самое, но сложнее:",b)
else:
    print("То же самое, но сложнее:", c)
