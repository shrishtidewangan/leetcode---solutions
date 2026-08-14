def containNearByDuplicate(nums, k):
    window = set()
    for i, num in emumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) < k:
            window.remove(nums[i-k])
    return False
nums = [1,2,3,1,2,3]
k = 3
result = containNearByDuplicate(nums, k)
print(result)