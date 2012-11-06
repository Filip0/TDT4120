from sys import stdin, maxint

def korteste_rute(rekkefolge, nabomatrise, byer):
    # SKRIV DIN KODE HER
    print rekkefolge
    print nabomatrise
    print byer

testcases = int(stdin.readline())
for test in range(testcases):
    byer = int(stdin.readline())
    rekkefolge = [int(by) for by in stdin.readline().split()]
    nabomatrise = []
    #for by in range(byer):
    # SKRIV DIN KODE HER
        
    print korteste_rute(rekkefolge, nabomatrise, byer)