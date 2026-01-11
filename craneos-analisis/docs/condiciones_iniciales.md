## HU-2.2 – Condiciones de aplicación del test t para la diferencia de medias

Antes de aplicar el test t para contrastar la igualdad de medias entre la anchura craneal del periodo predinástico temprano y tardío, es necesario analizar las condiciones bajo las cuales este contraste es válido.

### 1. Independencia de las muestras

El test t para dos muestras independientes requiere que las observaciones de cada grupo sean independientes entre sí y que no exista relación entre los valores de una muestra y los de la otra.

En este estudio, se asume de forma natural la independencia entre ambas muestras, ya que los cráneos pertenecen a individuos distintos y a periodos históricos diferentes. Además, el propio enunciado del ejercicio indica explícitamente que esta condición no es necesario comprobarla.

Por tanto, la condición de independencia se considera satisfecha.

---

### 2. Normalidad de las poblaciones

Otra condición fundamental del test t es que las poblaciones de las que proceden las muestras sigan una distribución normal.

En el ejercicio previo se aplicó el test de Kolmogorov–Smirnov para evaluar la normalidad de ambas submuestras. Los resultados indicaron que:

- La muestra correspondiente al periodo predinástico temprano no sigue estrictamente una distribución normal.
- La muestra del periodo predinástico tardío puede considerarse aproximadamente normal.

Por tanto, la condición de normalidad no se cumple de manera estricta para ambas poblaciones. Sin embargo, el test t es relativamente robusto frente a desviaciones moderadas de la normalidad, especialmente cuando los tamaños muestrales no son muy pequeños.

---

### 3. Igualdad de varianzas

El test t clásico para la diferencia de medias asume que ambas poblaciones tienen la misma varianza (homocedasticidad).

Dado que no se dispone de evidencia clara de igualdad de varianzas y con el fin de no imponer una restricción adicional innecesaria, se opta por utilizar el test t de Welch, que no requiere la suposición de varianzas iguales y es más robusto en situaciones reales.

---

### 4. Decisión metodológica

A pesar de que la condición de normalidad no se cumple estrictamente en una de las submuestras, se procede a realizar el contraste de hipótesis mediante el test t de Welch, tal y como se indica en el enunciado del ejercicio.

Esta decisión se justifica por la robustez del test, la independencia entre las muestras y la coherencia esperada con los intervalos de confianza obtenidos previamente. No obstante, los resultados del contraste deberán interpretarse con cautela y en conjunto con el análisis inferencial realizado en el apartado anterior.

## HU-2.2 – Comprobación de normalidad y homocedasticidad

Antes de aplicar el test t para la diferencia de medias, se analizan las condiciones de normalidad y homocedasticidad de las muestras, con el fin de evaluar la validez del contraste.

---

### 5. Normalidad de las submuestras

La normalidad de las distribuciones se evaluó previamente mediante el test de Kolmogorov–Smirnov. Los resultados obtenidos indicaron que:

- La submuestra correspondiente al periodo predinástico temprano no sigue estrictamente una distribución normal.
- La submuestra del periodo predinástico tardío puede considerarse aproximadamente normal.

Por tanto, la condición de normalidad no se cumple de manera estricta para ambas poblaciones. No obstante, el test t es relativamente robusto frente a desviaciones moderadas de la normalidad, especialmente cuando los tamaños muestrales no son muy pequeños.

---

## HU-2.2 – Comprobación de la homocedasticidad (test de Levene)

Con el fin de evaluar la igualdad de varianzas entre las submuestras correspondientes al periodo predinástico temprano y tardío, se aplicó el test de Levene, que resulta más robusto frente a desviaciones de la normalidad que otros contrastes clásicos.

---

### 1. Planteamiento del contraste

- **Hipótesis nula (H₀):** las varianzas poblacionales son iguales.  
- **Hipótesis alternativa (H₁):** las varianzas poblacionales son distintas.

El contraste se realiza con un nivel de significación \(\alpha = 0.05\).

---

### 2. Resultados obtenidos

El test de Levene aplicado a ambas submuestras arrojó los siguientes resultados:

- Tamaño muestral periodo predinástico temprano: \(n = 30\)  
- Tamaño muestral periodo predinástico tardío: \(n = 30\)  
- **Estadístico de Levene:** 0.6195  
- **p-valor:** 0.4344  

---

### 3. Interpretación estadística

Dado que el p-valor obtenido es claramente superior al nivel de significación considerado (\(p = 0.4344 > 0.05\)), no se rechaza la hipótesis nula de igualdad de varianzas.

Por tanto, no existe evidencia estadística suficiente para afirmar que las varianzas de la anchura craneal difieran entre los periodos predinástico temprano y tardío, por lo que la homocedasticidad puede considerarse plausible.

---

### 4. Implicaciones metodológicas

El cumplimiento de la condición de homocedasticidad permitiría, en principio, la aplicación del test t clásico para la diferencia de medias. No obstante, dado que la condición de normalidad no se cumple estrictamente para una de las submuestras, se opta por mantener el uso del test t de Welch en el contraste de hipótesis posterior.

Esta decisión garantiza una mayor robustez del análisis inferencial y resulta coherente con los supuestos observados en los datos.

