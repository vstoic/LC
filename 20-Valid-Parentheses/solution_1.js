var isValid = function (s) {
  //have an empty array/ answer stack
  //create a hashmap that have a key of opening bracket and value of closing value
  //itterate through the stack
  //set variable for each itteration of the stack
  //if the variable exists as a key in the as a map push the value into the stack
  //else if the last item in the stack is not equal to a key of the closing bracket then return false
  //in the end return a boolian for the stack length

  let stack = [];

  array = [a,b,c]
  let map = {
    '(': '[]',
    '{': '}',
    '[': ']',
  };
  for (let i = 0; i < s.length; i++) {
    let bracket = s[i];
    if (map[bracket]) {
      stack.push(map[bracket]);
    } else if (bracket !== stack.pop()) {
      return false;
    }
  }
  return !stack.length;
};
