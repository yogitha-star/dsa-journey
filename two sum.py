#two sum
#brute force approach(possible with all nums)
# time complexity o(n)2
#space complexity o(1)
nums=[2, 7, 11, 15]
target==9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
