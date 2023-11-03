class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # lets create dictonary for the first string itterate through
        # itterate through second string and if it exists in the dictonary remove a digit else retun false 
        s_list = {}
        for letter in s:
            if letter in s_list:
                s_list[letter] += 1
            else:
                s_list[letter] = 1
        for letter in t:
            if letter in s_list:
                s_list[letter] -= 1
                if s_list[letter] == 0:
                    del s_list[letter]
            else:
                return False
        return len(s_list) == 0