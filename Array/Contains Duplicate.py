def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = [1, 4, 2, 7, 5, 7]
result = containsDuplicate(nums)
print(result)