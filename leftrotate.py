#left rotate
arr = [1, 2, 3, 4, 5]

temp = arr[0]          # Save the first element

for i in range(len(arr)-1):
    arr[i] = arr[i+1]  # Shift every element left

arr[len(arr)-1] = temp # Put the first element at the end

print(arr)
