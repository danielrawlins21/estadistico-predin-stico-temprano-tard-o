# Protocolo estadístico y validación de supuestos

## 1. Objetivo del protocolo

El objetivo de este apartado es documentar de forma clara y sistemática las pruebas estadísticas utilizadas en el análisis, los supuestos evaluados, los resultados obtenidos y las decisiones metodológicas adoptadas. Este protocolo permite justificar la elección de los contrastes aplicados y evaluar la validez de las conclusiones alcanzadas.

---

## 2. Tabla resumen de supuestos, pruebas y decisiones

| Aspecto evaluado | Supuesto estadístico | Prueba aplicada | Resultado principal | Decisión (α = 0.05) | Implicación para el análisis |
|-----------------|---------------------|-----------------|--------------------|---------------------|------------------------------|
| Distribución – Predinástico temprano | Normalidad | Kolmogorov–Smirnov | p = 0.0489 | Se rechaza H₀ | Existen evidencias de desviación de la normalidad; se recomienda cautela con pruebas paramétricas |
| Distribución – Predinástico tardío | Normalidad | Kolmogorov–Smirnov | p = 0.0611 | No se rechaza H₀ | Normalidad plausible; el uso de pruebas paramétricas es razonable |
| Igualdad de varianzas | Homocedasticidad | Test de Levene | p = 0.4344 | No se rechaza H₀ | No hay evidencia de heterocedasticidad; varianzas similares entre grupos |
| Comparación de medias | Diferencia entre medias | Test t de Welch | p = 0.000233 | Se rechaza H₀ | Diferencia estadísticamente significativa entre los periodos históricos |
| Comparación alternativa | Diferencia en rangos | Mann–Whitney U | p < 0.001 | Se rechaza H₀ | Resultado consistente con el contraste paramétrico |

---

## 3. Interpretación metodológica y crítica

El análisis de normalidad indica que la submuestra correspondiente al periodo predinástico temprano presenta una desviación estadísticamente significativa respecto a la distribución normal, mientras que la submuestra del periodo predinástico tardío no muestra evidencias suficientes para rechazar dicho supuesto. Esta situación sugiere que el cumplimiento de la normalidad no es homogéneo entre ambos grupos.

Por otro lado, el test de Levene no detecta diferencias significativas entre las varianzas de las dos submuestras, lo que permite asumir homocedasticidad de forma razonable. Dado que uno de los supuestos de normalidad no se cumple estrictamente, se opta por aplicar el test t de Welch, que es más robusto frente a desviaciones de normalidad y posibles desigualdades de varianza.

Adicionalmente, se emplea la prueba no paramétrica de Mann–Whitney U como contraste alternativo. La concordancia entre los resultados obtenidos mediante enfoques paramétricos y no paramétricos refuerza la solidez de la conclusión principal, según la cual existen diferencias estadísticamente significativas en la anchura de los cráneos entre los periodos predinástico temprano y tardío.

---

## 4. Implicaciones para el análisis posterior

La validación de los supuestos y la coherencia entre distintos contrastes permiten interpretar con mayor confianza los intervalos de confianza y las conclusiones inferenciales que se presentan en los apartados siguientes, sin perder de vista las limitaciones asociadas al tamaño muestral y a las desviaciones observadas en la distribución de los datos.


# Limitaciones metodológicas del análisis

El presente análisis estadístico permite identificar diferencias significativas en la anchura de los cráneos entre los periodos predinástico temprano y predinástico tardío. No obstante, los resultados deben interpretarse teniendo en cuenta una serie de limitaciones metodológicas que pueden afectar al alcance y generalización de las conclusiones.

En primer lugar, el supuesto de normalidad no se cumple estrictamente en la submuestra correspondiente al periodo predinástico temprano, según el test de Kolmogorov–Smirnov. Aunque el tamaño muestral es moderado (n = 30) y se han empleado contrastes robustos como el test t de Welch, esta desviación de la normalidad puede influir en la precisión de las estimaciones paramétricas y en la interpretación de los intervalos de confianza.

En segundo lugar, aunque el test de Levene no detecta diferencias significativas entre las varianzas de ambos grupos, la comprobación de homocedasticidad se basa en pruebas estadísticas que pueden tener potencia limitada en muestras de tamaño moderado. Por tanto, no puede descartarse completamente la existencia de diferencias sutiles en la dispersión de las distribuciones.

Asimismo, el análisis asume la independencia entre las observaciones de ambas submuestras, condición que se admite de forma natural dado el contexto arqueológico del estudio. No obstante, la ausencia de información adicional sobre el proceso de muestreo o sobre posibles relaciones entre los restos analizados limita la verificación empírica de este supuesto.

