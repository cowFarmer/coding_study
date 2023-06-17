def solution(players, callings):
    player = {i:idx for idx, i in enumerate(players)}
    idx = {idx:i for idx, i in enumerate(players)}

    for i in callings:
        curIdx, preIdx = player[i], player[i]-1
        curPlayer, prePlayer = i, idx[preIdx]
        
        idx[curIdx], idx[preIdx] = prePlayer, curPlayer
        player[curPlayer], player[prePlayer] = preIdx, curIdx
        
    return list(idx.values())

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
solution(players, callings)