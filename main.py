import numpy as np
import funcao
import matplotlib.pyplot as plt
import ils
import hillClimb

# define range for input
bounds1a = [(-5, 5), (-5, 5)]
bounds1b = [(-2, 2), (-2, 2)]
bounds2a = [(-512, 512), (-512, 512)]
bounds2b = [(400, 512), (400, 512)]
memoriaHillClimb = []
memoriaIsl = []

for i in range(0, 30):

  num_iteracao = 1000
  perturbacao = 0.4

  # func = funcao.obj_1
  # bounds = bounds1a
  # bounds=bounds1b

  func = funcao.obj_2
  # bounds = bounds2a
  bounds = bounds2b

  # ///// chamada de funcao hill climb
  # melhor_solucao_HillClimb, score_HillClimb = hillClimb.hill_climb(
  #   func, bounds, num_iteracao, perturbacao)
  # print('%i //// f(%s) = %f \n' %
  #       (i, melhor_solucao_HillClimb, score_HillClimb))
  # memoriaHillClimb.append(score_HillClimb)

  num_repeticao = 30
  pertuba = 0.2504
  # ///// chamada de funcao Iterated Local Search
  melhor_solucao_ILS, score_Ils = ils.iterated_local_search(func,bounds,num_iteracao,perturbacao, num_repeticao, pertuba)
  print('%i //// f(%s) = %f \n' % (i, melhor_solucao_ILS, score_Ils))
  memoriaIsl.append(score_Ils)

if not memoriaIsl:
  print("///////////////////////Hill Climb/////////////////////////////")
  print(f"Mínimo: {min(memoriaHillClimb)}")
  print(f"Máximo: {max(memoriaHillClimb)}")
  print(f"Média: {np.mean(memoriaHillClimb)}")
  print(f"Desvio Padrão: {np.std(memoriaHillClimb)}")
  plt.boxplot(memoriaHillClimb)
  plt.show()
else:
  print("/////////////////Iterated Local Search////////////////////////")
  print(f"Mínimo: {min(memoriaIsl)}")
  print(f"Máximo: {max(memoriaIsl)}")
  print(f"Média: {np.mean(memoriaIsl)}")
  print(f"Desvio Padrão: {np.std(memoriaIsl)}")
  plt.boxplot(memoriaIsl)
  plt.show()
