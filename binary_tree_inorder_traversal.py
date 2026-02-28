from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    """
    二叉树节点类
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        """
        初始化二叉树节点
        :param val: 节点值
        :param left: 左子节点
        :param right: 右子节点
        """
        self.val = val        # 节点存储的值
        self.left = left      # 指向左子节点的指针
        self.right = right    # 指向右子节点的指针


class Solution:
    """
    二叉树中序遍历解决方案
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        递归方法实现二叉树的中序遍历
        中序遍历顺序：左子树 -> 根节点 -> 右子树
        
        时间复杂度: O(n)，其中 n 是二叉树的节点数
        空间复杂度: O(n)，最坏情况下树的高度为 n（当树退化为链表时），平均情况下为 O(log n)
        
        :param root: 二叉树的根节点
        :return: 包含中序遍历结果的列表
        """
        result = []  # 用于存储遍历结果的列表
        
        def inorder(node: Optional[TreeNode]) -> None:
            """
            递归辅助函数，执行中序遍历
            :param node: 当前遍历的节点
            """
            # 如果当前节点为空，直接返回（递归终止条件）
            if not node:
                return
            
            # 1. 先遍历左子树
            inorder(node.left)
            
            # 2. 访问根节点，将节点值添加到结果列表
            result.append(node.val)
            
            # 3. 最后遍历右子树
            inorder(node.right)
        
        # 从根节点开始递归遍历
        inorder(root)
        
        return result  # 返回中序遍历结果
    
    def inorderTraversal_functional(self, root: Optional[TreeNode]) -> List[int]:
        """
        函数式风格的递归方法实现二叉树的中序遍历
        这种方法更加简洁，但可能会创建更多的临时列表
        
        时间复杂度: O(n)，其中 n 是二叉树的节点数
        空间复杂度: O(n)，最坏情况下树的高度为 n（当树退化为链表时），平均情况下为 O(log n)
        
        :param root: 二叉树的根节点
        :return: 包含中序遍历结果的列表
        """
        # 基本情况：如果节点为空，返回空列表
        if not root:
            return []
        
        # 递归情况：左子树结果 + [当前节点值] + 右子树结果
        return (self.inorderTraversal_functional(root.left) +
                [root.val] +
                self.inorderTraversal_functional(root.right))
    
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        迭代方法实现二叉树的中序遍历（使用栈）
        中序遍历顺序：左子树 -> 根节点 -> 右子树
        
        时间复杂度: O(n)，其中 n 是二叉树的节点数
        空间复杂度: O(n)，最坏情况下栈的大小为 n（当树退化为链表时），平均情况下为 O(log n)
        
        :param root: 二叉树的根节点
        :return: 包含中序遍历结果的列表
        """
        result = []      # 用于存储遍历结果的列表
        stack = []       # 用于模拟递归的栈
        current = root   # 当前遍历的节点
        
        # 当当前节点不为空或栈不为空时继续循环
        while current or stack:
            
            # 1. 将所有左子节点压入栈中
            # 沿着左子树一直向下走，直到最左边的叶子节点
            while current:
                stack.append(current)  # 将当前节点压入栈
                current = current.left  # 移动到左子节点
            
            # 2. 弹出栈顶节点并访问
            # 此时栈顶节点是最左边的节点或需要访问的根节点
            current = stack.pop()      # 弹出栈顶节点
            result.append(current.val) # 将节点值添加到结果列表
            
            # 3. 转向右子树
            # 处理完左子树和根节点后，处理右子树
            current = current.right
        
        return result  # 返回中序遍历结果
    
    def inorderTraversal_iterative_deque(self, root: Optional[TreeNode]) -> List[int]:
        """
        使用 collections.deque 的迭代方法实现二叉树的中序遍历
        中序遍历顺序：左子树 -> 根节点 -> 右子树
        
        时间复杂度: O(n)，其中 n 是二叉树的节点数
        空间复杂度: O(n)，最坏情况下栈的大小为 n（当树退化为链表时），平均情况下为 O(log n)
        
        :param root: 二叉树的根节点
        :return: 包含中序遍历结果的列表
        """
        from collections import deque
        
        result = []          # 用于存储遍历结果的列表
        stack = deque()      # 使用 deque 作为栈
        current = root       # 当前遍历的节点
        
        # 当当前节点不为空或栈不为空时继续循环
        while current or stack:
            
            # 1. 将所有左子节点压入栈中
            # 沿着左子树一直向下走，直到最左边的叶子节点
            while current:
                stack.append(current)  # 将当前节点压入栈
                current = current.left  # 移动到左子节点
            
            # 2. 弹出栈顶节点并访问
            # 此时栈顶节点是最左边的节点或需要访问的根节点
            current = stack.pop()      # 弹出栈顶节点
            result.append(current.val) # 将节点值添加到结果列表
            
            # 3. 转向右子树
            # 处理完左子树和根节点后，处理右子树
            current = current.right
        
        return result  # 返回中序遍历结果
    
    def inorderTraversal_morris(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris 中序遍历方法（不使用递归或栈）
        中序遍历顺序：左子树 -> 根节点 -> 右子树
        
        时间复杂度: O(n)，其中 n 是二叉树的节点数
        空间复杂度: O(1)，只使用了常数级别的额外空间
        
        :param root: 二叉树的根节点
        :return: 包含中序遍历结果的列表
        """
        result = []      # 用于存储遍历结果的列表
        current = root   # 当前遍历的节点
        
        while current:
            # 如果当前节点没有左子节点
            if not current.left:
                # 直接访问当前节点
                result.append(current.val)
                # 移动到右子节点
                current = current.right
            else:
                # 找到当前节点左子树的最右节点（即中序遍历中当前节点的前驱节点）
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                # 如果前驱节点的右子节点为空
                if not predecessor.right:
                    # 将前驱节点的右子节点指向当前节点（建立临时链接）
                    predecessor.right = current
                    # 移动到左子节点
                    current = current.left
                else:
                    # 如果前驱节点的右子节点指向当前节点（说明左子树已经遍历完成）
                    # 断开临时链接
                    predecessor.right = None
                    # 访问当前节点
                    result.append(current.val)
                    # 移动到右子节点
                    current = current.right
        
        return result  # 返回中序遍历结果


# 测试代码
def test_inorder_traversal():
    """
    测试二叉树中序遍历的功能
    """
    print("=== 二叉树中序遍历测试 ===")
    
    # 构建测试二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #
    # 中序遍历结果应该是: [4, 2, 5, 1, 3]
    
    # 创建节点
    root = TreeNode(1)           # 根节点
    root.left = TreeNode(2)      # 左子节点
    root.right = TreeNode(3)     # 右子节点
    root.left.left = TreeNode(4) # 左子节点的左子节点
    root.left.right = TreeNode(5) # 左子节点的右子节点
    
    # 创建解决方案实例
    solution = Solution()
    
    # 测试递归方法
    recursive_result = solution.inorderTraversal(root)
    print(f"递归方法结果: {recursive_result}")
    
    # 测试函数式递归方法
    functional_result = solution.inorderTraversal_functional(root)
    print(f"函数式递归方法结果: {functional_result}")
    
    # 测试迭代方法
    iterative_result = solution.inorderTraversal_iterative(root)
    print(f"迭代方法结果: {iterative_result}")
    
    # 测试 deque 迭代方法
    deque_result = solution.inorderTraversal_iterative_deque(root)
    print(f"deque 迭代方法结果: {deque_result}")
    
    # 测试 Morris 遍历方法
    morris_result = solution.inorderTraversal_morris(root)
    print(f"Morris 遍历方法结果: {morris_result}")
    
    # 验证五种方法结果是否一致
    if recursive_result == functional_result == iterative_result == deque_result == morris_result == [4, 2, 5, 1, 3]:
        print("✅ 测试通过！五种方法都得到了正确的中序遍历结果")
    else:
        print("❌ 测试失败！结果不正确")
    
    print("\n=== 空树测试 ===")
    # 测试空树情况
    empty_result = solution.inorderTraversal(None)
    empty_result_func = solution.inorderTraversal_functional(None)
    empty_result_iter = solution.inorderTraversal_iterative(None)
    empty_result_deque = solution.inorderTraversal_iterative_deque(None)
    empty_result_morris = solution.inorderTraversal_morris(None)
    print(f"空树递归结果: {empty_result}")
    print(f"空树函数式递归结果: {empty_result_func}")
    print(f"空树迭代结果: {empty_result_iter}")
    print(f"空树 deque 迭代结果: {empty_result_deque}")
    print(f"空树 Morris 遍历结果: {empty_result_morris}")
    
    if empty_result == empty_result_func == empty_result_iter == empty_result_deque == empty_result_morris == []:
        print("✅ 空树测试通过！")
    else:
        print("❌ 空树测试失败！")
    
    print("\n=== 单节点树测试 ===")
    # 测试单节点树
    single_node = TreeNode(10)
    single_recursive = solution.inorderTraversal(single_node)
    single_functional = solution.inorderTraversal_functional(single_node)
    single_iterative = solution.inorderTraversal_iterative(single_node)
    single_deque = solution.inorderTraversal_iterative_deque(single_node)
    single_morris = solution.inorderTraversal_morris(single_node)
    print(f"单节点递归结果: {single_recursive}")
    print(f"单节点函数式递归结果: {single_functional}")
    print(f"单节点迭代结果: {single_iterative}")
    print(f"单节点 deque 迭代结果: {single_deque}")
    print(f"单节点 Morris 遍历结果: {single_morris}")
    
    if single_recursive == single_functional == single_iterative == single_deque == single_morris == [10]:
        print("✅ 单节点树测试通过！")
    else:
        print("❌ 单节点树测试失败！")
    
    print("\n=== 左斜树测试 ===")
    # 测试左斜树（所有节点只有左子节点）
    #       1
    #      /
    #     2
    #    /
    #   3
    left_skew = TreeNode(1)
    left_skew.left = TreeNode(2)
    left_skew.left.left = TreeNode(3)
    
    left_recursive = solution.inorderTraversal(left_skew)
    left_functional = solution.inorderTraversal_functional(left_skew)
    left_iterative = solution.inorderTraversal_iterative(left_skew)
    left_deque = solution.inorderTraversal_iterative_deque(left_skew)
    left_morris = solution.inorderTraversal_morris(left_skew)
    print(f"左斜树递归结果: {left_recursive}")
    print(f"左斜树函数式递归结果: {left_functional}")
    print(f"左斜树迭代结果: {left_iterative}")
    print(f"左斜树 deque 迭代结果: {left_deque}")
    print(f"左斜树 Morris 遍历结果: {left_morris}")
    
    if left_recursive == left_functional == left_iterative == left_deque == left_morris == [3, 2, 1]:
        print("✅ 左斜树测试通过！")
    else:
        print("❌ 左斜树测试失败！")
    
    print("\n=== 右斜树测试 ===")
    # 测试右斜树（所有节点只有右子节点）
    #       1
    #        \
    #         2
    #          \
    #           3
    right_skew = TreeNode(1)
    right_skew.right = TreeNode(2)
    right_skew.right.right = TreeNode(3)
    
    right_recursive = solution.inorderTraversal(right_skew)
    right_functional = solution.inorderTraversal_functional(right_skew)
    right_iterative = solution.inorderTraversal_iterative(right_skew)
    right_deque = solution.inorderTraversal_iterative_deque(right_skew)
    right_morris = solution.inorderTraversal_morris(right_skew)
    print(f"右斜树递归结果: {right_recursive}")
    print(f"右斜树函数式递归结果: {right_functional}")
    print(f"右斜树迭代结果: {right_iterative}")
    print(f"右斜树 deque 迭代结果: {right_deque}")
    print(f"右斜树 Morris 遍历结果: {right_morris}")
    
    if right_recursive == right_functional == right_iterative == right_deque == right_morris == [1, 2, 3]:
        print("✅ 右斜树测试通过！")
    else:
        print("❌ 右斜树测试失败！")


def performance_analysis():
    """
    性能分析函数，比较三种遍历方法的性能
    """
    import time
    import random
    
    print("\n=== 性能分析 ===")
    
    # 创建一个较大的二叉树用于性能测试
    # 这里我们创建一个平衡二叉搜索树
    def create_balanced_bst(values):
        if not values:
            return None
        
        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = create_balanced_bst(values[:mid])
        root.right = create_balanced_bst(values[mid+1:])
        return root
    
    # 生成随机值并排序，用于创建平衡二叉搜索树
    num_nodes = 1000
    values = sorted([random.randint(1, 10000) for _ in range(num_nodes)])
    root = create_balanced_bst(values)
    
    solution = Solution()
    
    # 测试递归方法性能
    start_time = time.time()
    recursive_result = solution.inorderTraversal(root)
    recursive_time = time.time() - start_time
    print(f"递归方法耗时: {recursive_time:.6f} 秒")
    
    # 测试函数式递归方法性能
    start_time = time.time()
    functional_result = solution.inorderTraversal_functional(root)
    functional_time = time.time() - start_time
    print(f"函数式递归方法耗时: {functional_time:.6f} 秒")
    
    # 测试迭代方法性能
    start_time = time.time()
    iterative_result = solution.inorderTraversal_iterative(root)
    iterative_time = time.time() - start_time
    print(f"迭代方法耗时: {iterative_time:.6f} 秒")
    
    # 测试 deque 迭代方法性能
    start_time = time.time()
    deque_result = solution.inorderTraversal_iterative_deque(root)
    deque_time = time.time() - start_time
    print(f"deque 迭代方法耗时: {deque_time:.6f} 秒")
    
    # 测试 Morris 遍历方法性能
    start_time = time.time()
    morris_result = solution.inorderTraversal_morris(root)
    morris_time = time.time() - start_time
    print(f"Morris 遍历方法耗时: {morris_time:.6f} 秒")
    
    # 验证结果是否一致
    if recursive_result == functional_result == iterative_result == deque_result == morris_result:
        print("✅ 所有方法结果一致")
    else:
        print("❌ 方法结果不一致")
    
    # 创建一个左斜树（最坏情况）
    left_skew_root = TreeNode(0)
    current = left_skew_root
    for i in range(1, num_nodes):
        current.left = TreeNode(i)
        current = current.left
    
    print("\n=== 左斜树性能分析（最坏情况）===")
    
    # 测试递归方法性能
    start_time = time.time()
    recursive_result = solution.inorderTraversal(left_skew_root)
    recursive_time = time.time() - start_time
    print(f"递归方法耗时: {recursive_time:.6f} 秒")
    
    # 测试函数式递归方法性能
    start_time = time.time()
    functional_result = solution.inorderTraversal_functional(left_skew_root)
    functional_time = time.time() - start_time
    print(f"函数式递归方法耗时: {functional_time:.6f} 秒")
    
    # 测试迭代方法性能
    start_time = time.time()
    iterative_result = solution.inorderTraversal_iterative(left_skew_root)
    iterative_time = time.time() - start_time
    print(f"迭代方法耗时: {iterative_time:.6f} 秒")
    
    # 测试 deque 迭代方法性能
    start_time = time.time()
    deque_result = solution.inorderTraversal_iterative_deque(left_skew_root)
    deque_time = time.time() - start_time
    print(f"deque 迭代方法耗时: {deque_time:.6f} 秒")
    
    # 测试 Morris 遍历方法性能
    start_time = time.time()
    morris_result = solution.inorderTraversal_morris(left_skew_root)
    morris_time = time.time() - start_time
    print(f"Morris 遍历方法耗时: {morris_time:.6f} 秒")
    
    # 验证结果是否一致
    if recursive_result == functional_result == iterative_result == deque_result == morris_result:
        print("✅ 所有方法结果一致")
    else:
        print("❌ 方法结果不一致")


# 如果直接运行此文件，则执行测试
if __name__ == "__main__":
    test_inorder_traversal()
    performance_analysis()
