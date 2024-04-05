statevotes = {}
voting = {}

with open('input.txt', 'r') as f:
    for _ in range(int(f.readline())):
        state, electcnt = f.readline().rstrip().split()

        if state not in statevotes:
            statevotes[state] = electcnt


    while True:
        q = f.readline().strip().split()
        if not q:
            break

        vstate, candidate = q
        
        if vstate not in voting:
            voting[vstate] = {}

        if not voting[vstate].get(candidate):
            voting[vstate][candidate] = 0
        
        voting[vstate][candidate] += 1

winners = {}

for kstate, results in voting.items():
    voting[kstate] = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))

    cands = 0
    for cand, vts in voting[kstate].items():
        if cand not in winners:
            winners[cand] = 0
        winners[cand] += int(statevotes.get(kstate))
        if cands > 0:
            winners[cand] -= int(statevotes.get(kstate))
        cands += 1

for k, v in dict(sorted(winners.items(), key=lambda x: (-int(x[1]), x[0]))).items():
    print(k, v)