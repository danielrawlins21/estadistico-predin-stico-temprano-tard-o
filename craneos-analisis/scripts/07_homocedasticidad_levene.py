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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import f
from pathlib import Path

# -----------------------------
# 1) Configuración
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "outputs"
FILE_TEMPRANO = OUT_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUT_DIR / "cranios_tardio.csv"
OUT_FILE = OUT_DIR / "homocedasticidad_levene.txt"

# Figura a guardar
OUT_FIG = OUT_DIR / "figures/distribucion_f_valores_criticos.png"

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

# Grados de libertad del estadístico ~ F en Levene:
# df1 = k - 1 (k grupos)
# df2 = N - k (N total observaciones)
k = 2
n1, n2 = len(temprano), len(tardio)
N = n1 + n2
df1 = k - 1
df2 = N - k

# Para visualización tipo “dos colas” (como tu figura):
f_crit_inf = f.ppf(ALPHA / 2, df1, df2)
f_crit_sup = f.ppf(1 - ALPHA / 2, df1, df2)


# -----------------------------
# 4) Salida por consola
# -----------------------------
print("=== HU-2.2 – Test de homocedasticidad (Levene) ===")
print(f"n_temprano: {n1} | n_tardio: {n2}")
print(f"Estadístico Levene: {levene_stat:.6f}")
print(f"p-valor: {levene_p:.6f}")
print(f"alpha: {ALPHA}")
print(f"Decisión: {decision}")


# -----------------------------
# 5) Guardar salida en archivo
# -----------------------------
os.makedirs(OUT_DIR, exist_ok=True)

with open(OUT_FILE, "w", encoding="utf-8") as ftxt:
    ftxt.write("HU-2.2 – Homocedasticidad (Levene)\n")
    ftxt.write("================================\n\n")
    ftxt.write("Datos:\n")
    ftxt.write(f"  - Archivo 1: {FILE_TEMPRANO.name}\n")
    ftxt.write(f"  - Archivo 2: {FILE_TARDIO.name}\n\n")
    ftxt.write("Grupos: periodo 1 (temprano) vs periodo 2 (tardío)\n\n")
    ftxt.write(f"n_temprano: {n1}\n")
    ftxt.write(f"n_tardio  : {n2}\n\n")
    ftxt.write("Hipótesis:\n")
    ftxt.write("  H0: varianzas iguales\n")
    ftxt.write("  H1: varianzas distintas\n\n")
    ftxt.write(f"Estadístico Levene: {levene_stat:.6f}\n")
    ftxt.write(f"p-valor           : {levene_p:.6f}\n")
    ftxt.write(f"alpha            : {ALPHA}\n\n")
    ftxt.write(f"Decisión: {decision}\n\n")
    ftxt.write("Parámetros distribución F (para visualización):\n")
    ftxt.write(f"  df1 = {df1}\n")
    ftxt.write(f"  df2 = {df2}\n")
    ftxt.write(f"  F crítico inferior (alpha/2): {f_crit_inf:.6f}\n")
    ftxt.write(f"  F crítico superior (1-alpha/2): {f_crit_sup:.6f}\n")

print(f"\nResultados guardados en: {OUT_FILE}")


# -----------------------------
# 6) Gráfico: Distribución F + críticos + observado
# -----------------------------
# Rango del eje X: lo ajustamos para que se vea bien el observado y el crítico superior
x_max = max(5.0, float(f_crit_sup) * 1.25, float(levene_stat) * 1.25)
x = np.linspace(0, x_max, 1200)
y = f.pdf(x, df1, df2)

plt.figure(figsize=(9, 5))
plt.plot(x, y, label="Distribución F")

# Líneas críticas y observado (estilo parecido a tu ejemplo)
plt.axvline(f_crit_inf, linestyle="--", label="Valor Crítico Inferior")
plt.axvline(f_crit_sup, linestyle="--", label="Valor Crítico Superior")
plt.axvline(levene_stat, linestyle="-", label="Valor Observado")

plt.title("Distribución F con valores críticos y valor observado")
plt.xlabel("Valor F")
plt.ylabel("Densidad de Probabilidad")
plt.legend()
plt.tight_layout()

plt.savefig(OUT_FIG, dpi=300)
plt.close()

print(f"Figura guardada en: {OUT_FIG}")
