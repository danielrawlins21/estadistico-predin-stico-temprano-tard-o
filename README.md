# Proyecto: Análisis estadístico comparativo (Predinástico temprano vs tardío)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-academic--project-success)
![Reproducible](https://img.shields.io/badge/reproducible-yes-brightgreen)


Este repositorio contiene el flujo completo de análisis estadístico para comparar dos submuestras (“Predinástico temprano” y “Predinástico tardío”) siguiendo las directrices de la asignatura: análisis descriptivo, verificación de supuestos (normalidad y homocedasticidad), elección de pruebas paramétricas/no paramétricas, estimación con intervalos de confianza e interpretación de resultados. El trabajo sigue un **protocolo estadístico completo**, documentado y reproducible.

---

## 1) 🎯 Objetivo

Evaluar si existen **diferencias estadísticamente significativas** entre dos periodos (temprano vs tardío) para la variable de estudio (según el dataset del curso), mediante:

- **Exploración y descripción** (medias, desviaciones, distribución, gráficos).
- **Normalidad** (Kolmogorov–Smirnov, Shapiro–Wilk, Lilliefors cuando proceda).
- **Homocedasticidad** (Levene).
- **Contrastes de hipótesis**:
  - Paramétricos: t (incluyendo Welch si aplica).
  - No paramétricos: Mann–Whitney U si fallan supuestos.
- **Estimación** (diferencia de medias e intervalos de confianza).

---

## 2) Dataset

- Fuente: archivo proporcionado por el curso (formato `.xlsx`).
- Organización: el script carga el archivo y **separa en submuestras**:
  - `Predinástico temprano`
  - `Predinástico tardío`
- Tamaños muestrales utilizados en los contrastes principales:
  - `n_temprano = 30`
  - `n_tardío = 30`

---

## 3) 🧪 Metodología aplicada

### 3.1 Análisis descriptivo
- Estadísticos: media, mediana, desviación estándar, varianza, mínimos/máximos.
- Visualizaciones típicas: histograma, boxplot, KDE (si se utiliza).

### 3.2 Normalidad
Se aplicaron pruebas de normalidad con α = 0.05:

- **Kolmogorov–Smirnov (con estandarización)**:
  - Temprano: estadístico = 0.2425, p = 0.0489 → rechaza normalidad
  - Tardío: estadístico = 0.2350, p = 0.0611 → no se rechaza normalidad

### 3.3 Homocedasticidad
- **Levene**:
  - Estadístico = 0.619493
  - p = 0.434440
  - Decisión: no se rechaza H0

### 3.4 Contrastes principales
- **t de Welch**: t = 3.935446, p = 0.000233
- **Mann–Whitney U**: U = 217.5, p = 0.000330

### 3.5 Estimación
- Diferencia de medias (tardío – temprano): 0.933
- IC 90%: [0.537, 1.330]

### 3.6 📌 Resultados clave

| Análisis | Resultado |
|--------|----------|
| Normalidad (temprano) | No normal (KS p = 0.0489) |
| Normalidad (tardío) | Aproximadamente normal (KS p = 0.0611) |
| Homocedasticidad | Varianzas similares (Levene p = 0.4344) |
| t de Welch | p = 0.000233 |
| Mann–Whitney U | p = 0.000330 |
| Δ medias (tardío − temprano) | **0.933** |
| IC 90 % | [0.537, 1.330] |

👉 **Conclusión**: la anchura media difiere entre periodos y es mayor en el periodo predinástico tardío.

---

## 4) 📂 Estructura del proyecto (entrega final)

```text
craneos-analisis/
├── data/
│   └── data.xlsx
├── scripts/
│   └── analisis_craneos.py
├── outputs/
│   └── figures/
│       ├── histogramas_submuestras.png
│       ├── boxplot_temprano.png
│       ├── boxplot_tardio.png
│       ├── boxplot_comparativo.png
│       └── qqplot_comparativo.png
├── docs/
│   └── informe.tex
├── requirements.txt
└── README.md
```


## 5) ▶️ Reproducibilidad

### 5.1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5.2. Ejecutar el análisis completo
```bash
python scripts/analisis_craneos.py
```

El script maestro ejecuta el pipeline **de forma secuencial**, generando todas las salidas necesarias.

---

## 6) 📄 Informe

El informe académico completo (LaTeX/PDF) incluye:

- Descriptivos y gráficos  
- Tests de supuestos  
- Intervalos de confianza  
- Contrastes de hipótesis  
- Discusión crítica  
- Anexos de reproducibilidad  

---

## 7) 👤 Autor

**Daniel Olmedo Rawlins**  
Proyecto académico – enero  

## 8) ⚠️ Nota

Repositorio con fines **estrictamente académicos**.  
Los resultados y conclusiones son válidos únicamente para el dataset analizado.
