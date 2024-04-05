def unfold_array(lst):
    for rw in lst:
        print(' '.join(map(lambda el: str(el).rjust(4), rw)))





n, m = 6, 9
array = [[0 if (r == 0 or r == n - 1 or c == 0 or c == m - 1) 
          else 1 if r == 1 or c == 1 or r == n - 2 or c == m - 2 else 2
    for c in range(0, m)] 
    for r in range(n)]


unfold_array(array)