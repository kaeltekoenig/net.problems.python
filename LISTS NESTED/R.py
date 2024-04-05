def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 12, 12
# array = [
#     [1 if c == r 
#      or (r % 2 == 0 and 0 < (c - r) < 2)
#      or (r % 2 == 1 and 0 < (r - c) < 2)
#      or c == n - r - 1
#      or (r % 2 == 0 and 0 < (n - c - r) < 3)
#      or (r % 2 == 0 and 0 < (r - c - n) < 3)
#      else 0
#      for c in range(m)] 
#      for r in range(n)]
array = [
    [1 if (c + r) % 4 < 2 and r % 4 == 0
     or (c + 4 * r) % 4 < 2 and r % 4 == 1
     or (c + r) % 4 < 2 and r % 4 == 2
     or (c + 2 * r) % 4 < 2 and r % 4 == 3
     else 0
     for c in range(m)] 
     for r in range(n)]


unfold_list(array)