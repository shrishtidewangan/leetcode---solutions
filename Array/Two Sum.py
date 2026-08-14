def Two_Sum(nums, target):
    seen={}
    for i, nums in enumerate(nums):
        complement = target - nums

        if complement in seen:
            return [seen[complement], i]
        seen[nums]=i 

nums = [2,7,11,15]
target=9

result = Two_Sum(nums, target)
print(result)