Por otra parte, el uso de pruebas no paramétricas, como el test de Mann–Whitney U, permite reforzar la robustez de las conclusiones al no depender de supuestos de normalidad. Sin embargo, estas pruebas contrastan diferencias en la distribución o en los rangos, y no directamente en las medias, lo que implica una ligera diferencia en la interpretación del efecto observado.

Finalmente, el tamaño muestral y la naturaleza específica del yacimiento arqueológico analizado restringen la generalización de los resultados a otras poblaciones o periodos históricos. Las conclusiones obtenidas deben entenderse como válidas para el conjunto de datos analizado, y no necesariamente extrapolables a contextos más amplios sin evidencia adicional.

En conjunto, estas limitaciones no invalidan los resultados obtenidos, pero sí subrayan la necesidad de interpretarlos con cautela y dentro del marco metodológico en el que han sido obtenidos.


# Conclusiones generales y coherencia inferencial

## 1. Síntesis de los resultados estadísticos

El análisis estadístico realizado sobre la anchura de los cráneos egipcios correspondientes a los periodos predinástico temprano y predinástico tardío revela diferencias consistentes y estadísticamente significativas entre ambos grupos.

En primer lugar, el análisis descriptivo mostró que la media de la anchura craneal es mayor en el periodo predinástico tardío que en el periodo temprano, acompañada de una distribución ligeramente diferente en términos de dispersión y forma. Estas diferencias iniciales fueron visibles tanto en las medidas resumen como en los diagramas de caja y bigotes.

La evaluación de los supuestos estadísticos indicó que la normalidad no se cumple estrictamente en la submuestra del periodo predinástico temprano, mientras que sí resulta plausible en la submuestra tardía. No obstante, el test de Levene no detectó diferencias significativas entre las varianzas de ambos grupos, lo que sugiere homocedasticidad razonable.

---

## 2. Coherencia entre intervalos de confianza y contrastes de hipótesis

Los intervalos de confianza para la diferencia de medias de la anchura craneal, calculados para niveles de confianza del 90%, 95% y 99%, no incluyen el valor cero en ninguno de los casos. Este resultado indica que la diferencia observada entre periodos no solo es estadísticamente significativa, sino también estable frente a variaciones en el nivel de confianza considerado.

La coherencia entre los intervalos de confianza y el resultado del test t de Welch, que conduce al rechazo de la hipótesis nula de igualdad de medias (p ≈ 0.00023), refuerza la solidez de la inferencia realizada. Ambos enfoques apuntan en la misma dirección: la anchura media de los cráneos es significativamente mayor en el periodo predinástico tardío que en el temprano.

---

## 3. Comparación entre enfoques paramétricos y no paramétricos

Dado que uno de los supuestos de normalidad no se cumple estrictamente, se aplicó de forma complementaria la prueba no paramétrica de Mann–Whitney U. Este contraste también condujo al rechazo de la hipótesis nula de igualdad de distribuciones entre ambos periodos (p < 0.001).

La concordancia entre los resultados obtenidos mediante el test t de Welch y el test de Mann–Whitney U sugiere que la conclusión principal no depende de manera crítica del cumplimiento estricto de los supuestos paramétricos. Esto aporta robustez adicional al análisis y reduce la probabilidad de que la diferencia observada sea un artefacto metodológico.

---

## 4. Interpretación sustantiva (storytelling)

Desde el punto de vista sustantivo, los resultados indican que, en el conjunto de datos analizado, los cráneos correspondientes al periodo predinástico tardío presentan una mayor anchura media que los del periodo predinástico temprano. En términos históricos y antropológicos, este hallazgo es coherente con la hipótesis de una transición progresiva hacia formas craneales más anchas a medida que avanza el tiempo, en línea con la intuición planteada al inicio del estudio.

Así, a la pregunta “¿en qué época la cabeza era más ancha?”, la evidencia estadística obtenida permite responder, con un alto grado de confianza, que la anchura craneal es mayor en el periodo predinástico tardío.

---

## 5. Conclusión final

En conjunto, el análisis descriptivo, la validación de supuestos, los intervalos de confianza y los contrastes de hipótesis conducen a una conclusión consistente: existen diferencias estadísticamente significativas y sustantivamente relevantes en la anchura de los cráneos entre los periodos predinástico temprano y predinástico tardío, siendo mayor la anchura en este último.

Estas conclusiones deben interpretarse dentro de las limitaciones metodológicas expuestas, pero cuentan con un respaldo inferencial sólido gracias a la coherencia entre los distintos métodos estadísticos empleados.
