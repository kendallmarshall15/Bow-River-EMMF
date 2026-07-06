from config.config import *
from scripts.io import load_river, load_endmembers
from scripts.preprocess import filter_site
from scripts.monte_carlo import run_mc
from scripts.export import export_results

# Load data
river = load_river(river_path, IONS_MODEL, META_COLS)
em = load_endmembers(em_path, IONS_MODEL, END_MEMBER_COLS)

# Filter
river = filter_site(river)

# Run model
frac_draws, rmse_draws = run_mc(river, em, N_MC)

# Export
export_results(river, frac_draws, rmse_draws, out_path)

print("EMMA run complete.")
