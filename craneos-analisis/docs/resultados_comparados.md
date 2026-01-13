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
