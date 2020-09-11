class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) < 2:
            return len(A)

        turbulent_size = max_size = 1
        prev_diff = 0
        start_idx = 0
        for i in range(1, len(A)):
            diff = A[i] - A[i-1]
            if diff == 0:
                max_size = max(max_size, turbulent_size)
                turbulent_size = 1
                start_idx = i
            elif start_idx == i-1 or (prev_diff < 0 and diff > 0) or (prev_diff > 0 and diff < 0):
                turbulent_size += 1
            else:
                max_size = max(max_size, turbulent_size)
                turbulent_size = 2
                start_idx = i-1

            prev_diff = diff

        return max(max_size, turbulent_size)


'''
Test Cases:
[9,4,2,10,7,8,8,1,9]
[9,4,8,10,7,8,1,9]
[4,8,12,16]
[8,8,8,8]
[100]
[]
'''
