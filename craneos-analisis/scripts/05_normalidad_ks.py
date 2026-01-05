import pandas as pd
import numpy as np
from scipy.stats import kstest
from pathlib import Path

# ---------------------------
# Rutas
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"

FILE_TEMPRANO = OUTPUTS_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUTPUTS_DIR / "cranios_tardio.csv"
FILE_TXT = OUTPUTS_DIR / "normalidad_ks.txt"


# ---------------------------
# Función KS con estandarización
# ---------------------------
def ks_normalidad(serie: pd.Series):
    """
    Aplica el test KS para normalidad tras estandarizar los datos.
    """
    media = serie.mean()
    std = serie.std(ddof=1)

    z = (serie - media) / std
    estadistico, p_valor = kstest(z, "norm")

    return estadistico, p_valor


# ---------------------------
# Carga de datos
# ---------------------------
temprano = pd.read_csv(FILE_TEMPRANO)["Anchura del cráneo"]
tardio = pd.read_csv(FILE_TARDIO)["Anchura del cráneo"]


# ---------------------------
# Test KS
# ---------------------------
ks_temp = ks_normalidad(temprano)
ks_tard = ks_normalidad(tardio)


# ---------------------------
# Guardar resultados
# ---------------------------
with open(FILE_TXT, "w", encoding="utf-8") as f:
    f.write("Test de normalidad Kolmogorov–Smirnov\n")
    f.write("====================================\n\n")

    f.write("Predinástico temprano\n")
    f.write(f"Estadístico KS: {ks_temp[0]:.4f}\n")
    f.write(f"p-valor       : {ks_temp[1]:.4f}\n\n")

    f.write("Predinástico tardío\n")
    f.write(f"Estadístico KS: {ks_tard[0]:.4f}\n")
    f.write(f"p-valor       : {ks_tard[1]:.4f}\n")

print("Resultados del test KS guardados en:", FILE_TXT)
