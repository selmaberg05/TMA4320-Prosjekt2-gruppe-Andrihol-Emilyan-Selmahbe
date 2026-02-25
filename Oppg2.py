import numpy as np
import matplotlib.pyplot as plt

#Oppgave a
runs = 100
n = 101
t_steps = 200
h = 1
dt = 1
beta_k = 1
n_runs = 100

k = 1
V_case = "i"  # "i" eller "ii"

x_min = -200
x_max = 200
x_vals = np.arange(x_min, x_max + 1, dtype=int)


def V(x):
    if V_case == "i":
        return k
    elif V_case == "ii":
        return -k*x


def probability(x0):
    vm = V(x0-1)
    v0 = V(x0)
    vp = V(x0+1)
    p_p = 1 / (1 + np.exp(-beta_k * (vm - vp)) + np.exp(-beta_k * (v0 - vp)))
    p0  = 1 / (1 + np.exp(-beta_k * (vm - v0)) + np.exp(-beta_k * (vp - v0)))
    p_m = 1 / (1 + np.exp(-beta_k * (vp - vm)) + np.exp(-beta_k * (v0 - vm)))
    return p_p, p0, p_m

all_positions = []
for i in range(runs):
    positions = np.arange(n, dtype=int) - n//2
    for t in range(t_steps):
        new_positions = positions.copy()
        for j in range(n):
            x0 = positions[j]
            p_p, p0, p_m = probability(x0)

            number = np.random.uniform(0, 1)
            
            if number <= p_m:
                new_positions[j] = x0 - 1
            elif number >= 1 - p_p:
                new_positions[j] = x0 + 1
        positions = new_positions
    all_positions.append(positions.copy())

all_positions = np.array(all_positions)
vals, counts = np.unique(all_positions.flatten(), return_counts=True)

count_map = dict(zip(vals, counts))
counts_on_xvals = np.array([count_map.get(x, 0) for x in x_vals], dtype=float)

distribution = counts_on_xvals / (runs * n)

plt.plot(x_vals, distribution)
plt.show()


#Oppgave b
all_positions = []
for i in range(runs):
    positions = np.arange(n, dtype=int) - n //2
    for t in range(t_steps):
        order = np.random.permutation(n)
        occupied = set(positions.tolist())
        for j in order:
            x0 = positions[j]
            p_p, p0, p_m = probability(x0)

            number = np.random.uniform(0, 1)
            if number <= p_m:
                x = x0 - 1
                if x not in occupied:
                    occupied.remove(x0)
                    occupied.add(x)
                    positions[j] = x
            elif number >= 1 - p_p:
                x = x0 + 1
                if x not in occupied:
                    occupied.remove(x0)
                    occupied.add(x)
                    positions[j] = x

    all_positions.append(positions.copy())

all_positions = np.array(all_positions)
vals, counts = np.unique(all_positions.flatten(), return_counts=True)

count_map = dict(zip(vals, counts))
counts_on_xvals = np.array([count_map.get(x, 0) for x in x_vals], dtype=float)

distribution = counts_on_xvals / (runs * n)

plt.plot(x_vals, distribution)
plt.show()