#https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        word = self.countAndSay(n - 1)

        answer = ""
        prev_char = word[0]
        count = 1

        for char in word[1:]:
            if char == prev_char:
                count += 1
            else:
                answer += str(count) + prev_char
                prev_char = char
                count = 1

        # Last group handling
        answer += str(count) + prev_char

        return answer


    def countAndSay_dp(self, n: int):
        dp = [""] * (n + 1)
        dp[1] = "1"

        for i in range(2, n + 1):
            prev = dp[i - 1]
            result = ""
            count = 1
            for j in range(1, len(prev)):
                if prev[j] == prev[j - 1]:
                    count += 1
                else:
                    result += str(count) + prev[j - 1]
                    count = 1
            result += str(count) + prev[-1]  # 마지막 그룹 추가
            dp[i] = result

        return dp[n]

test = Solution()
print(test.countAndSay_dp(8))