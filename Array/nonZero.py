'''
here,

    Naive Approach - Using Additional Array

    This approach leverages the use of an additional array to store the non-zero elements separately and finally concatenate the zeroes with the non-zero elements array. The idea is to iterate through the original array and build a separate list of non-zero elements. Once gathered, we'll fill the rest of the original array with zeroes.

    Steps:

    1. Initialize an empty list result to store non-zero elements.
    2. Iterate over each element num in the array nums.
    3. If num is non-zero, append it to the result list.
    4. Calculate the number of zeroes zero_count by subtracting the length of result from the length of nums.
    5. Extend result by the list of zeroes [0] * zero_count.
    6. Replace nums elements with elements from result to achieve in-place requirement.

    
    
    Optimal Approach - Two Pointer Technique

    This approach improves upon the naive approach by eliminating the need for an auxiliary list. Instead, we rearrange the elements in-place using a two-pointer technique. We maintain one pointer, last_non_zero_found_at, to track the position of the last non-zero element. As we iterate, we swap non-zero elements with the position pointed by last_non_zero_found_at.

    Steps:

    1. Initialize a pointer last_non_zero_found_at at index 0.
    2. Iterate through each element in nums using a pointer i.
    3. If the current element nums[i] is non-zero, swap nums[i] with nums[last_non_zero_found_at].
    4. Increment last_non_zero_found_at after the swap to move to the next position.
    5. Post iteration, all non-zero elements are at the beginning and rest are zeroes.

'''

def moveZero(nums:list):
    # non_zero = []
    # lenght_of_ori_nums = len(nums)
    # for value in nums:
    #     if value != 0:
    #         non_zero.append(value)

    # lenght_of_non_zero_list = len(non_zero)
    # while lenght_of_ori_nums > lenght_of_non_zero_list:
    #     non_zero.append(0)
    #     lenght_of_non_zero_list += 1

    # print(non_zero)

    index = 0
    for value in range(len(nums)):
        if value != 0:
            nums[index],nums[value] = nums[value],nums[index]
            index += 1
    return nums

nums = [3,0,5,7,0]
moveZero(nums)