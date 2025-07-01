a = [3, 4, 11, 55, 6, 4]
maximum = a[0] 
smaximum=maximum
for i in range(len(a)):
    if a[i] > maximum:
        smaximum=maximum
        maximum = a[i]
print(smaximum)
