# coding=utf-8
class Solution:
    # 1.1 字符是否唯一
    def uniqueChar(self, str):
        dict = {}
        for c in str:
            if c not in dict:
                dict[c] = True
            else:
                return False
        return True

    # 1.2 字符串反转
    def reverseStr(self, str):
        return str[::-1]

    # 1.3 两个字符串是否为变位词，anagram回文构词法,由颠倒字母顺序组成的单词
    def isAnagram(self, str1, str2):
        dict1 = {}; dict2 = {}
        for c in str1:
            dict1[c] = dict1.get(c, 0) + 1
        for c in str2:
            dict2[c] = dict2.get(c, 0) + 1
        if dict1 == dict2: return True
        else: return False
    
    # 1.4 空格替换为%20
    def replaceChar(self, str):
        ss = list(str)
        for i in range(len(ss)):
            if ss[i] == " ": ss[i] = "%20"
        return "".join(ss)
    
    # 1.5 字符串去重
    def compress(self, input):
        if input is None or len(input) == 0 or len(input) == 1: return input
        prev = input[:1]; cnt = 1
        res = input[:1]
        for c in input[1:]:
            if c is not prev:
                res = res + str(cnt); cnt = 1; prev = c; res = res + c
            else:
                cnt += 1
        res = res + str(cnt)
        if len(res) >= len(input): return input
        else: return res

    # 1.6  图片旋转90
    def rotateImage(self, matrix):
        return [list(reversed(x)) for x in zip(*matrix)]
 
    # 1.7  二维数组置0
    def setZero(self, matrix):
        row = [True for i in range(len(matrix))]
        col = [True for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = False; col[j] = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == False or col[j] == False:
                    matrix[i][j] = 0

    # 1.8 调用一次子字符串判断确认s2是否为s1的旋转字符
    def isRotation(self, str1, str2):
        if str1 is None and str2 is None: return True
        if len(str1) != len(str2): return False
        str3 = str2 + str2
        return str1 in str3

if __name__ == "__main__":
    s = Solution()
    # 1.1
    print "# 1.1"
    print s.uniqueChar("aassbcd")
    # 1.2
    print "# 1.2"
    print s.reverseStr("abcd")
    # 1.3
    print "# 1.3"
    print s.isAnagram("shen", "hsne")
    print s.isAnagram("yes", "nnnsye")
    # 1.4
    print "# 1.4"
    print s.replaceChar("nathan shen")
    # 1.5
    print "# 1.5"
    print s.compress("aabcccccaaa")
    print s.compress("abcdefg")
    # 1.6
    print "# 1.6"
    a = [[1, 2, 3], [4, 5, 6]]
    print s.rotateImage(a)
    # 1.7
    print "# 1.7"
    a = [[1,1,1], [1,0,1]]
    s.setZero(a)
    print a
    # 1.8
    print "# 1.8"
    print s.isRotation("waterbottle", "erbottlewat")
