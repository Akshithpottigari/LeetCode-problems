def findDuplicate(nums):
    hash = {}
    for item in nums:
        if item in hash:
            return item
        else:
            hash[item]=1
