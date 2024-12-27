def majorityElements(nums:list)->int:
    
    # for value in nums:
    #     if nums.count(value) > (len(nums) / 2):
    #         return value

    count = {}
    for value in nums:
        count[value] = nums.count(value)

nums = [2,2,1,1,1,2,2]
print(majorityElements(nums))