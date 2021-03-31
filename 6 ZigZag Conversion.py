# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 and numRows <= len(s): return s
        li = ['']*numRows
        row,step = 0,0
        for i in s:
            li[row] += i
            if row == 0: step = 1
            elif row == numRows - 1: step = -1
            # print(li)
            row += step
        return ''.join(li)
if __name__ == '__main__':
    a = Solution()
    print(a.convert('PAYPALISHIRING',3))

'''
Runtime: 56 ms, faster than 79.57% of Python3 online submissions for ZigZag Conversion.
Memory Usage: 14.4 MB, less than 47.73% of Python3 online submissions for ZigZag Conversion.
'''