## Oppgave 1a)

i)

#importerer nødvendig biblioteker
import numpy as np
import matplotlib.pyplot as plt

n = 101        # antall partikler
t_steps = 200  # antall tidssteg
runs = 100     # antall gjennomkjøringer av koden
delta_t = 1    # lengde på tidssteg
h = 1          # steglengde
Bk = 1

x0 = np.arange(-50, 51) #101 partikler  -50, 49, ... 0, ... 49, 50

# p+ og p- satt slik som løst i oppgave 1c)
p_minus = 1/3 
p_plus = 1/3

x_axis = np.arange(-200, 201)
total_count = np.zeros_like(x_axis, dtype=float) 
# np.zeros_like gjør at lengden på x-aksen kan endres uten å måtte skrive om denne linja

for i in range(runs):
    x = x0.copy()

    for j in range(t_steps):
        r = np.random.rand(n)  # tifeldig tall mellom 0 og 1

        x[r <= p_minus] -= 1
        x[r > (1 - p_plus)] += 1

    count = np.zeros_like(x_axis, dtype=float)
    for pos in x:
        if -200 <= pos <= 200:
            count[pos + 200] += 1  # +200 for å matche indeks-nummer

    total_count += count

distribution = total_count / (n * runs)

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

x_axis = np.arange(-200, 201)
total_count = np.zeros_like(x_axis, dtype=float) # np.zeros_like gjør at lengden på x-aksen kan endres uten å måtte skrive om denne linja

for i in range(runs):
    x = x0.copy()

    for j in range(t_steps):
        r = np.random.rand(n)

        x[r <= p_minus] -= 1
        x[r > (1 - p_plus)] += 1

    count = np.zeros_like(x_axis)
    for pos in x:
        if - 200 <= pos <= 200:
            count[pos + 200] += 1  # +200 for å matche indeks-nummer

    total_count += count

distribution = total_count / (n * runs)

plt.plot(x_axis, distribution, color = "teal")
plt.grid(alpha = 0.25)
plt.xlabel("x")
plt.ylabel("Sannsynlighet")
plt.title("V(x) = -kx")
plt.show()

