"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
"""
class Solution(object):
    def convert1(self, s, numRows):
        """Visit by Row
            Iterate through s from left to right, determine the row where each character (with index i) belongs to.
                - batch_size = 2 * n - 2
                    - if i % batch_size <= batch_size / 2
                        - the character c belongs to row[i % batch_size]
                    - else:
                        - the character c belongs to row[batch_size - i % batch_size]
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [''] * numRows
        batch_size = 2 * numRows - 2
        for i, c in enumerate(s):
            # determine the row where c belongs to
            row = self.checkRow(i, batch_size)
            res[row] += c
        return ''.join(res)

    def checkRow(self, i, batch_size):
        row = i % batch_size
        if row > batch_size / 2:
            row = batch_size - i % batch_size
        return row

    def convert2(self, s, numRows):
        """Sort by Row:
            Iterate through s from left to right, appending each character to the appropriate row.
            Change direction when we moved up to the topmost row or moved down to the bottommost row.
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [''] * numRows
        row, direction = 0, -1
        for i, c in enumerate(s):
            res[row] += c
            if row in [0, numRows-1]:
                direction *= -1
            row += direction
        return ''.join(res)

s1 = Solution().convert1('PAYPALISHIRING', numRows=3)
s2 = Solution().convert2('PAYPALISHIRING', numRows=3)
print(s1, s2)
