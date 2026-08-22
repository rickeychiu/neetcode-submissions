class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            for char in string:
                encodedString += str(ord(char)) + ","
            encodedString += " "
        return encodedString

    def decode(self, s: str) -> List[str]:

        returnArr = []
        strings = s.split(" ")
        for string in strings:
            
            characters = string.split(",")
            
            returnStr = ""
            for code in characters:
                if code.isdigit():
                    returnStr += chr(int(code))
            returnArr.append(returnStr)
        
        return returnArr[:-1]
