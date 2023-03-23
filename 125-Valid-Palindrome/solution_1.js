/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let lowString = s.toLowerCase();
  let cleaned = lowString.replace(/[^A-Za-z0-9]/g, '');
  // / begining of regex
  // ^ characters not in this set
  // [A-Za-z0-9] set of characters
  // /g, global search replace all occurences not just first
  // '' empty string to replace with
  // console.log(cleaned)
  let first = 0;
  let last = cleaned.length - 1;
  while (last > first) {
    if (cleaned[first] === cleaned[last]) {
      first++;
      last--;
    } else {
      return false;
    }
  }
  return true;
};
