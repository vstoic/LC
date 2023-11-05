  
def twoSum (nums, target):
  # brute force
  # using the length -1 of the nums array, itterate through the array
  # now itterate through the rest of the array matching it with the selected index num
  # if the num adds up to the target, return the indexs.

  numLength = len(nums)

  for first in range(numLength - 1):
      for searchIndex in range(first + 1, numLength):
          if nums[first] + nums[searchIndex] == target:
              return [first, searchIndex]
  return False 