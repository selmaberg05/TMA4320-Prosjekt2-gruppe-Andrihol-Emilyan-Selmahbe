## oppgave 3a)

import numpy as np
import matplotlib.pyplot as plt

alpha = 0.8
T_p = 500
h = 1
N_x = 100
P = 2 * N_x      #periode P, gjentas 2 ganger
N_p = 12 * N_x
delta_t = 1
Beta_k = 1000
n_steps = 20 * T_p



def build_V1(alpha, N_x):
    limit = int(alpha * (N_x - 1))
    n = np.arange(N_x)
    
    V = np.empty(N_x, float)
    V[:limit+1] = n[:limit+1] / limit  # stigende
    V[limit+1:] = (N_x - 1 - n[limit+1:]) / (N_x - 1 - limit)  # synkende
    
    return np.concatenate([V, V])

V1 = build_V1(alpha, N_x)
V2 = np.zeros(P)

x = np.repeat(np.arange(P), 6)

J = np.zeros(n_steps)

for i in range(n_steps):

    if ((i // T_p) % 2 == 0):
        p_minus = 1/3
        p_plus  = 1/3
    else:
        V_l = V1[(x - 1) % P]
        V_0 = V1[x]
        V_r = V1[(x + 1) % P]

        p_plus  = 1 / (1 + np.exp(-Beta_k*(V_l - V_r)) + np.exp(-Beta_k*(V_0 - V_r)))
        p_minus = 1 / (1 + np.exp(-Beta_k*(V_r - V_l)) + np.exp(-Beta_k*(V_0 - V_l)))

    r = np.random.rand(len(x))
    
    pos = np.zeros_like(x) # tomt array med posisjon 0
    pos[r < p_minus] = -1
    pos[r > 1 - p_plus] = +1

    n_plus  = np.sum(pos == 1) # teller hvor mange partikelr som gikk til høyre
    n_minus = np.sum(pos == -1) # teller hvor mange partikelr som gikk til venstre
    J[i] = (n_plus - n_minus) / N_p  # current J[i]

    x = (x + pos) % P  # randbet, x0 -> x199

J_avg = np.zeros(10)

for n in range(10):
    cycle_length = 2 * T_p  # 500 steg i V1 og 500 steg i V2
    start = n * cycle_length
    end = (n + 1) * cycle_length
    J_avg[n] = np.mean(J[start:end])
    print(n, J_avg[n])
       

# bruke clip for sensitivitet? for p_plus og p_minus
