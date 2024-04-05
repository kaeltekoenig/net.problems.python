def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


def max_number(a, b):
    return a * (a > b) + b * (a <= b)



n, m = 7, 7
array = [[1 if c == r or c == n - r - 1 else 0 for c in range(m)] for r in range(n)]


unfold_list(array)