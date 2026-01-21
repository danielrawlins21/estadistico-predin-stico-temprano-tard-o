# ============================================================
# HU-2.2 – Test t para la diferencia de medias (Welch)
# ============================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

# -----------------------------
# 1) Configuración
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUT_DIR = BASE_DIR / "outputs"
FILE_TEMPRANO = OUT_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUT_DIR / "cranios_tardio.csv"

OUT_FILE = OUT_DIR / "resultados_t_welch.txt"
OUT_PLOT = OUT_DIR / "figures/test_t_distribucion.png"

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
    equal_var=False
)

decision = (
    "Se rechaza H0 (diferencia significativa de medias)"
    if p_value <= ALPHA
    else "No se rechaza H0 (no hay evidencia de diferencia)"
)

# -----------------------------
# 4) Grados de libertad de Welch
# -----------------------------
n1, n2 = len(tardio), len(temprano)
s1, s2 = np.var(tardio, ddof=1), np.var(temprano, ddof=1)

df_welch = (s1/n1 + s2/n2)**2 / (
    (s1**2) / (n1**2 * (n1 - 1)) +
    (s2**2) / (n2**2 * (n2 - 1))
)

# -----------------------------
# 5) Gráfico de la distribución t
# -----------------------------
x = np.linspace(-6, 6, 1000)
y = stats.t.pdf(x, df_welch)

t_crit_low = stats.t.ppf(ALPHA / 2, df_welch)
t_crit_high = stats.t.ppf(1 - ALPHA / 2, df_welch)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Distribución t", linewidth=2)

plt.axvline(t_crit_low, color="red", linestyle="--",
            label="Valor crítico")
plt.axvline(t_crit_high, color="red", linestyle="--")

plt.axvline(t_stat, color="green", linestyle="-",
            label="Valor t observado")

plt.xlabel("Valor t")
plt.ylabel("Densidad de probabilidad")
plt.title("Distribución t con valor crítico y valor t observado")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_PLOT, dpi=300)
plt.close()

# -----------------------------
# 6) Salida por consola
# -----------------------------
print("=== HU-2.2 – Test t de Welch ===")
print(f"Estadístico t: {t_stat:.6f}")
print(f"p-valor: {p_value:.6f}")
print(f"Grados de libertad (Welch): {df_welch:.2f}")
print(f"alpha: {ALPHA}")
print(f"Decisión: {decision}")

# -----------------------------
# 7) Guardar resultados
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
    f.write(f"Grados de libertad (Welch): {df_welch:.2f}\n")
    f.write(f"alpha: {ALPHA}\n\n")
    f.write(f"Decisión: {decision}\n")

print(f"\nResultados guardados en: {OUT_FILE}")
print(f"Gráfico guardado en: {OUT_PLOT}")
