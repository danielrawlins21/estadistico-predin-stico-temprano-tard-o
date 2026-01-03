from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/data.xlsx")
OUT_PROFILE = Path("outputs/profile_summary.txt")
OUT_SAMPLE = Path("outputs/sample_rows.csv")

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"No encuentro el dataset en: {DATA_PATH.resolve()}")

    # Carga del Excel
    df = pd.read_excel(DATA_PATH)

    Path("outputs").mkdir(exist_ok=True)

    lines = []
    lines.append("=== PERFIL BÁSICO DEL DATASET ===")
    lines.append(f"Filas: {len(df)}")
    lines.append(f"Columnas: {df.shape[1]}")
    lines.append("")

    lines.append("=== COLUMNAS Y TIPOS ===")
    lines.append(str(df.dtypes))
    lines.append("")

    lines.append("=== NULOS POR COLUMNA ===")
    lines.append(str(df.isna().sum().sort_values(ascending=False)))
    lines.append("")

    lines.append("=== DUPLICADOS (FILAS COMPLETAS) ===")
    lines.append(str(df.duplicated().sum()))
    lines.append("")

    lines.append("=== DESCRIPTIVO (NUMÉRICAS) ===")
    num = df.select_dtypes(include="number")
    if not num.empty:
        lines.append(str(num.describe().T))
    else:
        lines.append("No hay columnas numéricas.")
    lines.append("")

    lines.append("=== VALORES ÚNICOS (CATEGÓRICAS, top 20) ===")
    cat = df.select_dtypes(exclude="number")
    if not cat.empty:
        for c in cat.columns:
            lines.append(f"\n-- {c} --")
            lines.append(str(df[c].value_counts(dropna=False).head(20)))
    else:
        lines.append("No hay columnas categóricas.")

    OUT_PROFILE.write_text("\n".join(lines), encoding="utf-8")
    df.head(30).to_csv(OUT_SAMPLE, index=False)

    print("OK ✅ Dataset cargado correctamente")
    print(f"Perfil: {OUT_PROFILE}")
    print(f"Muestra: {OUT_SAMPLE}")

if __name__ == "__main__":
    main()