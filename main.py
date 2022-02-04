class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        rnumber = []
        r = [y for y in s]
        for i in r:
            rnumber.append(roman[i])
        num = 0
        for i in range(len(rnumber) - 1, -1, -1):
            if rnumber[i - 1] < rnumber[i] and i != 0:
                num += rnumber[i] - (rnumber[i - 1] * 2)
            else:
                num += rnumber[i]
        return num