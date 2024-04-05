def xor(x, y):
    return not ((x and y) or (not x and not y))
        
print(xor(True, False))