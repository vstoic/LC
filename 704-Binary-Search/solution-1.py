def search(nums, target):
        # b search splits the array into two key word sorted!
        # set a left and right 
        # find the middle index
        # using a while loop
        # if middle return middle index
        # otherwise split into left and right side 
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1