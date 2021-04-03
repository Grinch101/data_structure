# merge sort:

# The divide-and-conquer paradigm involves three steps at each level of the recursion:
# Divide the problem into a number of subproblems that are smaller instances of the
# same problem.
# Conquer the subproblems by solving them recursively. If the subproblem sizes are
# small enough, however, just solve the subproblems in a straightforward manner.
# Combine the solutions to the subproblems into the solution for the original problem.
# The merge sort algorithm closely follows the divide-and-conquer paradigm. Intuitively,
# it operates as follows.
# Divide: Divide the n-element sequence to be sorted into two subsequences of n=2
# elements each.
# Conquer: Sort the two subsequences recursively using merge sort.
# Combine: Merge the two sorted subsequences to produce the sorted answer.
# The recursion “bottoms out” when the sequence to be sorted has length 1, in which
# case there is no work to be done, since every sequence of length 1 is already in
# sorted order.
# The key operation of the merge sort algorithm is the merging of two sorted
# sequences in the “combine” step.

# The recursion tree has lg n C 1 levels, each costing cn,
# for a total cost of cn.lg n C 1/ D cn lg n C cn. Ignoring the low-order term and
# the constant c gives the desired result of ‚.n lg n/.



def merge_sort( arr):
    if len(arr) >= 2:

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = idx = 0
        while True:
            if left[i] <= right[j]:
                arr[idx] = left[i]
                idx += 1
                i += 1
                if i == len(left):
                    break
            else:
                arr[idx] = right[j]
                idx += 1
                j += 1
                if j == len(right):
                    break

        # put extra item(s) in arr
        while i < len(left):
            arr[idx] = left[i]
            idx += 1
            i += 1
        while j < len(right):
            arr[idx] = right[j]
            idx += 1
            j += 1
    return arr

# # test:
# mg = merge_sort([9, 6, 4, 2, 0, 3, 1, 7, 8])
# print(mg)
