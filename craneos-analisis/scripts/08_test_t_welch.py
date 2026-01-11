# ============================================================
# HU-2.2 – Test t para la diferencia de medias (Welch)
#
# H0: μ_tardío = μ_temprano
# H1: μ_tardío ≠ μ_temprano
#
# Nivel de significación: alpha = 0.05
# ============================================================

import os
import pandas as pd
from scipy import stats
from pathlib import Path

# -----------------------------
# 1) Configuración
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "outputs"
FILE_TEMPRANO = OUT_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUT_DIR / "cranios_tardio.csv"
OUT_FILE = OUT_DIR / "homocedasticidad_levene.txt"

ALPHA = 0.05

# -----------------------------
# 2) Carga de datos
# -----------------------------
temprano = pd.read_csv(FILE_TEMPRANO)["Anchura del cráneo"]
tardio = pd.read_csv(FILE_TARDIO)["Anchura del cráneo"]

# -----------------------------
# 3) Test t de Welch
# -----------------------------
t_stat, p_value = stats.ttest_ind(
    tardio,
    temprano,
    equal_var=False  # Welch
)

decision = (
    "Se rechaza H0 (diferencia significativa de medias)"
    if p_value <= ALPHA
    else "No se rechaza H0 (no hay evidencia de diferencia)"
)

# -----------------------------
# 4) Salida por consola
# -----------------------------
print("=== HU-2.2 – Test t de Welch ===")
print(f"Estadístico t: {t_stat:.6f}")
print(f"p-valor: {p_value:.6f}")
print(f"alpha: {ALPHA}")
print(f"Decisión: {decision}")

# -----------------------------
# 5) Guardar resultados
# -----------------------------
os.makedirs(OUT_DIR, exist_ok=True)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("HU-2.2 – Test t de Welch\n")
    f.write("========================\n\n")
    f.write("Hipótesis:\n")
    f.write("  H0: μ_tardío = μ_temprano\n")
    f.write("  H1: μ_tardío ≠ μ_temprano\n\n")
    f.write(f"Estadístico t: {t_stat:.6f}\n")
    f.write(f"p-valor: {p_value:.6f}\n")
    f.write(f"alpha: {ALPHA}\n\n")
    f.write(f"Decisión: {decision}\n")

print(f"\nResultados guardados en: {OUT_FILE}")
