from typing import List, Optional


def reverse_array(nums: List[int], start: int, end: int) -> None:
    """
    反转数组中从start到end的元素（包含start和end）
    
    参数:
        nums -- 要反转的数组
        start -- 起始索引
        end -- 结束索引
    
    返回:
        None (原地修改数组)
    
    异常:
        IndexError -- 当start或end超出数组范围时
    """
    n = len(nums)
    if start < 0 or end >= n or start > end:
        raise IndexError(f"无效的索引范围: start={start}, end={end}, 数组长度={n}")
    
    # 使用双指针法进行反转
    while start < end:
        # 交换start和end位置的元素
        nums[start], nums[end] = nums[end], nums[start]
        # 移动指针，继续交换下一对元素
        start += 1
        end -= 1


def rotate_array_right(nums: List[int], k: int) -> None:
    """
    将数组向右轮转k个位置（原地修改）
    
    使用三次反转法实现，时间复杂度O(n)，空间复杂度O(1)
    
    参数:
        nums -- 要轮转的整数数组
        k -- 轮转位置数（非负整数）
    
    返回:
        None (原地修改数组)
    
    异常:
        ValueError -- 当k为负数时
        TypeError -- 当nums不是列表或k不是整数时
    
    示例:
        >>> nums = [1,2,3,4,5,6,7]
        >>> rotate_array_right(nums, 3)
        >>> print(nums)
        [5, 6, 7, 1, 2, 3, 4]
    """
    # 输入验证
    if not isinstance(nums, list):
        raise TypeError("nums必须是列表")
    if not isinstance(k, int):
        raise TypeError("k必须是整数")
    if k < 0:
        raise ValueError("k必须是非负整数")
    
    # 获取数组长度
    n = len(nums)
    
    # 处理k大于数组长度的情况，避免不必要的轮转
    # 例如数组长度为7，k=10，实际只需要轮转3次（10 % 7 = 3）
    k = k % n if n > 0 else 0
    
    # 如果k为0或者数组为空，直接返回，无需操作
    if k == 0 or n == 0:
        return
    
    # 三次反转法：
    # 第一步：反转整个数组
    # 例如 [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
    reverse_array(nums, 0, n - 1)
    
    # 第二步：反转前k个元素
    # 例如 [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1]
    reverse_array(nums, 0, k - 1)
    
    # 第三步：反转剩余的n-k个元素
    # 例如 [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4]
    reverse_array(nums, k, n - 1)


# 保持向后兼容性的别名
def rotate(nums: List[int], k: int) -> None:
    """
    将数组向右轮转k个位置（向后兼容函数）
    
    此函数是rotate_array_right的别名，保持向后兼容性
    建议使用rotate_array_right以获得更好的类型提示和错误处理
    """
    rotate_array_right(nums, k)

# 测试代码
if __name__ == "__main__":
    print("=== 基本功能测试 ===")
    
    # 测试用例1：正常情况
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    print(f"原始数组: {nums1}")
    rotate_array_right(nums1, k1)
    print(f"轮转{k1}个位置后: {nums1}")
    
    # 测试用例2：k大于数组长度
    nums2 = [1,2,3,4]
    k2 = 6
    print(f"\n原始数组: {nums2}")
    rotate_array_right(nums2, k2)
    print(f"轮转{k2}个位置后: {nums2}")
    
    # 测试用例3：空数组
    nums3 = []
    k3 = 3
    print(f"\n原始数组: {nums3}")
    rotate_array_right(nums3, k3)
    print(f"轮转{k3}个位置后: {nums3}")
    
    # 测试用例4：单个元素
    nums4 = [1]
    k4 = 5
    print(f"\n原始数组: {nums4}")
    rotate_array_right(nums4, k4)
    print(f"轮转{k4}个位置后: {nums4}")
    
    # 测试用例5：k等于数组长度
    nums5 = [1,2,3,4,5]
    k5 = 5
    print(f"\n原始数组: {nums5}")
    rotate_array_right(nums5, k5)
    print(f"轮转{k5}个位置后: {nums5}")
    
    print("\n=== 向后兼容性测试 ===")
    # 测试向后兼容性
    nums6 = [1,2,3,4,5]
    k6 = 2
    print(f"原始数组: {nums6}")
    rotate(nums6, k6)  # 使用旧函数名
    print(f"使用旧函数名轮转{k6}个位置后: {nums6}")
    
    print("\n=== 错误处理测试 ===")
    # 测试错误处理
    try:
        nums7 = [1,2,3]
        k7 = -1
        rotate_array_right(nums7, k7)
    except ValueError as e:
        print(f"捕获到预期错误 (k为负数): {e}")
    
    try:
        nums8 = [1,2,3]
        k8 = "invalid"
        rotate_array_right(nums8, k8)
    except TypeError as e:
        print(f"捕获到预期错误 (k类型错误): {e}")
    
    try:
        nums9 = "not a list"
        k9 = 2
        rotate_array_right(nums9, k9)
    except TypeError as e:
        print(f"捕获到预期错误 (nums类型错误): {e}")
    
    print("\n=== 性能测试 ===")
    import time
    
    # 大数组性能测试
    large_nums = list(range(100000))
    large_k = 99999
    
    start_time = time.time()
    rotate_array_right(large_nums, large_k)
    end_time = time.time()
    
    print(f"大数组 (100,000元素) 轮转耗时: {end_time - start_time:.6f}秒")
    print(f"轮转结果验证: 前5个元素 {large_nums[:5]}, 后5个元素 {large_nums[-5:]}")
    
    print("\n=== reverse_array 函数测试 ===")
    # 测试独立的reverse_array函数
    test_nums = [1,2,3,4,5]
    print(f"原始数组: {test_nums}")
    reverse_array(test_nums, 1, 3)
    print(f"反转索引1-3后: {test_nums}")
    
    # 测试reverse_array错误处理
    try:
        reverse_array(test_nums, -1, 3)
    except IndexError as e:
        print(f"捕获到预期错误 (索引越界): {e}")
