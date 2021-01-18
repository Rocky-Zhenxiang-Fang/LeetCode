from DS import TreeNode


def tribonacci(n):
    ans = tri_helper(n)
    return ans[0]


def tri_helper(n):
    if n == 0:
        return [0, 0, 0]
    elif n == 1:
        return [1, 0, 0]
    elif n == 2:
        return [1, 1, 0]
    else:
        ans = tri_helper(n - 1)
        return [sum(ans), ans[0], ans[1]]


if __name__ == '__main__':
    n = 5
    print(tribonacci(n))
