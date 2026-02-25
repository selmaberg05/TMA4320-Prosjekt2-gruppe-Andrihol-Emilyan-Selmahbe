import numpy as np
import matplotlib.pyplot as plt

#Opgave a

alpha = 0.1
T_p = 500
h = 1
N_x = 100
dt = 1
beta_k = 1000
k = 1
N_p = 12 * N_x
x_axis = np.arange(-N_x, N_x)
V_switch = 1

P = 2 * N_x

def build_V1(alpha, N_x):
    limit = int(alpha * (N_x - 1))
    n = np.arange(N_x)
    V = np.empty(N_x, float)
    V[:limit+1] = n[:limit+1] / max(limit, 1)
    V[limit+1:] = (N_x - 1 - n[limit+1:]) / max(N_x - 1 - limit, 1)
    return np.concatenate([V, V])

V1 = k * build_V1(alpha, N_x)

def V(x):
    if V_switch == 1:
        return V1[x % P]
    elif V_switch == 2:
        return 0
    return 0

def probability(x0):
    vm = V(x0 - 1)
    v0 = V(x0)
    vp = V(x0 + 1)
    p_p = 1 / (1 + np.exp(-beta_k * (vm - vp)) + np.exp(-beta_k * (v0 - vp)))
    p0  = 1 / (1 + np.exp(-beta_k * (vm - v0)) + np.exp(-beta_k * (vp - v0)))
    p_m = 1 / (1 + np.exp(-beta_k * (vp - vm)) + np.exp(-beta_k * (v0 - vm)))
    return p_p, p0, p_m

positions = np.arange(N_p, dtype=int)
j_current = []

for t in range(20 * T_p):
    if (t // T_p) % 2 == 0:
        V_switch = 2
    else:
        V_switch = 1

    n_p = 0
    n_m = 0
    new_positions = positions.copy()

    for j in range(N_p):
        x0 = positions[j]
        p_p, p0, p_m = probability(x0)

        r = np.random.rand()
        if r <= p_m:
            new_positions[j] = x0 - 1
            n_m += 1
        elif r >= 1 - p_p:
            new_positions[j] = x0 + 1
            n_p += 1

    positions = new_positions
    j_current.append((n_p - n_m) / N_p)

j_current = np.array(j_current)

def j(t):
    return j_current[t]

def j_mean(n):
    a = 2 * T_p * n
    b = 2 * T_p * (n + 1)
    return np.mean(j_current[a:b])

for n in range(10):
    print(n, j_mean(n))

#Oppgave b

'''
Choose 50 values of Tp equally spaced between 1 and 1001, and run the random walk simulation for
one cycle for each of these values. Let the number of particles in the system be Np = 40Nx, and
use α = 0.8. Start each simulation with half of the particles at each of the two x-coordinates which
coincide with the minima of V1(x) (however, let the particles start in energy level 2 defined by V2(x)).
Reset the system into this state for every new set of parameters Tp. Calculate one cycle-averaged
current Javg for all the values of Tp. Plot Javg as function of Tp. What do you observe? Give a
physical interpretation of the results.
'''

T_p = np.linspace(1,1001,50,dtype=int)
N_p = 40 * N_x
alpha = 0.8

