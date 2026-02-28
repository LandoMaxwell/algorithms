def longest_palindrome(s: str) -> str:
    """
    找到字符串中最长的回文子串
    
    Args:
        s: 输入字符串
        
    Returns:
        最长的回文子串
    """
    if not s or len(s) < 1:
        return ""
    
    start = 0
    end = 0
    
    for i in range(len(s)):
        # 奇数长度的回文子串（以当前字符为中心）
        len1 = expand_from_center(s, i, i)
        # 偶数长度的回文子串（以当前字符和下一个字符之间为中心）
        len2 = expand_from_center(s, i, i + 1)
        
        # 取两种情况中的较大值
        max_len = max(len1, len2)
        
        # 如果找到了更长的回文子串，更新起始和结束位置
        if max_len > end - start + 1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

def expand_from_center(s: str, left: int, right: int) -> int:
    """
    从中心向两边扩展，返回回文子串的长度
    
    Args:
        s: 输入字符串
        left: 左边界索引
        right: 右边界索引
        
    Returns:
        回文子串的长度
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    # 返回回文子串的长度
    return right - left - 1

def test_longest_palindrome():
    """
    测试函数
    """
    test_cases = [
        ("babad", ["bab", "aba"]),  # 两种可能的结果
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
        ("", [""]),
        ("racecar", ["racecar"]),
        ("abccba", ["abccba"]),
        ("forgeeksskeegfor", ["geeksskeeg"]),
        ("abacdfgdcaba", ["aba"]),
    ]
    
    for i, (input_str, expected_results) in enumerate(test_cases):
        result = longest_palindrome(input_str)
        if result in expected_results:
            print(f"测试用例 {i+1} 通过: 输入 '{input_str}', 输出 '{result}'")
        else:
            print(f"测试用例 {i+1} 失败: 输入 '{input_str}', 期望 {expected_results}, 得到 '{result}'")

if __name__ == "__main__":
    # 运行测试
    test_longest_palindrome()
    
    # 交互式测试
    print("\n请输入一个字符串来查找最长回文子串:")
    try:
        user_input = input().strip()
        result = longest_palindrome(user_input)
        print(f"最长回文子串是: '{result}'")
    except EOFError:
        # 在非交互式环境中运行时的默认测试
        print("检测到非交互式环境，使用默认测试用例:")
        test_str = "babad"
        result = longest_palindrome(test_str)
        print(f"输入: '{test_str}'")
        print(f"最长回文子串是: '{result}'")