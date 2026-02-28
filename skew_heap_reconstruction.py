#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
斜堆(Skew Heap)插入序列重构算法

问题描述：
给定一个斜堆的结构，重构出可能产生该结构的插入序列P。
斜堆是一种优先队列，每次插入元素时都会进行合并操作。

算法思路：
1. 逆向思考：从最终的斜堆结构出发，逆向模拟插入过程
2. 候选节点识别：在每一步中，识别哪些节点可能是最后插入的
3. 贪心策略：根据不同的贪心策略选择候选节点，生成字典序最小和最大的插入序列
4. 逆向插入：移除选中的节点并恢复之前的堆结构
"""

class Node:
    """树节点类"""
    def __init__(self, l=0, r=0, p=0):
        self.L = l      # 左孩子节点索引
        self.R = r      # 右孩子节点索引
        self.P = p      # 父节点索引

class SkewHeapReconstruction:
    """斜堆插入序列重构算法类"""
    
    def __init__(self):
        self.N = 0                      # 斜堆中的节点数量
        self.initial_tree = []          # 初始树结构，使用1-based索引，tree[0]不使用
    
    def find_candidates(self, tree, root):
        """
        查找候选节点函数
        
        算法思路：
        一个节点x可能是最后插入的候选节点，如果移除它后能得到一个有效的斜堆结构。
        
        候选节点识别规则：
        1. 沿着左脊线(left spine)找到最上面的没有右孩子的节点vk
        2. vk总是候选节点
        3. 如果vk的左孩子vk+1存在且是叶子节点，则vk+1也是候选节点
        
        参数：
        tree - 当前树结构
        root - 根节点索引
        
        返回：
        候选节点索引列表
        """
        if root == 0:
            return []
        
        # 1. 沿着左脊线找到最上面的没有右孩子的节点vk
        # 左脊线：从根节点开始，一直沿着左孩子路径
        vk = 0
        curr = root
        while curr != 0:
            if tree[curr].R == 0:  # 找到没有右孩子的节点
                vk = curr
                break
            curr = tree[curr].L  # 继续沿左脊线向下
        
        # 如果左脊线上所有节点都有右孩子，则不存在候选节点
        # 这意味着树结构不是通过顺序插入构建的有效斜堆
        if vk == 0:
            return []
        
        candidates = []
        # vk总是有效的候选节点
        candidates.append(vk)
        
        # 2. 检查vk的左孩子vk+1
        vk_plus_1 = tree[vk].L
        if vk_plus_1 != 0:
            # vk+1是候选节点当且仅当它是叶子节点（L=0且R=0）
            # 这个条件来源于：C2条件(R=0)和C3条件(因为R(vk)=0所以L=0)
            if tree[vk_plus_1].L == 0 and tree[vk_plus_1].R == 0:
                candidates.append(vk_plus_1)
        
        return candidates
    
    def reverse_insertion(self, tree, x, root):
        """
        逆向插入操作函数
        
        算法思路：
        模拟插入操作的逆过程，移除节点x并恢复插入前的堆结构。
        斜堆的插入操作涉及合并和交换子树，逆向操作需要：
        1. 移除节点x，提升其左孩子
        2. 沿着父节点路径向上交换左右子树，抵消插入时的交换操作
        
        参数：
        tree - 当前树结构（会被修改）
        x - 要移除的节点索引
        root - 当前根节点索引
        
        返回：
        移除操作后的新根节点索引
        """
        w = tree[x].L      # x的左孩子
        px = tree[x].P     # x的父节点
        
        # 1. 移除节点x，提升其左孩子w
        if px == 0:
            # x是根节点的情况
            root = w
            if w != 0:
                tree[w].P = 0  # 新根节点的父节点设为0
        else:
            # x必须是px的左孩子（因为它在左脊线上）
            tree[px].L = w
            if w != 0:
                tree[w].P = px  # 更新w的父节点
        
        # 清除x的连接（虽然不是严格必需，因为x不会被重用）
        tree[x].L = tree[x].R = tree[x].P = 0
        
        # 2. 沿着从px到根节点的路径交换左右子树
        # 这抵消了插入x时发生的交换操作
        curr = px
        while curr != 0:
            # 交换左右子树
            tree[curr].L, tree[curr].R = tree[curr].R, tree[curr].L
            curr = tree[curr].P  # 向上移动到父节点
        
        return root
    
    def find_permutation(self, strategy):
        """
        贪心策略执行函数
        
        算法思路：
        通过贪心策略重构插入序列。每一步选择候选节点，逆向模拟插入过程。
        
        贪心策略：
        - strategy = 0: 字典序最小的插入序列P
          每次选择数值最大的候选节点（最大化移除效果）
        - strategy = 1: 字典序最大的插入序列P  
          每次选择数值最小的候选节点（最小化移除效果）
        
        参数：
        strategy - 贪心策略类型
        
        返回：
        重构的插入序列（正向顺序）
        """
        # 在树结构的副本上操作，避免修改原始数据
        tree = [Node() for _ in range(len(self.initial_tree))]
        for i in range(len(self.initial_tree)):
            tree[i].L = self.initial_tree[i].L
            tree[i].R = self.initial_tree[i].R
            tree[i].P = self.initial_tree[i].P
        
        # 如果N>0，根节点总是1（因为1是最小的元素）
        root = 1 if self.N > 0 else 0
        reversed_P = []  # 逆向存储的插入序列
        
        # 执行N次逆向插入操作
        for _ in range(self.N):
            # 查找当前树结构的候选节点
            candidates = self.find_candidates(tree, root)
            
            if not candidates:
                return []  # 无法重构，返回空序列
            
            if strategy == 0:
                # 策略0：字典序最小的P
                # 每次选择数值最大的候选节点（最大化移除）
                x = max(candidates)
            else:
                # 策略1：字典序最大的P
                # 每次选择数值最小的候选节点（最小化移除）
                x = min(candidates)
            
            # 记录选中的节点并执行逆向插入
            reversed_P.append(x)
            root = self.reverse_insertion(tree, x, root)
        
        # 反转序列得到正向的插入顺序
        return reversed_P[::-1]
    
    def solve(self):
        """
        主求解函数
        
        算法思路：
        1. 读取输入数据（节点数量和树结构）
        2. 构建初始树结构
        3. 使用两种贪心策略求解插入序列
        4. 输出结果：字典序最小的插入序列和字典序最大的插入序列
        """
        try:
            # 读取节点数量N
            import sys
            input = sys.stdin.read().split()
            ptr = 0
            
            if ptr >= len(input):
                return
            
            self.N = int(input[ptr])
            ptr += 1
            
            # 初始化树结构，使用1-based索引
            self.initial_tree = [Node() for _ in range(self.N + 1)]
            
            # 读取每个节点的左右孩子信息
            for i in range(1, self.N + 1):
                if ptr + 1 >= len(input):
                    return
                
                l = int(input[ptr])
                r = int(input[ptr + 1])
                ptr += 2
                
                # 设置节点i的左右孩子
                self.initial_tree[i].L = l
                self.initial_tree[i].R = r
                
                # 设置孩子节点的父指针
                if l != 0:
                    self.initial_tree[l].P = i
                if r != 0:
                    self.initial_tree[r].P = i
            
            # 策略0：求字典序最小的插入序列P
            min_P = self.find_permutation(0)
            if not min_P:
                print("impossible")
                return
            
            # 策略1：求字典序最大的插入序列P
            # 如果min_P存在，max_P也应该存在
            max_P = self.find_permutation(1)
            
            # 输出结果
            # 输出字典序最小的插入序列
            print(' '.join(map(str, min_P)))
            
            # 输出字典序最大的插入序列
            print(' '.join(map(str, max_P)))
            
        except (ValueError, IndexError):
            # 处理输入错误
            pass

def main():
    """主函数"""
    solver = SkewHeapReconstruction()
    solver.solve()

if __name__ == "__main__":
    main()
