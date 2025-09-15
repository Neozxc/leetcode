class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split(' ')
        count = 0

        for word in words:
            for char in word:
                if char in broken:
                    break
            else:
                count += 1

        return count
