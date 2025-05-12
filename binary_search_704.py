from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 이진 탐색 알고리즘
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # 중간 인덱스

            if nums[mid] == target:  # target을 찾았을 경우
                return mid
            elif nums[mid] < target:  # 중간값이 target보다 작으면 오른쪽 절반 탐색
                left = mid + 1
            else:  # 중간값이 target보다 크면 왼쪽 절반 탐색
                right = mid - 1

        return -1  # target이 배열에 없을 경우




"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 재귀적으로 이진 탐색 수행
        def binary_search(left: int, right: int) -> int:
            if left > right:  # 탐색 범위가 없으면 종료
                return -1

            mid = (left + right) // 2  # 중간 인덱스

            if nums[mid] == target:  # 중간값이 target이면 해당 인덱스 반환
                return mid
            elif nums[mid] < target:  # 중간값이 target보다 작으면 오른쪽 절반 탐색
                return binary_search(mid + 1, right)
            else:  # 중간값이 target보다 크면 왼쪽 절반 탐색
                return binary_search(left, mid - 1)
        
        # 처음 호출 시 전체 범위를 넘겨줌
        return binary_search(0, len(nums) - 1)
"""
