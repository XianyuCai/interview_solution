class Solution:
        def check_brackets(self, s: str) -> str:
                stack = []
                result = [' '] * len(s)
                for i, char in enumerate(s):
                        if char == '(':
                                stack.append(i)

                        elif char == ')':
                                if stack:
                                        stack.pop()
                                else:
                                        result[i] = '?'

                        
                while stack:
                        result[stack.pop()] = 'x'
                return ''.join(result)
        
def test():
    solution = Solution()

    # Test case 1
    input1 = "bge)))))))))"
    exp1 =   "   ?????????"

    assert solution.check_brackets(input1) == exp1


    # Test case 2
    input2 = "((IIII))))))"
    exp2 =   "        ????"

    assert solution.check_brackets(input2) == exp2

    # Test case 3
    input3 = "()()()()(uuu"
    exp3 =   "        x   "

    assert solution.check_brackets(input3) == exp3

    # Test case 4
    input4 = "))))UUUU((()"
    exp4 =   "????    xx  "
    assert solution.check_brackets(input4) == exp4

    # Test case 5 (balanced brackets)
    input5 = "((()))"
    exp5 = "      "
    assert solution.check_brackets(input5) == exp5

    # Test case 6 (only left brackets)
    input6 = "(("
    exp6 = "xx"
    assert solution.check_brackets(input6) == exp6

    # Test case 7 (only right brackets)
    input7 = "))"
    exp7 = "??"
    assert solution.check_brackets(input7) == exp7

    # Test case 8 (mixed with other characters)
    input8 = "a(b)c)d(e"
    exp8 =   "     ? x "
    assert solution.check_brackets(input8) == exp8

    # Test case 9 (empty string)
    input9 = ""
    exp9 = ""
    assert solution.check_brackets(input9) == exp9

    print("All tests passed!!!")

if __name__ == "__main__":
        test()