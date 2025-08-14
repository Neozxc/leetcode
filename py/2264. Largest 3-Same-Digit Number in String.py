class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_str = ''

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i + 1] == num[i + 2]:
                if num[i] > good_str:
                    good_str = num[i]
        
        if good_str == '':
            return ""
        else:
            return good_str * 3
