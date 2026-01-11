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
