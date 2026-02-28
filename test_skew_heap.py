#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
斜堆插入序列重构算法测试用例
"""

from skew_heap_reconstruction import SkewHeapReconstruction
import sys

def test_case_1():
    """测试用例1：简单的3节点斜堆"""
    print("=== 测试用例1：简单的3节点斜堆 ===")
    
    # 模拟输入：3个节点
    # 节点1：左=2，右=3
    # 节点2：左=0，右=0  
    # 节点3：左=0，右=0
    input_data = "3\n2 3\n0 0\n0 0"
    
    # 重定向标准输入
    import io
    sys.stdin = io.StringIO(input_data)
    
    solver = SkewHeapReconstruction()
    solver.solve()
    
    # 恢复标准输入
    sys.stdin = sys.__stdin__

def test_case_2():
    """测试用例2：不可能的情况"""
    print("\n=== 测试用例2：不可能的情况 ===")
    
    # 模拟输入：无效的斜堆结构
    input_data = "2\n2 0\n1 0"
    
    import io
    sys.stdin = io.StringIO(input_data)
    
    solver = SkewHeapReconstruction()
    solver.solve()
    
    sys.stdin = sys.__stdin__

def test_case_3():
    """测试用例3：更复杂的结构"""
    print("\n=== 测试用例3：更复杂的结构 ===")
    
    # 模拟输入：5个节点的复杂结构
    input_data = "5\n2 3\n4 5\n0 0\n0 0\n0 0"
    
    import io
    sys.stdin = io.StringIO(input_data)
    
    solver = SkewHeapReconstruction()
    solver.solve()
    
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    print("开始测试斜堆插入序列重构算法...")
    
    test_case_1()
    test_case_2() 
    test_case_3()
    
    print("\n测试完成！")
