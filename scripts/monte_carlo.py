import numpy as np
from config.config import (
    frac_sd_by_ion, rng, IONS_MODEL, END_MEMBER_COLS
)
from scripts.solver import solve_sample

def run_mc(river, em, N_MC):

    frac_draws = np.zeros((len(river), len(END_MEMBER_COLS), N_MC))
    rmse_draws = np.zeros((len(river), N_MC))

    for k in range(N_MC):

        em_k = em.copy()

        for ion in IONS_MODEL:
            for col in END_MEMBER_COLS:
                mu = em.loc[ion, col]
                em_k.loc[ion, col] = max(
                    rng.normal(mu, frac_sd_by_ion[ion] * mu),
                    0
                )

        for i, row in river.iterrows():
            f, rmse = solve_sample(row, em_k)
            frac_draws[i,:,k] = f
            rmse_draws[i,k] = rmse

    return frac_draws, rmse_draws
