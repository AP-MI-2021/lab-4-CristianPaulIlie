def citireLista():
    lst = []
    givenString = input("Dati lista cu elemente separate prin virgula: ")
    numberAsString = givenString.split(" ")
    for x in numberAsString:
        lst.append(int(x))
    return lst

def printMenu():
    print("1. Citire lista")
    print("2. Afisarea numarului obtinut prin concatenarea tuturor elementelor pozitive din lista")
    print("3. Afisarea sumei dintre cel mai mic si cel mai mare numar din lista")
    print("4. Afisarea listei cu numere care au suma cifrelor mai mare sau egala cu un numar citit de la tastatura")
    print("5. Afisare lista")
    print("6 Ieșire")


def concatenarenumerepozitive(lst):
    '''
    Determina numarul obtinut prin concatenarea tuturor elementelor pozitive din lista
    param: lst, lista de intregi 
    return: nr, numarul obtinut
    '''
    nr = None
    for x in range(len(lst)):
        if x > 0:
            nr = str(nr) + str(x)
    return int(nr)


def testconcatenarenumerepozitive():
    assert concatenarenumerepozitive([0, 8, 23, -13, 25]) == 82325
    assert concatenarenumerepozitive([17, -9, 3, -5, 78]) == 17378
    assert concatenarenumerepozitive([0, -65, -56, -9]) is None


def sumaDintreMinsiMax(lst):
    '''
       Determina suma dintre cel mai mare si cel mai mic numar din lista
       param: lst, lista de intregi
       return: sum, suma obtinuta, nr intreg
       '''
    sum = min(lst) + max(lst)
    return sum


def testsumaDintreMinsiMax():
    assert sumaDintreMinsiMax([10, -3, 25, -1, 3, 25, 18]) == 22
    assert sumaDintreMinsiMax([13, 5, -2, -15, 30]) == 15
    assert sumaDintreMinsiMax([14, 16, 4, 13, 10]) == 20


def sumaCifrelor(x):
    '''
        Determina suma cifrelor lui x
        param: x, numar intreg
        return: s, suma cifrelor lui x
     '''
    while x:
        s = s + x % 10
        x = x/10
    return s


def testsumaCifrelor():
    assert sumaCifrelor(25) == 7
    assert sumaCifrelor(3) == 3
    assert sumaCifrelor(134) == 8


def sumaCifrelorMaiMareSauEgalaCuK(lst, k):
    '''
           Determina numerele care au suma cifrelor mai mare sau egala cu K
           param: lst, lista de intregi si k, un numar intreg
           return: rezultat, lista de intregi
           '''
    rezultat = []
    for x in range(len(lst)):
        if sumaCifrelor(x) >= k:
            rezultat.append(x)
    return rezultat


def testsumaCifrelorMaiMareSauEgalaCuK():
    assert sumaCifrelorMaiMareSauEgalaCuK([0, 8, 23, -13, 75], 9) == [75]
    assert sumaCifrelorMaiMareSauEgalaCuK([25, 11, 10, 24, 39], 7) == [25, 39]
    assert sumaCifrelorMaiMareSauEgalaCuK([10, -3, 25, -1, 3, 25, 18], -13) == [10, -3, 25, -1, 3, 25, 18]


def isperfectSquare(x):
    '''
          Determina daca un numar este patrat perfect
          param: x un numar intreg
          return:True daca e patrat perfect, False daca nu e 
    '''


def main():
    testconcatenarenumerepozitive()
    testsumaDintreMinsiMax()
    testsumaCifrelor()
    testsumaCifrelorMaiMareSauEgalaCuK()
    lst = []
    printMenu()
    while True:
        optiune = input("Dati optiune:  ")
            if optiune == "1":
                lst = citireLista()
            elif optiune == "2":
                print(concatenarenumerepozitive(lst))
            elif optiune == "3":
                print(sumaDintreMinsiMax(lst))
            elif optiune == "4":
                k = int(input("Dati numar: "))
                print(sumaCifrelorMaiMareSauEgalaCuK(lst, k))
            elif optiune == "5":
                break


main()
