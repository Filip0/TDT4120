from sys import stdin

def sorter(A):
    # Merk: den sorterte lista ma returneres
    # SKRIV DIN KODE HER
    if len(A) <= 1:
        return A
    pivot = A.pop(len(A)/2)
    less = []
    greater = []
    for v in A:
        if v <= pivot:
            less.append(v)
        else:
            greater.append(v)
    return sorter(less)+[pivot]+sorter(greater)
    
    
    

def finn(A, nedre, ovre):
    low = 0
    high = 0
    
    while ovre-nedre>high-low:
        low = closest(A, nedre, False)
        high = closest(A, ovre, True)
        #print("Nedre: " + str(nedre) + " Low: " + str(low))
        #print("Ovre: " + str(ovre) + " High: " + str(high))
        if(nedre<A[0] and ovre>A[len(A)-1]):
            low = A[0]
            high = A[len(A)-1]
            break

    return [low,high]
    
        
def closest(A, i, high):
    l = 100000
    closest = i
    for x in A:
        if high and x>=i:
            diff = x-i
            if diff <= l and diff >= 0:
                l = diff
                closest = x
        elif not(high) and x<=i:
            diff = i-x
            if diff <= l and diff >= 0:
                l = diff
                closest = x
    return  closest 

    
        

liste = []
for x in stdin.readline().split():
    liste.append(int(x))

sortert = sorter(liste)
#print(sortert)
for linje in stdin:
    ord = linje.split()
    minst = int(ord[0])
    maks = int(ord[1])
    resultat = finn(sortert, minst, maks)
    print str(resultat[0]) + " " + str(resultat[1])
