import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from pathlib import Path

# ---------------------------
# Configuración de rutas
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_DIR = BASE_DIR / "outputs"

FILE_TEMPRANO = OUTPUTS_DIR / "cranios_temprano.csv"
FILE_TARDIO = OUTPUTS_DIR / "cranios_tardio.csv"

FILE_TXT = OUTPUTS_DIR / "descriptivos_summary.txt"


# ---------------------------
# Función de descriptivos
# ---------------------------
def estadisticos_descriptivos(serie: pd.Series) -> dict:
    """
    Calcula medidas de centralización, dispersión y forma
    para una variable cuantitativa continua.
    """
    return {
        "n": serie.count(),
        "media": np.mean(serie),
        "mediana": np.median(serie),
        "varianza": np.var(serie, ddof=1),
        "desviacion_tipica": np.std(serie, ddof=1),
        "min": np.min(serie),
        "max": np.max(serie),
        "asimetria": skew(serie),
        "curtosis": kurtosis(serie, fisher=True)
    }

# ---------------------------
# Guardar resultados
# ---------------------------

def guardar_descriptivos_txt(path, titulo, descriptivos):
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"\n=== {titulo} ===\n")
        for k, v in descriptivos.items():
            if isinstance(v, float):
                f.write(f"{k:20s}: {v:.4f}\n")
            else:
                f.write(f"{k:20s}: {v}\n")

# ---------------------------
# Comparacion de descriptivos
# ---------------------------
def comparar_descriptivos(desc_temprano: dict, desc_tardio: dict) -> dict:
    """
    Compara estadísticos descriptivos entre submuestras.
    Devuelve diferencias clave (tardío - temprano).
    """
    comp = {
        "delta_media": desc_tardio["media"] - desc_temprano["media"],
        "delta_mediana": desc_tardio["mediana"] - desc_temprano["mediana"],
        "delta_varianza": desc_tardio["varianza"] - desc_temprano["varianza"],
        "delta_desviacion_tipica": desc_tardio["desviacion_tipica"] - desc_temprano["desviacion_tipica"],
        "delta_asimetria": desc_tardio["asimetria"] - desc_temprano["asimetria"],
        "delta_curtosis": desc_tardio["curtosis"] - desc_temprano["curtosis"],
        "delta_min": desc_tardio["min"] - desc_temprano["min"],
        "delta_max": desc_tardio["max"] - desc_temprano["max"],
    }
    return comp


# ---------------------------
# Carga de datos
# ---------------------------
def cargar_datos(path: Path) -> pd.Series:
    df = pd.read_csv(path)
    return df["Anchura del cráneo"]


# ---------------------------
# Ejecución principal
# ---------------------------
if __name__ == "__main__":

    anchura_temprano = cargar_datos(FILE_TEMPRANO)
    anchura_tardio = cargar_datos(FILE_TARDIO)

    desc_temprano = estadisticos_descriptivos(anchura_temprano)
    desc_tardio = estadisticos_descriptivos(anchura_tardio)

    comp = comparar_descriptivos(desc_temprano, desc_tardio)

    print("\n=== Predinástico temprano ===")
    for k, v in desc_temprano.items():
        print(f"{k:20s}: {v:.4f}" if isinstance(v, float) else f"{k:20s}: {v}")

    print("\n=== Predinástico tardío ===")
    for k, v in desc_tardio.items():
        print(f"{k:20s}: {v:.4f}" if isinstance(v, float) else f"{k:20s}: {v}")
    
    # Guardar en TXT
    # Limpiar archivo previo si existe
    with open(FILE_TXT, "w", encoding="utf-8") as f:
        f.write("Resumen de estadísticos descriptivos\n")

    guardar_descriptivos_txt(FILE_TXT, "Predinástico temprano", desc_temprano)
    guardar_descriptivos_txt(FILE_TXT, "Predinástico tardío", desc_tardio)
    guardar_descriptivos_txt(FILE_TXT, "Comparación (tardío - temprano)", comp)


    print("Resumen descriptivo guardado en:", FILE_TXT)