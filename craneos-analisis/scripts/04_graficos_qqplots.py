import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from pathlib import Path

# ---------------------------
# Rutas
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"

FIGURES_DIR.mkdir(exist_ok=True)

FILE_TEMPRANO = OUTPUTS_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUTPUTS_DIR / "cranios_tardio.csv"


# ---------------------------
# Carga de datos
# ---------------------------
temprano = pd.read_csv(FILE_TEMPRANO)["Anchura del cráneo"]
tardio = pd.read_csv(FILE_TARDIO)["Anchura del cráneo"]


# --------------------------------------------
# Q–Q plots para evaluación visual de normalidad
# --------------------------------------------

plt.figure(figsize=(12, 5))

# Q–Q plot predinástico temprano
plt.subplot(1, 2, 1)
stats.probplot(temprano, dist="norm", plot=plt)
plt.title("Q–Q plot – Predinástico temprano")

# Q–Q plot predinástico tardío
plt.subplot(1, 2, 2)
stats.probplot(tardio, dist="norm", plot=plt)
plt.title("Q–Q plot – Predinástico tardío")

plt.tight_layout()

plt.savefig(FIGURES_DIR / "qqplot_comparativo.png", dpi=300)
plt.close()

print("Q–Q plots generados en:", FIGURES_DIR)