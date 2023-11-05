
def groupAnagrams(strs):
    # create a hash
    # itterate through the list
    #  if it exists in the hash add the unsorted
    # else add it to the hash
    # return the values for the hash
    answer = {}
    for word in strs: 
        sortedWord = ''.join(sorted(word))
        if sortedWord in answer:
            answer[sortedWord].append(word)
        else: 
            answer[sortedWord] = [word]
    return (answer.values())