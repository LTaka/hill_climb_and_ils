def in_bounds(candidato, bounds):
    for i in range(len(bounds)):
        if candidato[i] < bounds[i][0] or candidato[i] > bounds[i][1]:
            return False
    return True
