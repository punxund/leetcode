from typing import List
#바이너리서치
def whitepaper(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    pointer = 0
    merged_nums = []

    for i in nums1:
        # nums2에서 i보다 작거나 같은 모든 값을 먼저 넣음
        while pointer < len(nums2) and nums2[pointer] <= i:
            merged_nums.append(nums2[pointer])
            pointer += 1
        merged_nums.append(i)

    # nums1을 다 순회한 후 nums2에 남은 값이 있으면 이어 붙임
    while pointer < len(nums2):
        merged_nums.append(nums2[pointer])
        pointer += 1

    return merged_nums

# 예시 출력
print(whitepaper([1,2,3,4,5], [1,3,5]))
# 예상 출력: [1,1,2,3,3,4,5,5]
