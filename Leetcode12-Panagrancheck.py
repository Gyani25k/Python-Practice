class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        alphabet = set(string.ascii_lowercase)
    
        letters_in_sentence = set(sentence.lower())
        return set(alphabet) <= letters_in_sentence

