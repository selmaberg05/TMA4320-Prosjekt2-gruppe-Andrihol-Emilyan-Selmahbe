import numpy as np
import matplotlib.pyplot as plt

alpha = 0.8
T_p = 500
h = 1
N_x = 100
P = 2 * N_x         # Lengde på system, to sagtanner
N_p = 12 * N_x      # Antall partikler
Beta_k = 1000
n_steps = 20 * T_p

np.random.seed(0)   # Velger seed for å kunne reprodusere resultat


def build_V1(alpha, N_x):
    peak = int(alpha * (N_x - 1))
    n = np.arange(N_x)
    V = np.zeros(N_x, dtype=float)

    left = (n <= peak)
    right = (n > peak)

    V[left]  = n[left] / max(peak, 1)
    V[right] = (N_x - 1 - n[right]) / max((N_x - 1 - peak), 1)
    
    return np.concatenate([V, V])


V1 = build_V1(alpha, N_x)
V2 = np.zeros(P)

x = np.repeat(np.arange(P), 6)

J = np.zeros(n_steps)

for i in range(n_steps):

    if ((i // T_p) % 2 == 0):
        V = V2
    else:
        V = V1
        
    V_l = V[(x - 1) % P]
    V_0 = V[x]
    V_r = V[(x + 1) % P]

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

print(V1[0], V1[N_x-1], V1[N_x], V1[2*N_x-1], V1.max())
