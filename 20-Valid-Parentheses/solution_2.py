def isValid(self, s: str) -> bool:
        # find see if there is a remainder when the length of the string is % 2
        # loop through the s with half the length of the string
        # if () , [], {} is found remove it 
        # if nothing is replaced then return false
        # return boolean value of s length
        if len(s) % 2 != 0:
            return False
        for idx in range(len(s)//2):
            answer=s.replace('()', '').replace('[]', '').replace('{}', '')
        return len(answer) == 0