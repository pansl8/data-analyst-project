# -*- coding:utf-8 -*-
class Solution:
    def threeSum(self, nums):
        length = len(nums)
        result = []
        i = 0
        while i < length:
            flag = False
            j = i + 1
            while j < length:
                k = j + 1
                while k < length:
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        del nums[i]
                        del nums[j]
                        del nums[k]
                        break
                    k += 1
                if flag:
                    break
                j += 1
            if flag:
                continue
            i += 1
        return result


if __name__ == "__main__":
    slt = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    for item in slt.threeSum(nums):
        print(item)
