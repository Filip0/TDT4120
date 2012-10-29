"""
I denne oevingen faar du gitt en graf, et sett med startnoder, og et sett med sluttnoder. 
Programmet ditt skal finne ut hvor mange stier det gaar an aa lage fra startnodene til sluttnoder 
uten at disse krysser. En sti fra en startnode kan gaa til hvilken som helst sluttnode, 
men forskjellige stier kan ikke moetes i samme sluttnode. For aa finne ut hvor mange stier 
det kan gaa gjennom en graf, maa du bruke maks flyt. Siden du i dette problemet har mange 
startnoder (sources) og mange sluttnoder (sinks), maa du lage en super-source med kant til 
alle startnoder, og en super-sink med kant fra all sluttnodene.

To stier som er innom samme node krysser. Det vil si at du maa tilordne en kapasitet til nodene. 
Dette kan du gjoere ved aa splitte nodene. For hver node v, lager du nodene v1 og v2. 
Saa lager du en kant fra v1 til v2. Hvis det gaar en kant fra u til v, lager du en kant fra u2 til v1, 
og hvis det gaar en kant fra v til w, lager du en kant fra v2 til w1. 
Da vil det ikke kunne gaa mer enn en flyt gjennom v. Sett bort fra dette oppfoerer v1 og v2 
seg til sammen som v gjorde i den opprinnelige grafen.

Foerste linje i input er antall noder, antall startnoder, og antall sluttnoder. 
Saa kommer en linje med alle startnodene, og en linje med alle sluttnodene. 
Deretter kommer en nabomatrise, hvor "1" betyr at det gaar en kant, og "0" betyr at det ikke gaar en kant. 
Programmet ditt skal skrive ut maksimalt antall stier fra startnoder til sluttnoder uten at 
noen av dem moetes i noen av nodene. 

Input-eksempel

6 2 2
0 1
4 5
0 0 1 0 0 0
0 0 0 1 0 0
0 0 0 0 0 1
0 0 0 0 1 1
0 0 0 0 0 0
0 0 0 0 0 0

Tilhoerende output

2

"""

from sys import stdin, stderr

# kapasiteter er den opprinnelige kapasitetsmatrisen, som inneholder n x n elementer (hvor n er antall noder).
# startrom er en liste med indeksene til nodene som tilsvarer startrommene.
# utganger er en liste med indeksene til nodene som tilsvarer utgangene.

def antallIsolerteStier(kapasiteter, startrom, utganger):
    # Du kan bruke metoden finnFlytsti for aa forenkle oppgaven.
    # SKRIV DIN KODE HER
    print(kapasiteter)
    print(startrom)
    print(utganger)

# Finner en sti fra noden med indeks 'kilde' til noden med indeks 'sluk'
# med ledig kapasitet i et flytnettverk med flyt F og kapasitet C.
# Returnerer en liste hvor foerste element er indeksen til en av startnodene, 
# siste element er indeksen til en av utgangene, og elementene imellom er 
# indeksene til de andre nodene paa veien som ble funnet, i riktig rekkefoelge.
# Eksempel: en sti fra startnoden 4 til node 3, node 9, node 7 og til slutt til 
# utgangen 12 vil representeres som [4, 3, 9, 7, 12].

def finnFlytsti(kilde, sluk, F, C):
    n = len(F)
    oppdaget = [False] * n
    forelder = [None] * len(F)
    koe = [kilde]
    while koe:
        node = koe.pop(0)
        if node == sluk:
            # Har funnet sluken, lager en array med passerte noder
            sti = []
            i = node
            while True:
                sti.append(i)
                if i == kilde:
                    break
                i = forelder[i]
            sti.reverse()
            return sti;
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                koe.append(nabo);
                oppdaget[nabo] = True;
                forelder[nabo] = node;
    return None

noder, _, _ = [int(x) for x in stdin.readline().split()]
startrom = [int(x) for x in stdin.readline().split()]
utganger = [int(x) for x in stdin.readline().split()]
nabomatrise = []
for linje in stdin:
    naborad = [int(nabo) for nabo in linje.split()]
    nabomatrise.append(naborad)
print antallIsolerteStier(nabomatrise, startrom, utganger)
