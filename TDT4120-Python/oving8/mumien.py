from sys import stdin

def beste_sti(nm, sans):
    # SKRIV DIN KODE HER
    v = nm
    results = []
    previous = []
    for x in range(nm):
        results[x] = 0
    print results
    for vertex in v:
        
    
    

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