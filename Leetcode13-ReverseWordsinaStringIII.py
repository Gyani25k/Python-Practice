class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split(" ")
        result = ""
        for word in res:
            reversed_word = word[::-1]
            result += reversed_word + " "
        return result.strip()
