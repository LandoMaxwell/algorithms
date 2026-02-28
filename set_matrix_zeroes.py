def setZeroes(matrix):
    """
    给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。
    使用原地算法，不创建额外的矩阵。
    
    参数:
        matrix: List[List[int]] - 输入的二维矩阵
    """
    # 获取矩阵的行数和列数
    m = len(matrix)  # 矩阵的行数
    n = len(matrix[0])  # 矩阵的列数
    
    # 使用两个集合来记录需要置零的行和列
    zero_rows = set()  # 存储需要置零的行的索引
    zero_cols = set()  # 存储需要置零的列的索引
    
    # 第一次遍历：找出所有包含0的行和列
    for i in range(m):  # 遍历每一行
        for j in range(n):  # 遍历每一列
            if matrix[i][j] == 0:  # 如果当前元素为0
                zero_rows.add(i)  # 记录该行的索引
                zero_cols.add(j)  # 记录该列的索引
    
    # 第二次遍历：将记录的行和列全部置零
    for i in range(m):  # 遍历每一行
        for j in range(n):  # 遍历每一列
            # 如果当前行或当前列在需要置零的集合中
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0  # 将该元素置为0


def setZeroesOptimized(matrix):
    """
    优化版本：使用矩阵的第一行和第一列来标记需要置零的行和列
    空间复杂度为O(1)，真正的原地算法
    
    参数:
        matrix: List[List[int]] - 输入的二维矩阵
    """
    # 获取矩阵的行数和列数
    m = len(matrix)  # 矩阵的行数
    n = len(matrix[0])  # 矩阵的列数
    
    # 两个变量来标记第一行和第一列是否需要置零
    first_row_zero = False  # 标记第一行是否需要置零
    first_col_zero = False  # 标记第一列是否需要置零
    
    # 检查第一行是否需要置零
    for j in range(n):  # 遍历第一行的每个元素
        if matrix[0][j] == 0:  # 如果第一行有0
            first_row_zero = True  # 标记第一行需要置零
            break  # 找到一个0就可以退出循环
    
    # 检查第一列是否需要置零
    for i in range(m):  # 遍历第一列的每个元素
        if matrix[i][0] == 0:  # 如果第一列有0
            first_col_zero = True  # 标记第一列需要置零
            break  # 找到一个0就可以退出循环
    
    # 使用第一行和第一列来标记其他行和列是否需要置零
    for i in range(1, m):  # 从第二行开始遍历
        for j in range(1, n):  # 从第二列开始遍历
            if matrix[i][j] == 0:  # 如果当前元素为0
                matrix[i][0] = 0  # 用第一列标记该行需要置零
                matrix[0][j] = 0  # 用第一行标记该列需要置零
    
    # 根据第一行和第一列的标记，将对应的行和列置零
    for i in range(1, m):  # 从第二行开始遍历
        for j in range(1, n):  # 从第二列开始遍历
            # 如果第一列标记该行需要置零，或第一行标记该列需要置零
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0  # 将该元素置为0
    
    # 最后处理第一行和第一列
    if first_row_zero:  # 如果第一行需要置零
        for j in range(n):  # 遍历第一行的每个元素
            matrix[0][j] = 0  # 将第一行全部置零
    
    if first_col_zero:  # 如果第一列需要置零
        for i in range(m):  # 遍历第一列的每个元素
            matrix[i][0] = 0  # 将第一列全部置零


def printMatrix(matrix):
    """
    打印矩阵的辅助函数
    
    参数:
        matrix: List[List[int]] - 要打印的二维矩阵
    """
    for row in matrix:  # 遍历每一行
        print(row)  # 打印该行


# 测试代码
if __name__ == "__main__":
    # 测试用例1
    print("测试用例1:")
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("原始矩阵:")
    printMatrix(matrix1)
    setZeroes(matrix1)
    print("置零后的矩阵:")
    printMatrix(matrix1)
    
    print("\n测试用例2:")
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print("原始矩阵:")
    printMatrix(matrix2)
    setZeroesOptimized(matrix2)
    print("置零后的矩阵:")
    printMatrix(matrix2)
    
    print("\n测试用例3:")
    matrix3 = [
        [1, 2, 3, 4],
        [5, 0, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    print("原始矩阵:")
    printMatrix(matrix3)
    setZeroesOptimized(matrix3)
    print("置零后的矩阵:")
    printMatrix(matrix3)
