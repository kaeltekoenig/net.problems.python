def unfold_list(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))


n, m = 7, 7

array = [[c * (c - r == 0)
          for c in range(m)] 
          for r in range(n)]


unfold_list(array)




# n = 7
# matrix = [[0 for _ in range(n)] for _ in range(n)]
 
# counter = 0
# for r in range(n):
#     for c in range(n-r):
#         matrix[c][c+r] = counter
#         counter += 1
 
# for line in matrix:
#     print(" ".join([f"{el:>2}" for el in line]))
