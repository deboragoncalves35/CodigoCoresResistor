def IEC60062(str):
    # Dicionario de cores, ordem e tolerância
    dict_cores = {
        -3 : 'Rosa',
        -2 : 'Prata',
        -1 : 'Dourada',
         0 : 'Preta',
         1 : 'Marrom',
         2 : 'Vermelha',
         3 : 'Laranja',
         4 : 'Amarela',
         5 : 'Verde',
         6 : 'Azul',
         7 : 'Violeta',
         8 : 'Cinza',
         9 : 'Branca'
    }

    dict_ordem = {
        'm' : -3,
        '-' : 0,
        'K' : 3,
        'M' : 6,
        'G' : 9
    }

    dict_tolerancia = {
          10 : 'Prata',
           5 : 'Dourada',
           1 : 'Marrom',
           2 : 'Vermelha',
        0.05 : 'Laranja',
        0.02 : 'Amarela',
         0.5 : 'Verde',
        0.25 : 'Azul',
         0.1 : 'Violeta',
        0.01 : 'Cinza'
    }

    # Separa a string em uma lista de caracteres
    letras = list(str) 
    cores = []

    # Substrings que serão identificadas na string recebida como parâmetro
    F = ""
    M = ""
    T = ""

    # Lista de multiplicadores possiveis
    multiplicadores = ['m', '-', 'K', 'M', 'G']
    i = 0

    # Percorre a string
    for i in range(len(str)):
        # Copia caractere M
        if letras[i] in multiplicadores:
            M += letras[i]
            break;
        
        # Copia caracteres de F
        F += letras[i]

    # i ainda contém a posição do caractere M, então adiciona 2
    # para mover para o primeiro char de T
    i += 2

    # Copia caracteres de T
    while(i < len(str)):
        T += letras[i]
        i += 1

    #######################################################################
    # Insere as cores que correspondem aos números de F, ao mesmo tempo,
    # determina a ordem da resistência
    ehDecimal = False

    ordem = dict_ordem.get(M) # Identificamos a ordem do multiplicador M
 
    # Percorre os caracteres da substring F
    for char in list(F):
        # Se o char atual é um ponto, então entramos na parte decimal do numero
        if(char == '.'):
            ehDecimal = True
        else:
            # Caso contrario, a descobrimos qual cor corresponde o char
            cor = dict_cores.get(int(char))

            # E a adicionamos na lista de cores
            cores.append(cor)
            
            # Se estamos na parte decimal, decrementamos a ordem
            if(ehDecimal):
                ordem -= 1

    # Se o numero F tiver apenas uma ordem decimal, adicionamos um zero e
    # diminuimos a ordem
    if len(F) == 1:
        cor = dict_cores.get(0)
        cores.append(cor)
        ordem -= 1

    # Agora podemos adicionar a cor correspondente à ordem
    cor = dict_cores.get(ordem)
    cores.append(cor)

    # Finalmente, adicionamos a cor correspondente à tolerância, apenas se a 
    # mesma for diferente de 20
    if(float(T) != 20):
        cor = dict_tolerancia.get(float(T))
        cores.append(cor)

    # Retorna a lista de cores calculada
    return cores
