from sys import stdin
from itertools import repeat

def merge(decks):
    a = decks[0]
    for i in range(1,len(decks)):
        c = a
        a = []
        b = decks[i]
        while c and b:
            if c[0][0] < b[0][0]:
                a.append(c[0])
                c.pop(0)
            else:
                a.append(b[0])
                b.pop(0)
        if c:
            for value in c:
                a.append(value)
        if b:
            for value in b:
                a.append(value)
    string = ""
    for value in a:
        string = string + value[1]
        
    return string
           
decks = []
for line in stdin:
    (index, list) = line.split(':')
    deck = zip(map(int, list.split(',')), repeat(index))
    decks.append(deck)
print merge(decks)
