array = [[1, 2, 3,], [4, 5, 6]]

def arrange_table(data):
    return str(data).rjust(4)


def unfold_mlist(lst):
    for rw in lst:
       print(''.join(map(arrange_table, rw)))


def unfold_lmlist(lst):
    for rw in lst:
        print(''.join(map(lambda el: str(el).rjust(4), rw)))



unfold_lmlist(array)