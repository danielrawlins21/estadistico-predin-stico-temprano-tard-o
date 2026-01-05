import pandas as pd
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


# ---------------------------
# Boxplot separado
# ---------------------------
plt.figure(figsize=(6, 4))
plt.boxplot(temprano, vert=True)
plt.title("Anchura craneal – Predinástico temprano")
plt.ylabel("Anchura")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "boxplot_temprano.png", dpi=300)
plt.close()

plt.figure(figsize=(6, 4))
plt.boxplot(tardio, vert=True)
plt.title("Anchura craneal – Predinástico tardío")
plt.ylabel("Anchura")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "boxplot_tardio.png", dpi=300)
plt.close()


# ---------------------------
# Boxplot comparativo
# ---------------------------
plt.figure(figsize=(7, 4))
plt.boxplot([temprano, tardio], labels=["Temprano", "Tardío"])
plt.title("Comparación de la anchura craneal por periodo")
plt.ylabel("Anchura")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "boxplot_comparativo.png", dpi=300)
plt.close()

print("Boxplots generados en:", FIGURES_DIR)
