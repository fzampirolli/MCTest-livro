variations = [
    8, 10, 16, 24, 37, 37, 37, 37, 37, 37, 37, 37, 40, 44, 44, 44, 44, 44, 44, 44, 44, 44,
    81, 81, 81, 81, 81, 81, 108, 108, 108, 108, 108, 108, 108, 108, 121, 121, 121, 121, 121,
    121, 184, 184, 184, 184, 184, 184, 184, 184, 184, 184, 184, 184, 184, 188, 188, 188, 188,
    188, 188, 188, 188, 188, 188, 193, 193, 194, 199, 199, 199, 199
]

num_elementos_distintos = len(set(variations))
print("Número de elementos distintos:", num_elementos_distintos)
print(sorted(set(variations)))
