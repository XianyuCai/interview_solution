def generate_all_subsequences(seq):
    n = len(seq)
    subsequences = []
    
    for i in range(1 << n): 
        subsequence = []
        for j in range(n):

            if (i & (1 << j)) > 0:
                subsequence.append(seq[j])
                # print("i:", bin(i)[2:], "j:", bin(1 << j)[2:], "|", j)
        if subsequence:
            subsequences.append(subsequence)
    
    return subsequences

def find_max_val(arr):
    max_val = float('-inf')
    for a in arr:
        median = 0
        length = len(a)

        if length % 2 == 1:
            median = a[length // 2]
        else:
            median = (a[length // 2 - 1] + a[length // 2]) / 2
        mean = sum(a) / length;
        max_val = max(max_val, mean - median)
    return max_val
            



seq = [1, 3, 5, 9]
all_subsequences = generate_all_subsequences(seq)
result = find_max_val(all_subsequences)
print(result)
