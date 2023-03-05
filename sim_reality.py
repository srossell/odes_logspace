from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

from bcodes.ratevector import create_rate_vector
from bcodes.stoichiometrymatrix import build_stoichiometry_matrix
from stanutils.io import dict_to_rdump


np.random.seed(2357)
id_sp = ["met"]
id_rs = ["v1", "v2"]
rates = {"v1": "a", "v2": "b * met / (c + met)"}
params = {"a": 1, "b": 1.5, "c": 0.314}

mass_balances = {"met": {"v1": 1, "v2": -1}}
y0 = [1e-6]

t_vec = np.linspace(0, 100, 100)

S = build_stoichiometry_matrix(id_sp, id_rs, mass_balances)
v = create_rate_vector(id_sp, id_rs, rates, params)

def odes(t, y):
    return np.dot(S, v(y))

t_obs = np.linspace(0, 5, 5)
sol = solve_ivp(odes, [0, 100], y0, t_eval=t_obs)

noise = (0.5 - np.random.rand(5)) * 0.2
obs = (sol.y.flatten() + noise)[1:]

# plt.plot(sol.t, sol.y.T, lw=0, marker="o", label="true")
# plt.plot(sol.t, obs, lw=0, marker="o", label="noise")
# plt.legend()
# plt.savefig("reality.png")

datadict = {
        "y_obs_dim0": len(obs),
        "y_obs": obs,
        "t_obs_dim0": t_obs.shape[0] - 1,
        "t_obs": t_obs[1:],
        "y0": y0,
        "y0_dim0": 1,
        }
datadict_ln = {
        "y_obs_dim0": len(obs),
        "y_obs": np.log(obs),
        "t_obs_dim0": t_obs.shape[0] - 1,
        "t_obs": t_obs[1:],
        "y0": np.log(y0),
        "y0_dim0": 1,
        }

with open("data.r", "w") as f:
    f.write(dict_to_rdump(datadict))

with open("data_ln.r", "w") as f:
    f.write(dict_to_rdump(datadict_ln))
