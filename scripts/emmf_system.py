import numpy as np
from config.config import (
    sigma_analytical, MIN_SIGMA,
    IONS_MODEL
)

def build_system(row, em, sd_df):
    A = em.to_numpy(float)
    b = row[IONS_MODEL].to_numpy(float)

    sigma_env = np.zeros(len(IONS_MODEL))

    for i, ion in enumerate(IONS_MODEL):

        m = sd_df[
            (sd_df["Ion"] == ion) &
            (sd_df["Month_num"] == int(row["Month"]))
        ]

        if not m.empty:
            sigma_env[i] = m["SD_mgL"].iloc[0]
        else:
            sigma_env[i] = sd_df.loc[
                sd_df["Ion"] == ion, "SD_mgL"
            ].median()

    sigma = np.sqrt(
        sigma_env**2 +
        np.array([sigma_analytical[i] for i in IONS_MODEL])**2
    )

    sigma = np.maximum(sigma, MIN_SIGMA)

    return A / sigma[:, None], b / sigma, sigma
