import subprocess
import sys
from pathlib import Path

# -----------------------------
# Configuración
# -----------------------------
SCRIPTS_DIR = Path(__file__).parent

PIPELINE = [
    "01_load_and_profile.py",
    "02_split_samples.py",
    "03_descriptivos.py",
    "04_graficos_boxplots.py",
    "04_graficos_histogramas.py",
    "04_graficos_qqplots.py",
    "05_normalidad_ks.py",
    "07_homocedasticidad_levene.py",
    "06_IC_medias.py",
    "06_mann_whitney.py",
    "08_test_t_welch.py",
]

# -----------------------------
# Ejecutor
# -----------------------------
def run_script(script_name):
    script_path = SCRIPTS_DIR / script_name

    if not script_path.exists():
        print(f"❌ ERROR: No se encontró {script_name}")
        sys.exit(1)

    print(f"\n▶ Ejecutando: {script_name}")
    print("-" * 60)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=False
    )

    if result.returncode != 0:
        print(f"\n❌ ERROR en {script_name}. Ejecución detenida.")
        sys.exit(result.returncode)

    print(f"✅ Finalizado: {script_name}")

# -----------------------------
# Main
# -----------------------------
def main():
    print("=" * 60)
    print("ANÁLISIS ESTADÍSTICO DE ANCHURAS CRANEALES")
    print("Ejecución secuencial del pipeline")
    print("=" * 60)

    for script in PIPELINE:
        run_script(script)

    print("\n🎉 Pipeline completado correctamente.")
    print("Resultados disponibles en /outputs")

if __name__ == "__main__":
    main()
