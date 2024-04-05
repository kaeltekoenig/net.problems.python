f = open('input.txt')
nums = list(map(int, f.read().split()))
o = open('output.txt', 'w')
o.write(str(sum(nums)))