import numpy as np
import matplotlib.pyplot as plt

alpha = 0.8
h = 1
N_x = 100
P = 2 * N_x      #periode P, gjentas 2 ganger
N_p = 40 * N_x
Beta_k = 1000

T_p_vals = np.linspace(1, 1001, 50).astype(int)



def build_V1(alpha, N_x):
    limit = int(alpha * N_x)
    n = np.arange(N_x)

    V = np.zeros(N_x, dtype=float)

    left = (n <= limit)
    right = (n > limit)

    V[left]  = n[left] / max(limit, 1)
    V[right] = (N_x - n[right]) / max((N_x - limit), 1)

    return np.concatenate([V, V])

V1 = build_V1(alpha, N_x)
V2 = np.zeros(P)

min1 = np.argmin(V1[:N_x])
min2 = N_x + np.argmin(V1[N_x:])

x0 = np.array([min1] * (N_p // 2) + [min2] * (N_p // 2), dtype=int)

J_avg =  np.zeros(len(T_p_vals))

for i, T_p in enumerate(T_p_vals):

    x = x0.copy()

    J_sum = 0
    n_steps = 2 * T_p

    for j in range(n_steps):
        
        if (j < T_p):
            p_minus = 1/3
            p_plus  = 1/3
        else:
            V_l = V1[(x - 1) % P]
            V_0 = V1[x]
            V_r = V1[(x + 1) % P]

            p_plus  = 1 / (1 + np.exp(-Beta_k*(V_l - V_r)) + np.exp(-Beta_k*(V_0 - V_r)))
            p_minus = 1 / (1 + np.exp(-Beta_k*(V_r - V_l)) + np.exp(-Beta_k*(V_0 - V_l)))
    

        r = np.random.rand(N_p)
    
        pos = np.zeros_like(x) # tomt array med posisjon 0
        pos[r < p_minus] = -1
        pos[r > 1 - p_plus] = +1

        n_plus  = np.sum(pos == 1) # teller hvor mange partikelr som gikk til høyre
        n_minus = np.sum(pos == -1) # teller hvor mange partikelr som gikk til venstre
        J_t = (n_plus - n_minus) / N_p  # current J[i]

        J_sum += J_t
        x = (x + pos) % P  # randbet, x0 -> x199
        

    J_avg[i] = J_sum / (2 * T_p)
    
plt.plot(T_p_vals, J_avg, color = "teal")
plt.title("curren noe sånt")
plt.grid(alpha = 0.2)
plt.xlabel("$T_p$")
plt.ylabel("$J_{avg}$")
plt.show()

# bruke clip for sensitivitet? for p_plus og p_minus
