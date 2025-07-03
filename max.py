a = [3, 4, 11, 55, 6, 4]
first = second = a[0] 
for i in range(len(a)):
    if a[i] > first:
        second = first
        first = a[i]
    elsif(a[i]>second and a[i]<first):
    second
print(second)
