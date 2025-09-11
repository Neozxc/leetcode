class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([char for char in s if char.lower() in 'aeiou'])
        result = list(s)
        vowel_index = 0

        for i in range(len(result)):
            if result[i].lower() in 'aeiou':
                result[i] = vowels[vowel_index]
                vowel_index += 1

        return "".join(result)
