def twoSum(nums:list,target:int)->list:
    numsDict = {}
    for index,value in enumerate(nums):
        numsDict[value] = index

    for key in numsDict.keys():
        complement = target - key
        if complement in numsDict:
            return [numsDict[key],numsDict[complement]]
        
nums = [1,3,5,8]
target = 8
print(twoSum(nums,target))