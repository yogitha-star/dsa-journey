#sorted array
arr=[1,2,10,5]
for i in range(len(arr)-1):
    if arr[i]<=arr[i+1]:
        print("sorted")
    else:
     print("not sorted") 


