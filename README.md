# Codigo Cores em Resistor

Este projeto em Python é uma aplicação prática do padrão IEC 60062 para a codificação das cores de resistores.
O objetivo é decodificar as cores presentes no resistor e obter seu valor de resistência e tolerância correspondentes.

### Uso:
O programa recebe uma string no formato "", como por exemplo "13M 2%", como entrada. 
O valor da resistência e a tolerância devem estar separados por um espaço.

A saída é uma lista de strings que representa as cores das faixas do resistor

### Dicionarios:
Os dicionários usados no script:

* *dict_cores = { -3 : 'Rosa', -2 : 'Prata',-1 : 'Dourada', 0 : 'Preta',1 : 'Marrom',2 : 'Vermelha',3 : 'Laranja', 4 : 
              'Amarela', 5 : 'Verde', 6 : 'Azul', 7 : 'Violeta', 8 : 'Cinza', 9 : 'Branca' }*

* *dict_ordem = {'m' : -3, '-' : 0, 'K' : 3, 'M' : 6, 'G' : 9 }*

* *dict_tolerancia = { 10 : 'Prata', 5 : 'Dourada', 1 : 'Marrom', 2 : 'Vermelha', 0.05 : 'Laranja', 0.02 : 'Amarela',
                    0.5 : 'Verde',  0.25 : 'Azul', 0.1 : 'Violeta', 0.01 : 'Cinza' }*

### Função IEC60062
A função principal IEC60062 recebe a string do resistor e a decodifica em relação às cores das suas bandas. 
Inicialmente, a função separa a string de entrada em valor de resistência e tolerância. Em seguida, realiza o processamento do valor da resistência para obter as cores correspondentes usando os dicionários previamente definidos.
Da mesma forma, a tolerância é processada e sua cor correspondente é obtida.
O resultado final consiste em uma lista de strings que representa as cores das bandas do resistor.

### Conclusão
Esse projeto apresenta uma abordagem simplificada para decodificar as cores de um resistor e obter seu valor de resistência e tolerância.
Ele adere ao padrão IEC 60062 e utiliza dicionários para associar números e caracteres às cores correspondentes.
