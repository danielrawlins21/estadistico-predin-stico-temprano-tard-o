# Resultados del test de normalidad

## 1. Introducción

En este apartado se presentan los resultados de los tests de normalidad aplicados a la variable *anchura craneal* para cada uno de los periodos históricos analizados: predinástico temprano y predinástico tardío.

El objetivo de este contraste es evaluar si el supuesto de normalidad resulta razonable en cada submuestra, con el fin de contextualizar y discutir la validez de los análisis inferenciales posteriores.

El contraste se ha realizado de forma independiente para cada periodo, utilizando un nivel de significación \(\alpha = 0.05\).

En particular, se reporta el test de **Kolmogorov–Smirnov (KS)** por ser el solicitado en el enunciado, y se complementa con **Shapiro–Wilk** y la corrección de **Lilliefors** (una variante del KS cuando los parámetros de la normal se estiman a partir de la muestra), siguiendo las directrices indicadas en clase.

---

## 2. Resultados para el periodo predinástico temprano

Los resultados del test de Kolmogorov–Smirnov para la submuestra correspondiente al periodo **predinástico temprano** son los siguientes:

- **Estadístico KS:** 0.2425  
- **p-valor:** 0.0489


Además del KS, se aplicaron dos contrastes adicionales:

- **Shapiro–Wilk:** estadístico = 0.8378, p-valor = 0.0003 → **se rechaza H₀ (normalidad)**.
- **Lilliefors (KS corregido):** estadístico = 0.2425, p-valor = 0.0010 → **se rechaza H₀ (normalidad)**.
Dado que el p-valor obtenido es inferior al nivel de significación establecido (\(p < 0.05\)), se **rechaza la hipótesis nula de normalidad** para esta submuestra.

Este resultado indica que la distribución de la anchura craneal en el periodo predinástico temprano presenta desviaciones estadísticamente significativas respecto a una distribución normal. Dichas desviaciones son coherentes con las características observadas previamente en el análisis descriptivo y gráfico, como la asimetría positiva moderada y la curtosis elevada.

---

## 3. Resultados para el periodo predinástico tardío

Para la submuestra correspondiente al periodo **predinástico tardío**, los resultados del test de Kolmogorov–Smirnov son los siguientes:

- **Estadístico KS:** 0.2350  
- **p-valor:** 0.0611


Además del KS, se aplicaron dos contrastes adicionales:

- **Shapiro–Wilk:** estadístico = 0.8832, p-valor = 0.0033 → **se rechaza H₀ (normalidad)**.
- **Lilliefors (KS corregido):** estadístico = 0.2350, p-valor = 0.0010 → **se rechaza H₀ (normalidad)**.
En este caso, el p-valor es superior al nivel de significación (\(p > 0.05\)), por lo que **no se rechaza la hipótesis nula de normalidad**.

El resultado del KS sugiere compatibilidad con normalidad; sin embargo, **Shapiro–Wilk** y **Lilliefors** rechazan la hipótesis de normalidad (p < 0.05). Por tanto, la evidencia global apunta a que la normalidad estricta no es un supuesto robusto en esta submuestra, y el KS podría estar siendo menos sensible ante desviaciones moderadas.

---

## 4. Comparación e implicaciones metodológicas

La aplicación del test de normalidad revela un comportamiento diferente entre ambos periodos históricos:

- En el periodo predinástico temprano, **KS, Shapiro–Wilk y Lilliefors** rechazan la hipótesis de normalidad.
- En el periodo predinástico tardío, **KS no rechaza** la normalidad, pero **Shapiro–Wilk y Lilliefors sí la rechazan**, lo que sugiere que el KS podría estar teniendo menor potencia en este caso.

Estas diferencias indican que las distribuciones no solo difieren en su posición central y dispersión, sino también en su forma. En consecuencia, el supuesto de normalidad no se cumple de manera homogénea en ambas submuestras.

Este hecho deberá ser tenido en cuenta al aplicar y discutir los contrastes inferenciales posteriores, en particular el contraste de igualdad de medias mediante el test t, cuya validez teórica depende, entre otros factores, del cumplimiento del supuesto de normalidad.
En línea con las directrices del curso, cuando existen discrepancias entre el KS y tests más potentes para tamaños muestrales moderados (n≈30), se adopta una interpretación prudente priorizando **Shapiro–Wilk/Lilliefors**. En consecuencia, **no puede asumirse normalidad estricta en ninguna de las dos submuestras**. Este punto se tendrá en cuenta en los contrastes posteriores: se reportarán los tests paramétricos solicitados (p. ej., t de Student/Welch), pero se complementarán con alternativas no paramétricas (p. ej., Mann–Whitney) y una discusión explícita del impacto de los supuestos.


---

## 5. Consideraciones finales

Es importante destacar que no rechazar la hipótesis de normalidad no implica afirmar que los datos sean normales, sino únicamente que no se dispone de evidencia estadística suficiente para rechazar dicho supuesto.

Los resultados aquí presentados se utilizarán como base para interpretar críticamente los análisis inferenciales posteriores, tal y como se indica en el enunciado del ejercicio.

