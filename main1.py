# This is a sample Python script.
import time

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
import pandas
import pygame
import plotly.express

#vetor de 100 mil zeros
a1 = numpy.zeros(100000)
#vetor de 100 mil uns
b1 = numpy.ones(100000)
# cria mil elementos que começam no 10 e termina no 1000
c1 = numpy.linspace(10, 1000, 1000)
a = numpy.random


#f string é uma versão moderna de string formatada
print(f'1 - Conteúdo da lista: {a1}, de tamanho {len(a1)}')
print(f'2 - Conteúdo da Lista: {b1}, de tamanho {len(b1)}')
print(f'3 - Conteúdo da Lista: {c1}, de tamanho {len(c1)}')

start_time = time.time()
a2 = numpy.zeros(1000000000, dtype='uint8')
end_time = time.time()
time_elapsed1 = end_time - start_time
print(f'Tempo decorrido para numpy array: {time_elapsed1}')

start_time2 = time.time()
a3 = [0] * 1000000000
end_time2 = time.time()
time_elapsed2 = end_time2 - start_time2
print(f'Tempo decorrido para array comum: {time_elapsed2}')

#vetores, matrizes e tensores
rng = numpy.random.default_rng() #cria a variável com os métodos random do numpy
vetor = rng.random(4)
print(f'Array de uma dimensão (vetor) randômico: \n{vetor}\n')
matriz = rng.random([4,4])
print(f'Array de duas dimensões (matriz) randômico: \n{matriz}\n')
tensor = rng.random([4,4,4])
print(f'Array de 3 dimensões (tensor) randômico: \n{tensor}\n')

#ordenar vetores
m_coluna = numpy.sort(matriz, axis=0) #axis=0 ordena pela coluna
m_linha = numpy.sort(matriz, axis=1) #axis=1 ordena pela linha
m_col_lin = numpy.sort(m_linha, axis=0) #aqui, ordena a ordenação por linha em coluna, ordenando a matriz em linha e coluna

print(f'ordenado por coluna \n{m_coluna}')
print(f'ordenado por linha \n{m_linha}')
print(f'ordenado por linha e coluna \n{m_col_lin}')

#ndarrays representados por gráficos
vetor_a = numpy.linspace(10, 1000, 100)
vetor_b = numpy.linspace(10, 3000, 100)
vetor_c = numpy.linspace(10, 8000, 100)

print(vetor_a)
print(vetor_b)
print(vetor_c)

#metodo para salvar em formato txt
numpy.savetxt('vetor_a.txt', vetor_a, fmt='%f', delimiter=';')
numpy.savetxt('vetor_b.txt', vetor_b, fmt='%f', delimiter=';')
numpy.savetxt('vetor_c.txt', vetor_c, fmt='%f', delimiter=';')


#plotando os gráficos
#carrega o vetores
array_a = numpy.loadtxt('vetor_a.txt', dtype=numpy.float64, delimiter=';')
array_b = numpy.loadtxt('vetor_b.txt', dtype=numpy.float64, delimiter=';')
array_c = numpy.loadtxt('vetor_c.txt', dtype=numpy.float64, delimiter=';')

#mostra o primeiro vetor
print(array_a)

#empilha os 3 arrays
array_abc = numpy.vstack([array_a, array_b, array_c])
print(array_abc)
#transpõe para o eixo x
array_abc = array_abc.transpose()
print(array_abc)
fig = plotly.express.line(array_abc)
fig.show()






