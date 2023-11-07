def isValid(s):
    # build a hash "model" that contains the open and close 
    # itterate through the input and find the key value in the model and add it to the answer hash.
    # if it cannot be found see if it matches the values of any of the values in the answer hash
    # if it exists remove the pair in the answer hash
    model = {'(':')', '{': '}', '[':']'}
    answer = []
    for char in s:
        if char in model:
            answer.append(char)
        elif char in model.values():
            if not answer or model[answer.pop()] != char:
                return False
        else:
            return False
    return len(answer) == 0