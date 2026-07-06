from pathlib import Path
import numpy as np

# ================================================================
# PATHS
# ================================================================
BASE_DIR = Path.home() / "OneDrive/Desktop/Excel Files"
HIST_DIR = Path.home() / "OneDrive/Desktop/Hist_data"

river_path = HIST_DIR / "Canmore_hits.csv"
em_path    = BASE_DIR / "Endmember Ions From Springs.csv"

sd_LL_path  = HIST_DIR / "LL_uncertainty.csv"
sd_CNM_path = HIST_DIR / "Canmore_Uncertainty.csv"

out_path = BASE_DIR / "EMMA_Bow125_results.csv"

TARGET_SITE = "Bow (125 km)"

# ================================================================
# MODEL SETTINGS
# ================================================================
IONS_MODEL = ["CaMg", "HCO3", "SO4", "Sr", "Na", "SiO2"]
ENDMEMBER_COLS = ["LSW", "MR_sil", "MR_carb", "FR_sil", "FR_carb"]
META_COLS = ["date", "site"]

N_MC = 300
MIN_SIGMA = 1e-6

rng = np.random.default_rng(42)

# ================================================================
# UNCERTAINTY
# ================================================================
sigma_analytical = {
    "CaMg": 0.05,
    "HCO3": 2.0,
    "SO4": 0.5,
    "Sr": 0.005,
    "Na": 0.2,
    "SiO2": 0.05
}

frac_sd_by_ion = {
    "CaMg": 0.10,
    "HCO3": 0.10,
    "SO4": 0.15,
    "Sr": 0.20,
    "Na": 0.20,
    "SiO2": 0.05
}

month_map = {
    "Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
    "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12
}
