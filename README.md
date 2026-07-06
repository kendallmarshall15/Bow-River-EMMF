# Bow-River-EMMF
End-Member Mixing Framework (EMMF) model for groundwater contributions in the Bow River watershed

This repository contains a reproducible End-Member Mixing Framework (EMMf) used to quantify groundwater and surface water contributions to streamflow in the Bow River watershed, Alberta, Canada.

The script solves a constrained mixing problem:

stream samples are expressed as mixtures of defined hydrochemical end-members
mixing fractions are solved using a weighted least-squares approach
uncertainty is propagated using Monte Carlo simulations

The output is a time series of end-member contributions for each sampling site, along with uncertainty bounds.

The Bow River watershed provides a useful setting for this type of analysis because it crosses two distinct hydrogeologic domains:

the Main Ranges, where flow is more seasonally driven and shallow systems dominate
the Front Ranges, where more permeable units and structural features support longer flow paths and greater groundwater storage

These differences show up clearly in the chemistry and mixing behaviour downstream.

bow-river-emmf/
│
├── run_emmf.py                 # Main execution script
│
├── config/
│   └── config.py               # All model parameters and file paths
│
├── scripts/
│   ├── io.py                  # Data loading functions
│   ├── preprocess.py         # Site filtering and cleaning
│   ├── emma_system.py        # Weighted EMMA system builder
│   ├── solver.py             # Constrained mixing solver
│   ├── monte_carlo.py       # Uncertainty propagation
│   ├── diagnostics.py       # End-member redundancy analysis
│   ├── export.py            # Output generation
│
├── data/
│   ├── raw/                  # Input datasets (optional)
│   └── processed/
│
├── outputs/
│   ├── fractions/           # EMMA results (median + CI)
│   ├── diagnostics/         # Model diagnostics
│   └── figures/             # Plots
│
└── README.md

Install the basic dependencies:

pip install numpy pandas scipy

Then run:

python run_emma.py

If you use this code, please cite the associated thesis or manuscript:
Campbell et al, in preparation

This is a research codebase, not a packaged software tool. It assumes:
conservative mixing of solutes
steady end-member compositions
representative sampling of seasonal variability
