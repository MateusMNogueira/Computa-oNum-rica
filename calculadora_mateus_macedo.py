print("Conversão de base, digite 1 e aperte enter e coloque da seguinte maneira (numero1,base1,base_desejada) \nMultiplicação de bases diferentes digite 2 e coloque (numero1,base1,numero2,base2,base_desejada) \nSoma digite 3 e coloque (numero1,base1,numero2,base2,base_desejada)")

valores = {
    "A": 10, "a": 10, "B": 11, "b": 11, "C": 12, "c": 12, "D": 13, "d": 13,
    "E": 14, "e": 14, "F": 15, "f": 15, "G": 16, "g": 16, "H": 17, "h": 17,
    "I": 18, "i": 18, "J": 19, "j": 19, "K": 20, "k": 20, "L": 21, "l": 21,
    "M": 22, "m": 22, "N": 23, "n": 23, "O": 24, "o": 24, "P": 25, "p": 25,
    "Q": 26, "q": 26, "R": 27, "r": 27, "S": 28, "s": 28, "T": 29, "t": 29,
    "U": 30, "u": 30, "V": 31, "v": 31, "W": 32, "w": 32, "X": 33, "x": 33,
    "Y": 34, "y": 34, "Z": 35, "z": 35
}

def base_10(n1, b1):
    lista_convertido = []
    lista = list(n1)
    for i in range(len(lista)):
        if lista[i].isdigit():
            lista_convertido.append(int(lista[i]))
        elif lista[i] in valores:
            lista_convertido.append(int(valores[lista[i]]))

    soma = 0
    for j in range(len(lista_convertido)):
        soma += lista_convertido[j] * (b1 ** (len(lista_convertido) - j - 1))

    return soma

def conversor(n1, b1, b2):
    lista = []
    lista_deci = []
    if "." in n1:
        n1, n1_deci = n1.split(".")
        n1 = base_10(n1, b1)
        n1_deci = decimal(n1_deci, b1)

        for _ in range(12):
            n1_deci *= b2
            inteiro = int(n1_deci)
            n1_deci -= inteiro
            if inteiro >= 10:
                for k, m in valores.items():
                    if m == inteiro:
                        lista_deci.append(k)
                        break
            else:
                lista_deci.append(str(inteiro))

        while n1 > 0:
            resto = n1 % b2
            n1 = n1 // b2
            if resto >= 10:
                for k, m in valores.items():
                    if m == resto:
                        lista.append(k)
                        break
            else:
                lista.append(str(resto))
        lista = lista[::-1]
        lista.append(".")
        lista += lista_deci

    else:
        n1 = int(n1, b1)
        while n1 > 0:
            resto = n1 % b2
            n1 = n1 // b2
            if resto >= 10:
                for k, m in valores.items():
                    if m == resto:
                        lista.append(k)
                        break
            else:
                lista.append(str(resto))

        lista = lista[::-1]

    return "".join(lista)

def decimal(n1, b1):
    lista_decimais = []
    lista = list(n1)

    for i in range(len(lista)):
        if lista[i].isdigit():
            lista_decimais.append(int(lista[i]))
        elif lista[i] in valores:
            lista_decimais.append(int(valores[lista[i]]))

    soma = 0

    for j in range(len(lista_decimais)):
        soma += lista_decimais[j] * (b1 ** -(j + 1))
    return soma

def somando(n1, b1, n2, b2, b3):
    if "." in n1:
        n1, n1_deci = n1.split(".")
        n1 = base_10(n1, b1)
        n1_deci = decimal(n1_deci, b1)
        n1 = n1 + n1_deci
    else:
        n1 = base_10(n1, b1)

    if "." in n2:
        n2, n2_deci = n2.split(".")
        n2 = base_10(n2, b2)
        n2_deci = decimal(n2_deci, b2)
        n2 = n2 + n2_deci
    else:
        n2 = base_10(n2, b2)

    soma = n1 + n2

    return conversor(str(soma), 10, b3)

def multiplicando(n1, b1, n2, b2, b3):
    if "." in n1:
        n1, n1_deci = n1.split(".")
        n1 = base_10(n1, b1)
        n1_deci = decimal(n1_deci, b1)
        n1 = n1 + n1_deci
    else:
        n1 = base_10(n1, b1)

    if "." in n2:
        n2, n2_deci = n2.split(".")
        n2 = base_10(n2, b2)
        n2_deci = decimal(n2_deci, b2)
        n2 = n2 + n2_deci
    else:
        n2 = base_10(n2, b2)

    n3 = n1 * n2

    return conversor(str(n3), 10, b3)

def Horner(n1, b1, b2):
    lista_Horner = []
    n1 = n1.split()
    for i in range(len(n1)):
        n1[i] = conversor(n1[i], b1, 10)
        lista_Horner.append(n1[i])

    soma = lista_Horner[0]

    for i in range(1, len(lista_Horner)):
        mult = multiplicando(soma, b2, str(b1), b2, b2)
        soma = somando(mult, b2, lista_Horner[i], b2, b2)
    return conversor(str(soma), 10, b2)

def conversao_base(n1, b1, b2):
    if "." in n1:
        lista = []
        n1, n1_deci = n1.split(".")
        n1 = Horner(n1, b1, b2)
        n1_deci = decimal(n1_deci, b1)
        for _ in range(12):
            n1_deci *= b2
            inteiro = int(n1_deci)
            n1_deci -= inteiro
            if inteiro >= 10:
                for k, m in valores.items():
                    if m == inteiro:
                        lista.append(k)
                        break
            else:
                lista.append(str(inteiro))

        return n1 + "." + "".join(lista)

    else:
        return Horner(n1, b1, b2)

n = int(input())

if n == 1:
    base = input().split(",")
    n1 = base[0]
    b1 = int(base[1])
    b2 = int(base[2])
    print(conversao_base(n1, b1, b2))

elif n == 2:
    mult = input().split(",")
    if len(mult) != 5:
        print("Erro de digitação")
    n1 = str(mult[0])
    b1 = int(mult[1])
    n2 = str(mult[2])
    b2 = int(mult[3])
    b3 = int(mult[4])
    print(multiplicando(n1, b1, n2, b2, b3))

elif n == 3:
    somar = input().split(",")
    if len(somar) != 5:
        print("Erro de digitação")
    n1 = str(somar[0])
    b1 = int(somar[1])
    n2 = str(somar[2])
    b2 = int(somar[3])
    b3 = int(somar[4])
    print(somando(n1, b1, n2, b2, b3))
else:
    print("Digite um número abaixo de 3")
    
    
    
    