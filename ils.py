import limites
from datetime import datetime
from numpy.random import randn
from numpy.random import rand
from random import seed
from numpy import asarray

seed(datetime.now())


def iterated_local_search(func, bounds, num_iteracao, perturbacao,
                          num_repeticao, pertuba):
  solucao_inicial = None
  # uniform irá imprimir um número aleatório no intervalo
  # rand(len) gera um vetor de números aleatórios entre 0 e 1, com o mesmo tamanho de bounds
  bounds = asarray(bounds)
  while solucao_inicial is None or not limites.in_bounds(
      solucao_inicial, bounds):
    solucao_inicial = bounds[:, 0] + rand(
      len(bounds)) * (bounds[:, 1] - bounds[:, 0])
  melhor_atual = func(solucao_inicial[0], solucao_inicial[1])

  for n in range(num_repeticao):
    # fazendo busca local com Hill climb
    start_pt = None
    while start_pt is None or not limites.in_bounds(start_pt, bounds):
      start_pt = solucao_inicial + randn(len(bounds)) * pertuba
    solucao, solucaoPertubado = hillclimbing(func, bounds, num_iteracao,
                                             perturbacao, start_pt)

    if solucaoPertubado < melhor_atual:
      solucao_inicial, melhor_atual = solucao, solucaoPertubado
  return [solucao_inicial, melhor_atual]


def hillclimbing(func, bounds, n_iterations, perturbacao, start_pt):
  solucao = start_pt
  # pertubacao
  solucaoPertubado = func(solucao[0], solucao[1])
  for i in range(n_iterations):
    candidato = None
    while candidato is None or not limites.in_bounds(candidato, bounds):
      # pertubacao
      candidato = solucao + randn(len(bounds)) * perturbacao
    candidatoPertuba = func(candidato[0], candidato[1])
    if candidatoPertuba <= solucaoPertubado:
      solucao, solucaoPertubado = candidato, candidatoPertuba
  return [solucao, solucaoPertubado]
