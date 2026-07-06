import numpy as np
from scipy.optimize import minimize, nnls
from scripts.emma_system import build_system
from config.config import IONS_MODEL, sd_lookup

def solve_sample(row, em):

    sd_df = sd_lookup[row["site"]]

    A, b, sigma = build_system(row, em, sd_df)

    n = A.shape[1]
    x0 = np.ones(n) / n

    res = minimize(
        lambda f: np.sum((A @ f - b)**2),
        x0,
        bounds=[(0,1)] * n,
        constraints={"type":"eq", "fun": lambda f: np.sum(f) - 1},
        method="SLSQP"
    )

    if res.success:
        f = res.x
    else:
        f_nnls, _ = nnls(A, b)
        f = f_nnls / f_nnls.sum() if f_nnls.sum() > 0 else x0

    rmse = np.sqrt(np.mean(((A @ f - b) * sigma)**2))

    return f, rmse
