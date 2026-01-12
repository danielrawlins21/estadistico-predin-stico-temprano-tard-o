
## HU-2.2 – Contraste no paramétrico: test de Mann–Whitney U

### 1. Justificación metodológica
Los tests de normalidad (Kolmogorov–Smirnov, Shapiro–Wilk y Lilliefors) indican que no puede asumirse normalidad estricta en ninguna de las dos submuestras.  
Por este motivo, y siguiendo las directrices del profesor, se complementa el contraste paramétrico (test t de Welch) con una **alternativa no paramétrica**, el test de Mann–Whitney U.

Este contraste no requiere normalidad y compara la posición central de las distribuciones mediante rangos.

---

### 2. Planteamiento del contraste
- **Hipótesis nula (H₀):** las distribuciones de la anchura craneal en los periodos predinástico temprano y tardío son iguales.
- **Hipótesis alternativa (H₁):** las distribuciones de la anchura craneal en ambos periodos son distintas.

Se utiliza un nivel de significación \(\alpha = 0.05\).

---

### 3. Resultados obtenidos
- Tamaño muestral periodo predinástico temprano: \(n = 30\)
- Tamaño muestral periodo predinástico tardío: \(n = 30\)
- **Estadístico U:** 217.5  
- **p-valor:** 0.00033  

Con un nivel de significación del 5%, el test de Mann–Whitney **rechaza la hipótesis nula**, indicando que **existe evidencia estadísticamente significativa** de diferencias entre ambos periodos.

---

### 4. Comparación con el test t de Welch
El contraste paramétrico mediante el test t de Welch arrojó un p-valor de \(p = 0.000233\), rechazando igualmente la hipótesis nula de igualdad de medias.

La coincidencia entre ambos contrastes se analiza de forma crítica, teniendo en cuenta que:
- El test t de Welch compara medias bajo supuestos aproximados.
- El test de Mann–Whitney compara distribuciones mediante rangos, sin asumir normalidad.

El hecho de que ambos contrastes conduzcan a la misma decisión refuerza la solidez de la conclusión inferencial.

---

### 5. Interpretación conjunta y cierre metodológico
La comparación entre el test t de Welch y el test de Mann–Whitney permite evaluar la **robustez de las conclusiones** frente al incumplimiento del supuesto de normalidad.

En este caso, la coincidencia entre ambos contrastes refuerza la evidencia de diferencias reales en la anchura craneal entre los periodos predinástico temprano y tardío.  
Por tanto, puede afirmarse que la diferencia observada no depende del método estadístico empleado, sino que refleja una diferencia estructural entre ambas poblaciones.

Con este análisis se da por **cerrada la HU-2.2**, habiendo contrastado la hipótesis de igualdad de medias mediante enfoques paramétricos y no paramétricos y documentado de forma crítica sus condiciones de aplicación.
