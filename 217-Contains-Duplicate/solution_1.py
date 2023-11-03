def containsDuplicate(nums) -> bool:
    hashset= set()
    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)

