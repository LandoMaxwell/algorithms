def firstMissingPositive(nums):
    """
    找出未排序数组中缺失的最小正整数
    
    参数:
    nums: 未排序的整数数组
    
    返回:
    缺失的最小正整数
    """
    n = len(nums)  # 获取数组长度
    
    # 第一步：将所有非正数和大于n的数设置为n+1
    # 因为缺失的最小正整数范围在1到n+1之间
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1
    
    # 第二步：将出现的正整数对应位置的数标记为负数
    # 利用数组本身作为哈希表，通过符号标记数字是否出现过
    for i in range(n):
        num = abs(nums[i])  # 取绝对值，因为可能已经被标记为负数
        if num <= n:  # 只处理在1到n范围内的数
            # 将对应位置的数标记为负数（如果还不是负数的话）
            if nums[num - 1] > 0:  # num-1是因为数组索引从0开始
                nums[num - 1] = -nums[num - 1]
    
    # 第三步：找到第一个正数的位置，其索引+1就是缺失的最小正整数
    for i in range(n):
        if nums[i] > 0:  # 如果当前位置是正数，说明i+1这个数没有出现过
            return i + 1
    
    # 如果所有位置都被标记了，说明1到n都出现了，缺失的是n+1
    return n + 1


# 测试代码
if __name__ == "__main__":
    # 测试用例1
    nums1 = [1, 2, 0]
    print(f"输入: {nums1}")
    print(f"输出: {firstMissingPositive(nums1)}")  # 应该输出3
    print()
    
    # 测试用例2
    nums2 = [3, 4, -1, 1]
    print(f"输入: {nums2}")
    print(f"输出: {firstMissingPositive(nums2)}")  # 应该输出2
    print()
    
    # 测试用例3
    nums3 = [7, 8, 9, 11, 12]
    print(f"输入: {nums3}")
    print(f"输出: {firstMissingPositive(nums3)}")  # 应该输出1
    print()
    
    # 测试用例4
    nums4 = [1, 2, 3, 4, 5]
    print(f"输入: {nums4}")
    print(f"输出: {firstMissingPositive(nums4)}")  # 应该输出6
    print()
    
    # 测试用例5
    nums5 = [1]
    print(f"输入: {nums5}")
    print(f"输出: {firstMissingPositive(nums5)}")  # 应该输出2
