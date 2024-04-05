def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 8, 8
array = [
    [1 if c > r and c < (n - r - 1) 
     else 2 if c > r and c > (n - r - 1) 
     else 3 if r > c and c > (n - r - 1) 
     else 4 if r > c 
     else 0
     for c in range(m)] 
     for r in range(n)]


unfold_list(array)