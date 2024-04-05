def unfold_array(lst):
    for rw in lst:
        print(' '.join(map(lambda el: str(el).rjust(4), rw)))





n, m = 8, 8

array = [[
    max(r, c) if (r < n // 2 and c < m // 2) 
    else max((n - 1) % r, c) if (r >= n // 2 and c < m // 2)
    else max(r, (n - 1) % c) if (r < n // 2 and c >= m // 2)
    else max((n - 1) % r, (n - 1) % c) if (r >= n // 2 and c >= m // 2)


    else 9
    for c in range(0, m)] 
    for r in range(n)]


unfold_array(array)