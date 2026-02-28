def merge(intervals):
    """
    合并重叠区间的函数
    参数: intervals - 二维数组，每个元素是一个区间 [starti, endi]
    返回: 合并后的不重叠区间数组
    """
    # 如果输入为空，直接返回空列表
    if not intervals:
        return []
    
    # 按照区间的起始位置进行排序
    # 这样可以确保我们按顺序处理区间，便于合并
    intervals.sort(key=lambda x: x[0])
    
    # 初始化结果列表，将第一个区间放入结果中
    merged = [intervals[0]]
    
    # 从第二个区间开始遍历
    for current in intervals[1:]:
        # 获取结果列表中最后一个区间
        last = merged[-1]
        
        # 检查当前区间是否与最后一个区间重叠
        # 如果当前区间的起始位置小于等于最后一个区间的结束位置，说明有重叠
        if current[0] <= last[1]:
            # 合并区间：将最后一个区间的结束位置更新为两个区间结束位置的较大值
            last[1] = max(last[1], current[1])
        else:
            # 如果没有重叠，将当前区间添加到结果列表中
            merged.append(current)
    
    # 返回合并后的区间列表
    return merged

# 测试用例
def test_merge_intervals():
    """
    测试合并区间函数的测试用例
    """
    # 测试用例1：有重叠的区间
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    result1 = merge(intervals1)
    print(f"输入: {intervals1}")
    print(f"输出: {result1}")
    print(f"期望: [[1,6],[8,10],[15,18]]")
    print()
    
    # 测试用例2：包含关系的区间
    intervals2 = [[1,4],[4,5]]
    result2 = merge(intervals2)
    print(f"输入: {intervals2}")
    print(f"输出: {result2}")
    print(f"期望: [[1,5]]")
    print()
    
    # 测试用例3：无重叠的区间
    intervals3 = [[1,2],[3,4],[5,6]]
    result3 = merge(intervals3)
    print(f"输入: {intervals3}")
    print(f"输出: {result3}")
    print(f"期望: [[1,2],[3,4],[5,6]]")
    print()
    
    # 测试用例4：空输入
    intervals4 = []
    result4 = merge(intervals4)
    print(f"输入: {intervals4}")
    print(f"输出: {result4}")
    print(f"期望: []")
    print()
    
    # 测试用例5：单个区间
    intervals5 = [[1,4]]
    result5 = merge(intervals5)
    print(f"输入: {intervals5}")
    print(f"输出: {result5}")
    print(f"期望: [[1,4]]")
    print()
    
    # 测试用例6：复杂重叠情况
    intervals6 = [[1,3],[2,4],[5,7],[6,8],[9,10]]
    result6 = merge(intervals6)
    print(f"输入: {intervals6}")
    print(f"输出: {result6}")
    print(f"期望: [[1,4],[5,8],[9,10]]")

# 主程序入口
if __name__ == "__main__":
    print("合并重叠区间算法演示")
    print("=" * 30)
    test_merge_intervals()
