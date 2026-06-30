#remove duplicates from sorted array
arr = [1,1,2,2,3,3,4]
new_arr=[]
new_arr.append(arr[0])
for i in range(1,len(arr)):
    if arr[i]!=arr[i-1]:
        new_arr.append(arr[i])
print(new_arr)
