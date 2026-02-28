def productExceptSelf(nums):
    """
    给你一个整数数组 nums，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    不使用除法，且在 O(n) 时间复杂度内完成此题。
    
    参数:
    nums (List[int]): 输入的整数数组
    
    返回:
    List[int]: 结果数组 answer
    """
    n = len(nums)  # 获取数组的长度
    answer = [1] * n  # 初始化结果数组，所有元素设为1
    
    # 第一遍遍历：计算每个元素左侧所有元素的乘积
    left_product = 1  # 初始化左侧乘积为1
    for i in range(n):
        answer[i] = left_product  # 将当前元素的左侧乘积存入结果数组
        left_product *= nums[i]   # 更新左侧乘积，包含当前元素
    
    # 第二遍遍历：计算每个元素右侧所有元素的乘积，并与左侧乘积相乘
    right_product = 1  # 初始化右侧乘积为1
    for i in range(n-1, -1, -1):  # 从数组末尾开始遍历
        answer[i] *= right_product  # 将右侧乘积与结果数组中的左侧乘积相乘
        right_product *= nums[i]    # 更新右侧乘积，包含当前元素
    
    return answer  # 返回最终结果数组

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    nums1 = [1, 2, 3, 4]
    print(f"输入: {nums1}")
    print(f"输出: {productExceptSelf(nums1)}")  # 预期输出: [24, 12, 8, 6]
    
    # 测试用例2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"输入: {nums2}")
    print(f"输出: {productExceptSelf(nums2)}")  # 预期输出: [0, 0, 9, 0, 0]
    
    # 测试用例3
    nums3 = [4, 5, 1, 8, 2]
    print(f"输入: {nums3}")
    print(f"输出: {productExceptSelf(nums3)}")  # 预期输出: [80, 64, 320, 40, 160]
