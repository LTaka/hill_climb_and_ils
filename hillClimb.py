import limites
import random


def hill_climb(func, bounds, num_iteracao, pertubacao):
  melhor_solucao = None
  melhor_atual = float('inf')
  # pertubacao
  solucao = [
    # uniform irá imprimir um número aleatório no intervalo
    # range(len) é usada para gerar uma sequência de números inteiros que vai de 0 até o comprimento do vetor
    random.uniform(bounds[i][0], bounds[i][1]) for i in range(len(bounds))
  ]
  for i in range(num_iteracao):
    candidato = None
    while candidato is None or not limites.in_bounds(candidato, bounds):
      # pertubacao
      candidato = [
        solucao[j] + random.uniform(-pertubacao, pertubacao)
        for j in range(len(bounds))
      ]
      # print(candidato)
    valorPerturbada = func(candidato[0], candidato[1])
    # print(valorPerturbada)
    if valorPerturbada < melhor_atual:
      melhor_solucao = candidato
      melhor_atual = valorPerturbada
      solucao = candidato
  return melhor_solucao, melhor_atual
