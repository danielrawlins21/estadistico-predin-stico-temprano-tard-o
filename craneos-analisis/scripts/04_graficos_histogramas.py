import pandas as pd
import seaborn as sns
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
# Histogramas por submuestra
# --------------------------------------------

plt.figure(figsize=(12, 5))

# Histograma predinástico temprano
plt.subplot(1, 2, 1)
sns.histplot(temprano, bins=10, kde=True)
plt.title("Histograma – Predinástico temprano")
plt.xlabel("Anchura craneal (mm)")
plt.ylabel("Frecuencia")

# Histograma predinástico tardío
plt.subplot(1, 2, 2)
sns.histplot(tardio, bins=10, kde=True)
plt.title("Histograma – Predinástico tardío")
plt.xlabel("Anchura craneal (mm)")
plt.ylabel("Frecuencia")

plt.tight_layout()
plt.savefig(FIGURES_DIR / "histogramas_submuestras.png", dpi=300)
plt.close()

print("Histogramas generados en:", FIGURES_DIR)
