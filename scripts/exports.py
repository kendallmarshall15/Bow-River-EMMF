import pandas as pd
import numpy as np
from config.config import END_MEMBER_COLS

def export_results(river, frac_draws, rmse_draws, out_path):

    q_frac = np.quantile(frac_draws, [0.025, 0.5, 0.975], axis=2)
    q_rmse = np.quantile(rmse_draws, [0.025, 0.5, 0.975], axis=1)

    rows = []

    for i, row in river.iterrows():

        rec = {
            "Row": row["Row"],
            "date": row["date"],
            "RMSE_med": q_rmse[1,i]
        }

        for j, emc in enumerate(END_MEMBER_COLS):
            rec[f"{emc}_med"] = q_frac[1,i,j]
            rec[f"{emc}_lo"]  = q_frac[0,i,j]
            rec[f"{emc}_hi"]  = q_frac[2,i,j]

        rows.append(rec)

    out = pd.DataFrame(rows)
    out.to_csv(out_path, index=False)

    return out
