/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  //split the string by the " "
  //pop the last array and see if it contains only letter in the dictionary of english letters
  //then return the length -1
  let splitArr = s.split(' ');
  console.log(splitArr);
  for (let i = splitArr.length - 1; i >= 0; i--) {
    if (splitArr[i].length > 0) {
      return splitArr[i].length;
    }
  }
};
