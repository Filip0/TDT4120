from sys import stdin,stderr 

def beste_sti(nm, sans):
    n = len(nm)
    results = [0]*n
    visited = [0]*n
    results[0] = sans[0]
    for i in range(n):
        for j in range(len(nm[i])):
            if nm[i][j] == 1:
                if results[j] < (results[i]*sans[j]):
                    results[j] = (results[i]*sans[j])
                    print("Result: " + str(j) + " satt til: " + str(results[i]*sans[j] ))
                    visited[j] = i
    print(results)
    print(visited)
    if results[len(results)-1] == 0:
        return 0
    end = n-1
    path = []
    while 1:
        path.append(end)
        if end == 0: break
        end = visited[end]
    path.reverse()
    return "-".join(str(y) for y in path)

n = int(stdin.readline())
sansynligheter = [float(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [0] * n
    naboer = [int(nabo) for nabo in linje.split()]
    for nabo in naboer:
        naborad[nabo] = 1
    nabomatrise.append(naborad)
print beste_sti(nabomatrise, sansynligheter)