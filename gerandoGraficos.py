import matplotlib.pyplot as plt

#Tempo de execucao do Quick Sort em segundos para cada qtd de elementos

condicoes = [10,25,50,75,100,250,500,750,1000,2500,5000,7500,10000,25000,50000,75000,100000]

dados_quick = [0.000004,0.000017,0.000024,0.000035,0.000078,0.000127,
               0.000226,0.000290,0.000325,0.000419,0.002382 ,0.003919 ,
               0.005457,0.011295,0.014825,0.025722,0.029547]

dados_bubble = [0.000006, 0.000020, 0.000057, 0.000094, 0.000237, 0.001510,
                0.004262, 0.008453, 0.014843, 0.040041, 0.128084, 0.290784,
                0.526207, 3.337507, 13.393707, 30.671931, 54.459569]

#Criando grafico Geral bubbleSort

plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,100000)
plt.ylim(0,25)
plt.title("Bubble Sort : Tempo decorrido na ordenacao")
plt.plot(condicoes, dados_bubble)
plt.show()

#Criando grafico Geral quickSort

plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,30000)
plt.ylim(0,0.1)
plt.title("Quick Sort : Tempo decorrido na ordenacao")
plt.plot(condicoes, dados_quick, 'r')
plt.show()

# Graficos sobrepostos

plt.rcParams['figure.figsize'] = (10,8)
plt.xlabel('n')
plt.ylabel('s')
plt.xlim(0,80000)
plt.ylim(0,5)
plt.title("Insertion Sort versus Bubble Sort")
plt.plot(condicoes, dados_quick)
plt.plot(condicoes, dados_bubble)
plt.show()
