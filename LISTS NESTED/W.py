def unfold_array(lst):
    for rw in lst:
        print(' '.join(map(lambda el: str(el).rjust(4), rw)))





n, m = 7, 7

array = [[
    c + r if (r < n // 2 + 1 * (n % 2 != 0) and c < m // 2  + 1 * (m % 2 != 0)) 
    else (n - 1) % r + c if (r >= n // 2 + 1 * (n % 2 != 0) and c < m // 2 + 1 * (m % 2 != 0))
    else r + (n - 1) % c if (r < n // 2 + 1 * (n % 2 != 0) and c >= m // 2 + 1 * (m % 2 != 0))
    else (n - 1) % r + (n - 1) % c if (r >= n // 2 + 1 * (n % 2 != 0) and c >= m // 2 + 1 * (m % 2 != 0))


    else 9
    for c in range(0, m)] 
    for r in range(n)]


unfold_array(array)