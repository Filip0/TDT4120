from sys import stdin, stderr
import traceback

class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    # SKRIV DIN KODE HER
    root = Node()
    current = root
    for word in ordliste:
        for letter in word[0]:
            node = Node()
            current.barn[(letter,word[1])] = node
            current = node
        current = root
            
        

def posisjoner(ord, indeks, node):
    # SKRIV DIN KODE HER


try:
    ord = stdin.readline().split()
    ordliste = []
    pos = 0
    for o in ord:
        ordliste.append( (o,pos) )
        pos += len(o) + 1
    toppnode = bygg(ordliste)
    for sokeord in stdin:
        sokeord = sokeord.strip()
        print sokeord + ":",
        posi = posisjoner(sokeord, 0, toppnode)
        posi.sort()
        for p in posi:
            print p,
        print
except:
    traceback.print_exc(file=stderr)
