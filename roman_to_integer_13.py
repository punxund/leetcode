#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        int_array = []
        for i in s :
            match i :
                case 'I' :
                    int_array.append(1)
                case 'V':
                    int_array.append(5)
                case 'X':
                    int_array.append(10)
                case 'L':
                    int_array.append(50)
                case 'C':
                    int_array.append(100)
                case 'D':
                    int_array.append(500)
                case 'M':
                    int_array.append(1000)

        for j in range(len(int_array)-1) :
            if int_array[j] >= int_array[j+1] :
                result += int_array[j]
            else :
                result += int_array[j+1]-int_array[j]

        print(result)

# 내코드는 앞에서 부터 확인하려해서 문제, 뒤에부터 하는 코드는 아래
class Solution2:
    def romanToInt2(self, s: str) -> int:
        def get_value(ch: str) -> int:
            match ch:
                case 'I': return 1
                case 'V': return 5
                case 'X': return 10
                case 'L': return 50
                case 'C': return 100
                case 'D': return 500
                case 'M': return 1000

        result = 0
        prev = 0

        for ch in reversed(s):
            value = get_value(ch)
            if value < prev:
                result -= value
            else:
                result += value
                prev = value

        return result

s = Solution()
print(s.romanToInt('III'))