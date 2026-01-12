import pandas as pd
import numpy as np
from scipy.stats import kstest, shapiro
from statsmodels.stats.diagnostic import lilliefors
from pathlib import Path

# ---------------------------
# Rutas
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"

FILE_TEMPRANO = OUTPUTS_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUTPUTS_DIR / "cranios_tardio.csv"
FILE_TXT = OUTPUTS_DIR / "normalidad_tests.txt"  

ALPHA = 0.05


# ---------------------------
# Funciones de normalidad
# ---------------------------
def ks_normalidad_estandarizada(serie: pd.Series):
    """
    KS para normalidad tras estandarizar los datos (z-scores).
    """
    media = serie.mean()
    std = serie.std(ddof=1)

    # Evitar división por cero si std fuese 0 (muy raro, pero robustez)
    if std == 0 or np.isnan(std):
        return np.nan, np.nan

    z = (serie - media) / std
    estadistico, p_valor = kstest(z, "norm")
    return estadistico, p_valor


def shapiro_normalidad(serie: pd.Series):
    """
    Shapiro-Wilk (recomendado para n pequeño/mediano).
    """
    estadistico, p_valor = shapiro(serie)
    return estadistico, p_valor


def lilliefors_normalidad(serie: pd.Series):
    """
    Lilliefors (KS corregido cuando mu y sigma se estiman de la muestra).
    """
    estadistico, p_valor = lilliefors(serie)  # 'norm' por defecto
    return estadistico, p_valor


def decision(p_valor: float, alpha: float = ALPHA) -> str:
    if np.isnan(p_valor):
        return "No evaluable"
    return "Rechazar H0" if p_valor < alpha else "No rechazar H0"


def write_block(f, label: str, serie: pd.Series):
    n = len(serie)

    ks_stat, ks_p = ks_normalidad_estandarizada(serie)
    sh_stat, sh_p = shapiro_normalidad(serie)
    lf_stat, lf_p = lilliefors_normalidad(serie)

    f.write(f"{label}\n")
    f.write(f"n = {n}\n\n")

    f.write("H0: la muestra proviene de una distribución Normal.\n")
    f.write("H1: la muestra NO proviene de una distribución Normal.\n\n")

    f.write("Kolmogorov–Smirnov (con estandarización)\n")
    f.write(f"  Estadístico: {ks_stat:.4f}\n")
    f.write(f"  p-valor    : {ks_p:.4f}\n")
    f.write(f"  Decisión   : {decision(ks_p)} (alpha={ALPHA})\n\n")

    f.write("Shapiro–Wilk\n")
    f.write(f"  Estadístico: {sh_stat:.4f}\n")
    f.write(f"  p-valor    : {sh_p:.4f}\n")
    f.write(f"  Decisión   : {decision(sh_p)} (alpha={ALPHA})\n\n")

    f.write("Lilliefors (KS corregido)\n")
    f.write(f"  Estadístico: {lf_stat:.4f}\n")
    f.write(f"  p-valor    : {lf_p:.4f}\n")
    f.write(f"  Decisión   : {decision(lf_p)} (alpha={ALPHA})\n\n")

    # Mini comparación (útil para el informe)
    f.write("Comentario breve\n")
    f.write(
        "  - KS se reporta porque lo solicita el enunciado.\n"
        "  - Shapiro–Wilk y Lilliefors suelen ser más potentes/adecuados en n pequeño-mediano.\n"
        "  - Si hay discrepancias entre tests, se interpreta con cautela y se justifica.\n"
    )
    f.write("\n" + "-" * 60 + "\n\n")


# ---------------------------
# Carga de datos
# ---------------------------
temprano = pd.read_csv(FILE_TEMPRANO)["Anchura del cráneo"].dropna()
tardio = pd.read_csv(FILE_TARDIO)["Anchura del cráneo"].dropna()

# ---------------------------
# Guardar resultados
# ---------------------------
with open(FILE_TXT, "w", encoding="utf-8") as f:
    f.write("Tests de normalidad: KS + Shapiro–Wilk + Lilliefors\n")
    f.write("===================================================\n\n")
    f.write(f"alpha = {ALPHA}\n\n")

    write_block(f, "Predinástico temprano", temprano)
    write_block(f, "Predinástico tardío", tardio)

print("Resultados de normalidad guardados en:", FILE_TXT)
