#second largest
arr=[10,20,30]
first=arr[0]
second=-1
for num in arr:
    if num>first:
        second=first
        first=num
    elif num>second and num<first:
       second=num
print(second)