import math
def obj_1( x, y):  # calcula o valor para a funcao objetivo do 
  funcao = ((math.pow(x, 2)) + (math.pow(y, 2)) + 25 *
            (math.sin(math.radians(x + y))**2))

  return funcao
def obj_2(x, y):  # calcula o valor para a funcao objetivo do exercício 2
  funcao = -1 * (y + 47) * (math.sin(
    math.radians(math.sqrt(abs((1 / 2) * y + y + 47))))) - x * (math.sin(
      math.radians(math.sqrt(abs(x - (y + 47))))))

  return funcao
