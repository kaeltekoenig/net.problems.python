def unfold_array(lst):
    for rw in lst:
        print(' '.join(map(lambda el: str(el).rjust(4), rw)))





n, m = 5, 6
array = [[
    ((c + m * r + 1 * (r % 2 == 0)) // 2) * ((c + r) % 2 != 0)
    for c in range(1, m+1)] 
    for r in range(n)]


unfold_array(array)