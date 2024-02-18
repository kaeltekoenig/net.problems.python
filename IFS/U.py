amin = int(input())
amax = int(input())
bmin = int(input())
bmax = int(input())


if amin > amax:
    amin, amax = amax, amin
if bmin > bmax:
    bmin, bmax = bmax, bmin

if (amin + amax) > (bmin + bmax):
    amin, amax = bmin, bmax

if amax < bmin:
    print(0)
else:
    print(amax - bmin)