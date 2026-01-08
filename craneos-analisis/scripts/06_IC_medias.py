# ============================================================
# HU-2.1 – Intervalos de confianza para la diferencia de medias
# Sprint 2 – Inferencia estadística
#
# Objetivo:
#   - Calcular intervalos de confianza al 90%, 95% y 99%
#     para la diferencia entre las medias de la anchura craneal
#     (predinástico tardío – predinástico temprano).
#   - Interpretar los resultados en función del test de normalidad
#     realizado en el Sprint 1.
#
# Parámetro de interés:
#   Δ = μ_tardío − μ_temprano
#
# Notas metodológicas:
#   - Se utiliza el enfoque de Welch (no asume igualdad de varianzas).
#   - Aunque una de las submuestras no sigue estrictamente una
#     distribución normal, se construyen IC paramétricos y se
#     discute su validez (robustez de la media).
# ============================================================

import pandas as pd
import numpy as np
from scipy import stats
import os
from pathlib import Path

# ------------------------------------------------------------
# 1. Carga de datos
# ------------------------------------------------------------

# ---------------------------
# Rutas
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"

FILE_TEMPRANO = OUTPUTS_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUTPUTS_DIR / "cranios_tardio.csv"
FILE_TXT = OUTPUTS_DIR / "normalidad_ks.txt"



# Se asume:
#   - columna 'periodo': 1 = predinástico temprano, 2 = predinástico tardío
#   - columna 'anchura': anchura del cráneo en mm

temprano = pd.read_csv(FILE_TEMPRANO)["Anchura del cráneo"]
tardio = pd.read_csv(FILE_TARDIO)["Anchura del cráneo"]

# ------------------------------------------------------------
# 2. Estadísticos descriptivos necesarios
# ------------------------------------------------------------

n_T = len(temprano)
n_L = len(tardio)

mean_T = temprano.mean()
mean_L = tardio.mean()

var_T = temprano.var(ddof=1)
var_L = tardio.var(ddof=1)

diff_means = mean_L - mean_T  # Δ = μ_tardío − μ_temprano

# ------------------------------------------------------------
# 3. Función para IC de la diferencia de medias (Welch)
# ------------------------------------------------------------

def ic_diferencia_medias(mean1, mean2, var1, var2, n1, n2, alpha):
    """
    Calcula un intervalo de confianza para la diferencia de medias
    utilizando el método de Welch.
    """
    se = np.sqrt(var1 / n1 + var2 / n2)

    # Grados de libertad de Welch
    df = (var1 / n1 + var2 / n2) ** 2 / (
        ((var1 / n1) ** 2) / (n1 - 1) + ((var2 / n2) ** 2) / (n2 - 1)
    )

    t_crit = stats.t.ppf(1 - alpha / 2, df)

    lower = (mean2 - mean1) - t_crit * se
    upper = (mean2 - mean1) + t_crit * se

    return lower, upper

# ------------------------------------------------------------
# 4. Cálculo de los intervalos solicitados
# ------------------------------------------------------------

ic_90 = ic_diferencia_medias(mean_T, mean_L, var_T, var_L, n_T, n_L, alpha=0.10)
ic_95 = ic_diferencia_medias(mean_T, mean_L, var_T, var_L, n_T, n_L, alpha=0.05)
ic_99 = ic_diferencia_medias(mean_T, mean_L, var_T, var_L, n_T, n_L, alpha=0.01)

# ------------------------------------------------------------
# 5. Resultados por pantalla
# ------------------------------------------------------------

print("Diferencia de medias (tardío - temprano): {:.3f}".format(diff_means))
print()
print("IC 90% : [{:.3f}, {:.3f}]".format(ic_90[0], ic_90[1]))
print("IC 95% : [{:.3f}, {:.3f}]".format(ic_95[0], ic_95[1]))
print("IC 99% : [{:.3f}, {:.3f}]".format(ic_99[0], ic_99[1]))

# ------------------------------------------------------------
# 6. Guardar resultados para el informe
# ------------------------------------------------------------

os.makedirs("outputs", exist_ok=True)

with open("outputs/ic_diferencia_medias.txt", "w", encoding="utf-8") as f:
    f.write("HU-2.1 – Intervalos de confianza para la diferencia de medias\n\n")
    f.write(f"Diferencia de medias (tardío - temprano): {diff_means:.3f}\n\n")
    f.write(f"IC 90% : [{ic_90[0]:.3f}, {ic_90[1]:.3f}]\n")
    f.write(f"IC 95% : [{ic_95[0]:.3f}, {ic_95[1]:.3f}]\n")
    f.write(f"IC 99% : [{ic_99[0]:.3f}, {ic_99[1]:.3f}]\n")

# ------------------------------------------------------------
# Fin del script HU-2.1
# ------------------------------------------------------------
