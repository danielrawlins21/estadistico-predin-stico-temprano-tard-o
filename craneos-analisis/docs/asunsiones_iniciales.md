# Supuestos iniciales del análisis

## 1. Naturaleza de los datos
El conjunto de datos está compuesto por 60 observaciones correspondientes a la anchura de cráneos humanos (en milímetros) procedentes de un yacimiento arqueológico egipcio. Cada observación se clasifica según la variable dicotómica *Época histórica*, con valores 1 (predinástico temprano) y 2 (predinástico tardío).

Se asume que las mediciones son cuantitativas, comparables entre sí y obtenidas bajo un mismo criterio antropométrico.

---

## 2. Independencia de las observaciones
Se asume que las observaciones son independientes entre sí, es decir, que la anchura de un cráneo no influye en la anchura de otro. Esta hipótesis se considera razonable dado que cada medición corresponde a un individuo distinto.

---

## 3. Presencia de valores repetidos
El análisis exploratorio muestra un número elevado de valores repetidos (duplicados). Se asume que estos duplicados no corresponden a errores de medición ni de registro, sino a valores reales coincidentes en la anchura de los cráneos, lo cual es plausible en estudios antropométricos.

Por tanto, no se eliminan observaciones duplicadas.

---

## 4. Normalidad de las distribuciones
No se asume a priori que las submuestras correspondientes a cada periodo histórico sigan una distribución normal. La normalidad será evaluada explícitamente mediante el test de Kolmogorov-Smirnov antes de aplicar contrastes paramétricos.

---

## 5. Homogeneidad de varianzas
Inicialmente no se asume igualdad de varianzas entre ambos periodos históricos. Esta condición será evaluada indirectamente en el análisis inferencial y discutida en relación con la validez del test t para la diferencia de medias.

---

## 6. Nivel de significación
Salvo que se indique lo contrario, se trabajará con niveles de confianza del 90%, 95% y 99%, y con un nivel de significación α = 0.05 para los contrastes de hipótesis.

---

## 7. Objetivo del análisis
El objetivo principal es determinar si existen diferencias estadísticamente significativas en la anchura media de los cráneos entre el periodo predinástico temprano y el tardío, y contextualizar los resultados desde un punto de vista histórico y antropométrico.
