def transfer(dct, clnt1, clnt2, val):
    if clnt1 not in dct:
        dct[clnt1] = 0
    if clnt2 not in dct:
        dct[clnt2] = 0

    dct[clnt1] -= val
    dct[clnt2] += val

def inout(dct, clnt, val):
    if clnt not in dct:
        dct[clnt] = 0
    dct[clnt] += val


clients = {}

with open('input.txt', 'r') as f:
    while True:
        q = f.readline().rstrip().split()

        if q:
            if q[0] == 'INCOME':
                for k, v in clients.items():
                    if v > 0:
                        clients[k] += int(v / 100 * int(q[1]))

            elif q[0] == 'DEPOSIT':
                inout(clients, q[1], int(q[2]))
            
            elif q[0] == 'WITHDRAW':
                inout(clients, q[1], -int(q[2]))

            elif q[0] == 'BALANCE':
                if q[1] not in clients:
                    print('ERROR')
                else:
                    print(clients[q[1]])
            
            elif q[0] == 'TRANSFER':
                transfer(clients, q[1], q[2], int(q[3]))
        else:
            break