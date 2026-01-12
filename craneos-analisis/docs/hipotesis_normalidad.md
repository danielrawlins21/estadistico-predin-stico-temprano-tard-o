
# Hipótesis de Normalidad (Actualizadas)

## 1. Introducción
Con el objetivo de evaluar el supuesto de normalidad de la variable **anchura craneal** en los dos periodos históricos analizados (predinástico temprano y predinástico tardío), se plantean y contrastan las hipótesis estadísticas correspondientes.  
Además del test de Kolmogorov–Smirnov solicitado en el enunciado, se incorporan los tests de **Shapiro–Wilk** y **Lilliefors**, con el fin de reforzar el análisis, dada su mayor potencia en muestras de tamaño pequeño o moderado.

---

## 2. Tests de normalidad utilizados
Para cada submuestra se aplican los siguientes contrastes:

- **Kolmogorov–Smirnov (KS)** con estandarización previa de los datos.
- **Shapiro–Wilk**, especialmente adecuado para tamaños muestrales moderados.
- **Lilliefors**, variante del KS apropiada cuando los parámetros de la normal se estiman a partir de la muestra.

Los contrastes se realizan de forma independiente para cada periodo histórico.

---

## 3. Formulación general de las hipótesis
Las hipótesis contrastadas, comunes a los tres tests aplicados, son:

- **Hipótesis nula (H₀):** la variable *anchura craneal* sigue una distribución normal.
- **Hipótesis alternativa (H₁):** la variable *anchura craneal* no sigue una distribución normal.

Se adopta un nivel de significación \( \alpha = 0.05 \).  
El contraste es bilateral, al pretender detectar cualquier tipo de desviación respecto a la normalidad.

---

## 4. Hipótesis para el periodo predinástico temprano
Para la submuestra correspondiente al periodo **predinástico temprano**, se plantean:

- **H₀ (temprano):** la anchura craneal en el periodo predinástico temprano sigue una distribución normal.
- **H₁ (temprano):** la anchura craneal en el periodo predinástico temprano no sigue una distribución normal.

Estas hipótesis se contrastan mediante los tests KS, Shapiro–Wilk y Lilliefors.

---

## 5. Hipótesis para el periodo predinástico tardío
Para la submuestra correspondiente al periodo **predinástico tardío**, se formulan:

- **H₀ (tardío):** la anchura craneal en el periodo predinástico tardío sigue una distribución normal.
- **H₁ (tardío):** la anchura craneal en el periodo predinástico tardío no sigue una distribución normal.

De nuevo, estas hipótesis se evalúan utilizando los tres contrastes de normalidad mencionados.

---

## 6. Criterio de decisión e interpretación conjunta
Para cada test aplicado se sigue el criterio:

- Si el *p-valor* > \( \alpha \), no se rechaza H₀.
- Si el *p-valor* ≤ \( \alpha \), se rechaza H₀.

Dado que los tests presentan distinta potencia, en caso de discrepancia entre resultados se interpretarán con cautela, otorgando mayor peso a **Shapiro–Wilk y Lilliefors**, por ser más adecuados cuando los parámetros de la distribución normal se estiman a partir de la muestra.

---

## 7. Relación con el análisis inferencial posterior
Las conclusiones obtenidas sobre la normalidad servirán para contextualizar la validez de los contrastes inferenciales posteriores (por ejemplo, el test t para la diferencia de medias).  
En caso de que el supuesto de normalidad no se cumpla estrictamente, los resultados paramétricos se interpretarán con prudencia y se complementarán, cuando proceda, con alternativas no paramétricas.
