import random

for i in range(10):
    soma, diferenca = random.sample(range(2, 30), 2)
    if soma==30 or diferenca == 30:
        print(soma, diferenca)
