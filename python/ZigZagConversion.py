
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a
 given number of rows like this: (you may want to display this pattern 
 in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if  numRows == 1 :
            return s
        ans = []
        for i in range(numRows):
            ans.append([])
        row, i , desc = 0 , 0, True
        while i < len(s):
            ans[row].append(s[i])
            i += 1
            if desc:
                if row == numRows-1:
                    row -= 1
                    desc = False
                else:
                    row += 1
            else:
                if row == 0:
                    desc = True
                    row += 1
                else:
                    row -= 1
        ret = ""
        for l in ans:
            ret += "".join(l)
        return ret


            
            
        