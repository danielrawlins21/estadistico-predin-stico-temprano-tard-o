from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"
DATA_PATH = INPUT_DIR / "data.xlsx"

OUT_EARLY = OUTPUTS_DIR / "cranios_temprano.csv"
OUT_LATE = OUTPUTS_DIR / "cranios_tardio.csv"

COL_GROUP = "Época histórica"
COL_VALUE = "Anchura del cráneo"

EARLY_CODE = 1
LATE_CODE = 2

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"No encuentro el dataset en: {DATA_PATH.resolve()}")

    df = pd.read_excel(DATA_PATH)

    # Validaciones mínimas
    expected_cols = {COL_GROUP, COL_VALUE}
    missing = expected_cols - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas esperadas: {missing}. Columnas actuales: {list(df.columns)}")

    if df[[COL_GROUP, COL_VALUE]].isna().any().any():
        raise ValueError("Hay valores nulos en columnas clave (época o anchura).")

    # Asegura tipos numéricos (por si Excel viene raro)
    df[COL_GROUP] = pd.to_numeric(df[COL_GROUP], errors="raise")
    df[COL_VALUE] = pd.to_numeric(df[COL_VALUE], errors="raise")

    # Separación
    early = df[df[COL_GROUP] == EARLY_CODE].copy()
    late = df[df[COL_GROUP] == LATE_CODE].copy()

    # Validar que existan ambos grupos
    if early.empty or late.empty:
        counts = df[COL_GROUP].value_counts(dropna=False).to_dict()
        raise ValueError(
            f"No se detectaron ambos grupos {EARLY_CODE} y {LATE_CODE}. Conteo por época: {counts}"
        )

    OUTPUTS_DIR.mkdir(exist_ok=True)

    # Guardar solo la variable de interés (anchura), para facilitar análisis posteriores
    early[[COL_VALUE]].to_csv(OUT_EARLY, index=False)
    late[[COL_VALUE]].to_csv(OUT_LATE, index=False)

    # Log útil para Jira / informe
    print("OK ✅ Submuestras generadas")
    print(f"Temprano (época={EARLY_CODE}): {len(early)} filas → {OUT_EARLY}")
    print(f"Tardío  (época={LATE_CODE}): {len(late)} filas → {OUT_LATE}")
    print("\nResumen rápido (anchura):")
    print(f"Temprano mean={early[COL_VALUE].mean():.3f}, std={early[COL_VALUE].std(ddof=1):.3f}")
    print(f"Tardío   mean={late[COL_VALUE].mean():.3f}, std={late[COL_VALUE].std(ddof=1):.3f}")

if __name__ == "__main__":
    main()