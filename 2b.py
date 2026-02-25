## Oppgave 2b

i) 

import numpy as np
import matplotlib.pyplot as plt

n = 101        # antall partikler
t_steps = 200  # antall tidssteg
runs = 100     # antall gjennomkjøringer av kdoen
delta_t = 1    # lengde på tidssteg
h = 1          # steglengde
Beta_k = 1

x0 = np.arange(-50, 51) #1 01 partikler  -50, 49, ... 0, ... 49, 50

p_minus = 1/3
p_plus = 1/3

def hardcore(p_minus, p_plus, x0, t_steps):

    x = x0.copy()

    for i in range(t_steps):
        occupied = set(x.tolist()) # okkupert posisjon, fjerner duplikat
        order = np.random.permutation(len(x)) # nytt array i tilfeldig rekkefølge

        for j in order:
            r = np.random.rand() # normaliser

            if r <= p_minus:
                new_pos = x[j] - 1
            elif r > (1 -  p_plus):
                new_pos = x[j] + 1
            else:
                new_pos = x[j]

            if new_pos != x[j]:  # forsøker her å flytte til ledig
                if new_pos not in occupied:
                    occupied.remove(x[j])
                    occupied.add(new_pos)
                    x[j] = new_pos
                    
    return x

x_axis = np.arange(-200, 201)
total = np.zeros_like(x_axis, dtype=float) # np.zeros_like gjør at lengden på x-aksen kan endres uten å måtte skrive om denne linja

for _ in range(runs):
    x_end = hardcore(p_minus, p_plus, x0, t_steps)
    for pos in x_end:
        if -200 <= pos <= 200:
            total[pos + 200] += 1

distribution = total / (n * runs)

plt.plot(x_axis, distribution, color = "teal")
plt.grid(alpha = 0.25)
plt.xlabel("x")
plt.ylabel("Sannsynlighet")
plt.title("V(x) = k")
plt.show()




ii)


import numpy as np
import matplotlib.pyplot as plt

n = 101       #antall partikler
t_steps = 200  #antall tidssteg
runs = 100     #antall gjennomkjøringer av kdoen
delta_t = 1   #lengde på tidssteg
h = 1         # steglengde
Beta_k = 1

x0 = np.arange(-50, 51) #101 partikler  -50, 49, ... 0, ... 49, 50

denominator = 1 + np.exp(Beta_k) + np.exp(-Beta_k)

p_minus = np.exp(-Beta_k) / denominator
p_plus = np.exp(+Beta_k) / denominator

def hardcore(p_minus, p_plus, x0, t_steps):

    x = x0.copy()
    for i in range(t_steps):
        occupied = set(x.tolist()) #okkupert posisjon
        order = np.random.permutation(len(x)) #tilfeldig rekkefølge

        for j in order:
            r = np.random.rand() #normaliser

            if r <= p_minus:
                new_pos = x[j] - 1
            elif r > (1 -  p_plus):
                new_pos = x[j] + 1
            else:
                new_pos = x[j]

            if new_pos != x[j]:  #forsøker her å flytte til ledig
                if new_pos not in occupied:
                    occupied.remove(x[j])
                    occupied.add(new_pos)
                    x[j] = new_pos
                    
    return x

x_axis = np.arange(-300, 301)
total = np.zeros_like(x_axis, dtype=float) # np.zeros_like gjør at lengden på x-aksen kan endres uten å måtte skrive om denne linja

for _ in range(runs):
    x_end = hardcore(p_minus, p_plus, x0, t_steps)
    for pos in x_end:
        if -300 <= pos <= 300:
            total[pos + 300] += 1

distribution = total / (n * runs)

plt.plot(x_axis, distribution, color = "teal")
plt.grid(alpha = 0.25)
plt.xlabel("x")
plt.ylabel("Sannsynlighet")
plt.title("V(x) = -kx")
plt.show()
            
