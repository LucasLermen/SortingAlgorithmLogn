import matplotlib.pyplot as plt

#Tempo de execucao do Quick Sort em segundos para cada qtd de elementos

condicoes = [10,25,50,75,100,250,500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000]

dados = [0.000004,0.000017,0.000024,0.000011,0.000012,0.000127,
         0.000226,0.000290,0.000174,0.000419,0.002382 ,0.001559 ,
         0.001894,0.011295,0.014825,0.025722,0.025080]

#Criando grafico Geral insertionSort

plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,100000)
plt.ylim(0,0.1)
plt.title("Quick Sort : Tempo decorrido na ordenacao")
plt.plot(condicoes, dados, 'r')
plt.show()
