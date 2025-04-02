'''
 Reverse Degree of a String
 Given a string s, calculate its reverse degree.

 The reverse degree is calculated as follows:
    For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).
    Sum these products for all characters in the string.

 In this problem I decided to keep track of two variables, index at of a character and fina results, which holds the sum of all characters multiplied by their index
 Every character's position is obtained by using ord() function, which returs asci value. 
 These values start and 96 so I subtract that number and also substract 27 to get character's reversed position in alphabet.
 To avoid negative numbers I used abs() function.
'''

class Solution:

    def reverseDegree(s: str) -> int:
        index: int = 1
        result: int = 0
        for char in s:
            result += abs(ord(char)-123) * index
            index += 1
        return result
    

case1: Solution = Solution.reverseDegree(s="abc")
print(case1)    # Should ouptut 148

case2: Solution = Solution.reverseDegree(s="zaza")
print(case2)    # Should ouptut 160