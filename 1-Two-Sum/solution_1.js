/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  //make a hashmap and with the keys of a number and then a value of a index
  //itterate through the array and check if the key is already in the hashmap
  // if not then we create it and set the value to the index within the nums
  // else if it exists in the hashmap then we return the answer of
  //[index in the hash map, index within the loop of nums ]
  
  let hash = {};
  for (let i = 0; i < nums.length; i++) {
    if (hash[target - nums[i]] || hash[target - nums[i]] === 0) {
      return [hash[target - nums[i]], i];
    } else {
      hash[nums[i]] = i;
    }
  }
};
