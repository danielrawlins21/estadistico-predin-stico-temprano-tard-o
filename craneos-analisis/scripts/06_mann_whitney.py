"""
HU-2.2 – Contraste no paramétrico
Test de Mann–Whitney U para la diferencia de anchura craneal
Periodo predinástico temprano vs tardío
"""

import pandas as pd
from scipy.stats import mannwhitneyu
from pathlib import Path

# --------------------------------------------------
# Parámetros generales
# --------------------------------------------------
ALPHA = 0.05

# --------------------------------------------------
# Rutas del proyecto
# (ajusta solo si tu estructura es distinta)
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"

FILE_TEMPRANO = OUTPUTS_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUTPUTS_DIR / "cranios_tardio.csv"
FILE_TXT = OUTPUTS_DIR / "mann_whitney.txt"

# --------------------------------------------------
# Carga de datos
# --------------------------------------------------
temprano = pd.read_csv(FILE_TEMPRANO)["Anchura del cráneo"].dropna()
tardio = pd.read_csv(FILE_TARDIO)["Anchura del cráneo"].dropna()

n_temprano = len(temprano)
n_tardio = len(tardio)

# --------------------------------------------------
# Test de Mann–Whitney U (bilateral)
# --------------------------------------------------
u_stat, p_val = mannwhitneyu(
    temprano,
    tardio,
    alternative="two-sided"
)

# --------------------------------------------------
# Decisión estadística
# --------------------------------------------------
if p_val < ALPHA:
    decision = "Se rechaza H0 (diferencias estadísticamente significativas)"
else:
    decision = "No se rechaza H0 (no se detectan diferencias significativas)"

# --------------------------------------------------
# Guardar resultados en TXT
# --------------------------------------------------
with open(FILE_TXT, "w", encoding="utf-8") as f:
    f.write("Test de Mann–Whitney U\n")
    f.write("======================\n\n")

    f.write("Justificación:\n")
    f.write(
        "Se aplica el test no paramétrico de Mann–Whitney U debido a que los\n"
        "tests de normalidad (KS, Shapiro–Wilk y Lilliefors) indican que no puede\n"
        "asumirse normalidad estricta en las submuestras.\n\n"
    )

    f.write("Hipótesis:\n")
    f.write("H0: Las distribuciones de la anchura craneal son iguales en ambos periodos.\n")
    f.write("H1: Las distribuciones de la anchura craneal son distintas.\n\n")

    f.write("Datos:\n")
    f.write(f"n predinástico temprano = {n_temprano}\n")
    f.write(f"n predinástico tardío   = {n_tardio}\n\n")

    f.write("Resultados:\n")
    f.write(f"Estadístico U = {u_stat:.4f}\n")
    f.write(f"p-valor       = {p_val:.6f}\n")
    f.write(f"alpha         = {ALPHA}\n\n")

    f.write("Decisión:\n")
    f.write(decision + "\n\n")

    f.write(
        "Interpretación:\n"
        "El contraste de Mann–Whitney evalúa diferencias en la posición central\n"
        "de las distribuciones mediante rangos, sin asumir normalidad. El resultado\n"
        "se utilizará para contrastar la robustez de las conclusiones obtenidas\n"
        "mediante el test t de Welch.\n"
    )

# --------------------------------------------------
# Salida por consola
# --------------------------------------------------
print("=== Test de Mann–Whitney U ===")
print(f"U = {u_stat:.4f}")
print(f"p-valor = {p_val:.6f}")
print(f"Decisión (alpha={ALPHA}): {decision}")
print("\nResultados guardados en:", FILE_TXT)
