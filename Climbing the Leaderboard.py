def climbingLeaderboard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse=True)
    ascores = []
    alice.sort(reverse=True)
    j = 0 
    for i in range(len(alice)):
        while j < len(scores) and alice[i]< scores[j]:
            j += 1
        ascores.append(j+1)
    #ascores[-1] += 1

    return ascores[::-1]
    


s = [100 , 100, 50, 40, 40, 10] 
a = [5, 25, 50, 120]
print(climbingLeaderboard(s,a))
