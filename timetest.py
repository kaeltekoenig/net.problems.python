from time import time

##################
starttime = time()
##################
for i in range(1, 10 ** 4):
    for j in range(1, 10 ** 4):
        pass
##################
endtime = time()
print(f'Программа выполнена. Время работы: {round(endtime - starttime, 5)} сек.')