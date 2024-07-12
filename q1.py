class Solution: 
        def minSubsequence(self, source: str, target: str) -> int:
                count = 0
                # pointer for target
                i = 0
                
                while i < len(target):
                        # pointer for source
                        j = 0
                        while j < len(source) and i < len(target):
                                # If found matched char, move i backwards by 1
                                if source[j] == target[i]:
                                       i += 1
                                # If not continue loop source string
                                j += 1

                                # If counter is greater than len(target) and source[j] not equal to target[i]
                                # mains cannot be constructed, return -1
                                if count > len(target) and source[j] != target[i]:
                                        return -1
                        count += 1
                return count
                        
def test():
        solution = Solution()

        src1 = "abc"
        tar1 = "abcbc"
        exp1 = 2
        assert solution.minSubsequence(src1, tar1) == exp1 

        src2 = "xyz"
        tar2 = "xzyxz"
        exp2 = 3
        assert solution.minSubsequence(src2, tar2) == exp2         
        
        src3 = "abc"
        tar3 = "acdbc"
        exp3 = -1
        assert solution.minSubsequence(src3, tar3) == exp3 

        print("All test passed!!!")

if __name__ == "__main__": 
        test()