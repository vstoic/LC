def twoSum (nums, target):
    # solution 2
        # create a dictonary key being the number and the value being the index
        # itterate through the list again this time finding the differene that will add up to the target
        # see if that index matches with the difference and not the same number
        hash = {}
        n = len(nums)
        # dont need to - 1 for range because when you use range it starts from 0 and -1.
        for i in range(n):
            hash[nums[i]] = i

        for i in range(n):
            diff = target - nums[i]
            if diff in hash and hash[diff] != i:
                return [i, hash[diff]]
        return False