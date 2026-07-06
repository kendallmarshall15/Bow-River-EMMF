import pandas as pd
from config.config import month_map

def load_river(path, ions, meta_cols):
    df = pd.read_csv(path)

    cols = meta_cols + ["Ca","Mg","HCO3","SO4","Sr","Na","SiO2"]
    df = df[cols].copy()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["Month"] = df["date"].dt.month

    for c in ["Ca","Mg","HCO3","SO4","Sr","Na","SiO2"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df.replace([float("inf"), float("-inf")], None, inplace=True)

    df = df.dropna(subset=ions + ["Month"]).reset_index(drop=True)
    df["Row"] = df.index

    return df


def load_endmembers(path, ions, em_cols):
    em_raw = pd.read_csv(path)

    ion_col = next(c for c in ["Ion","ion","Unnamed: 1"] if c in em_raw.columns)

    em_raw = em_raw.rename(columns={ion_col: "Ion"}).set_index("Ion")

    em = em_raw.loc[ions, em_cols].astype(float)

    return em
