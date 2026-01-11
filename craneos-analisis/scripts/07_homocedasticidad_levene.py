# ============================================================
# HU-2.2 – Homocedasticidad (igualdad de varianzas)
# Subtarea: comprobar homocedasticidad entre dos muestras
#
# Test recomendado: Levene (robusto a no-normalidad)
#
# H0: varianzas iguales
# H1: varianzas distintas
#
# Regla (alpha=0.05):
#   - p > alpha  -> no se rechaza H0 (homocedasticidad plausible)
#   - p <= alpha -> se rechaza H0 (no homocedasticidad)
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
# 3) Test de Levene
# -----------------------------
# center='median' suele ser aún más robusto a outliers/no-normalidad
levene_stat, levene_p = stats.levene(temprano, tardio, center="median")

decision = (
    "NO se rechaza H0 (homocedasticidad plausible)"
    if levene_p > ALPHA
    else "Se rechaza H0 (NO hay homocedasticidad)"
)

# -----------------------------
# 4) Salida por consola
# -----------------------------
print("=== HU-2.2 – Test de homocedasticidad (Levene) ===")
print(f"n_temprano: {len(temprano)} | n_tardio: {len(tardio)}")
print(f"Estadístico Levene: {levene_stat:.6f}")
print(f"p-valor: {levene_p:.6f}")
print(f"alpha: {ALPHA}")
print(f"Decisión: {decision}")

# -----------------------------
# 5) Guardar salida en archivo
# -----------------------------
os.makedirs(OUT_DIR, exist_ok=True)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("HU-2.2 – Homocedasticidad (Levene)\n")
    f.write("================================\n\n")
    f.write(f"Datos: \n")
    f.write(f"  - Archivo 1: {FILE_TEMPRANO.name}\n")
    f.write(f"  - Archivo 2: {FILE_TARDIO.name}\n\n")
    f.write(f"Grupos: periodo 1 (temprano) vs periodo 2 (tardío)\n\n")
    f.write(f"n_temprano: {len(temprano)}\n")
    f.write(f"n_tardio  : {len(tardio)}\n\n")
    f.write("Hipótesis:\n")
    f.write("  H0: varianzas iguales\n")
    f.write("  H1: varianzas distintas\n\n")
    f.write(f"Estadístico Levene: {levene_stat:.6f}\n")
    f.write(f"p-valor           : {levene_p:.6f}\n")
    f.write(f"alpha            : {ALPHA}\n\n")
    f.write(f"Decisión: {decision}\n")

print(f"\nResultados guardados en: {OUT_FILE}")
